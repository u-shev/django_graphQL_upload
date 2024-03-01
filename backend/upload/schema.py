import graphene
from graphene_django import DjangoObjectType
from .models import File
from graphene_file_upload.scalars import Upload


class FilesType(DjangoObjectType):
    class Meta:
        model = File
        fields = ("id", "file", "uploaded_at", "processed")

class Query(graphene.ObjectType):

    all_files = graphene.List(FilesType)

    def resolve_all_files(root, info):
        return File.objects.all()


class UploadMutation(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)

    success = graphene.Boolean()

    def mutate(self, info, file, **kwargs):
        # do something with your file

        return UploadMutation(success=True)

schema = graphene.Schema(query=Query, mutation=UploadMutation)