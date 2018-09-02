from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver


class PhotoUpload(models.Model):
    photo = models.ImageField(upload_to='photos')
    user = models.ForeignKey(get_user_model())
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Photo Upload"
        verbose_name_plural = "Photo Uploads"

    def __str__(self):
        return '{}'.format(self.pk)


@receiver(models.signals. pre_delete, sender=PhotoUpload, )
def remove_file_from_s3(sender, instance, using, **kwargs):
        instance.photo.delete(save=False)
