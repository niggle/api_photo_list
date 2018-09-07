from rest_framework import serializers

from photos.models import PhotoUpload


class PhotoUploadSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = PhotoUpload
        fields = ('photo', 'user', 'thumbnail')

    def get_thumbnail(self, obj):
        return obj.image.url if obj.image.name else None

