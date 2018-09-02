from rest_framework import serializers

from photos.models import PhotoUpload


class PhotoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoUpload
        fields = ('photo', 'user')