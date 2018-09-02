import tempfile
from unittest import TestCase

from django.contrib.auth import get_user_model

from photos.models import PhotoUpload


class PhotoUploadTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test', email='test@test.pt', password='testpass')

    def test_add_record_to_photoupload(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        obj = PhotoUpload.objects.create(photo=image, user=self.user)

        self.assertTrue(isinstance(obj, PhotoUpload))
        self.assertEqual(obj.__str__(), '{}'.format(obj.pk))
        self.assertTrue(obj.created)
        self.assertEqual(obj.user, self.user)
        self.assertEqual(obj.photo.name, image)
