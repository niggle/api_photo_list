from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response

from photos.models import PhotoUpload
from photos.serializers import PhotoUploadSerializer


class PhotoUploadListCreate(ListCreateAPIView):
    """
    API endpoint that allows photos to be viewed.
    """
    queryset = PhotoUpload.objects.all()
    serializer_class = PhotoUploadSerializer
    http_method_names = ('get', 'post')
    parser_classes = (MultiPartParser,)




