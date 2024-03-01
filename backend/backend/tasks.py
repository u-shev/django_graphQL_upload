from celery import shared_task
from upload.models import File
from django.conf import settings




@shared_task
def process_file(file_id=None):
    file = File.objects.get(pk=file_id)
    file_path = settings.MEDIA_ROOT / file.file.name


    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    updated_text = text.replace("ё", "е").replace('Ё', 'Е')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_text)


    file.processed = True
    file.save()
