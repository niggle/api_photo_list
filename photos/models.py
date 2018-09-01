from django.contrib.auth import get_user_model
from django.db import models


class PhotoUpload(models.Model):
    photo = models.ImageField()
    user = models.ForeignKey(get_user_model())
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Photo Upload"
        verbose_name_plural = "Photo Uploads"

    def __str__(self):
        return self.pk
