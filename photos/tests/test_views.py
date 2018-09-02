from PIL import Image
from io import BytesIO

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase

from photos.models import PhotoUpload
from photos.serializers import PhotoUploadSerializer


class ProductTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_view', email='test@test.pt', password='testpass')

    def test_can_get_photo_list(self):
        for item in range(3):
            photo = self.generate_photo_file()
            photo_file = SimpleUploadedFile('test.png', photo.getvalue())
            PhotoUpload.objects.create(user=self.user, photo=photo_file)

        obj_list = PhotoUpload.objects.all()
        response = self.client.get('/photos/')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.data, PhotoUploadSerializer(obj_list, many=True).data)
        self.assertEqual(len(PhotoUploadSerializer(obj_list, many=True).data), 3)

    def test_can_upload_photo(self):
        photo = self.generate_photo_file()
        photo_file = SimpleUploadedFile('test.png', photo.getvalue())
        response = self.client.post('/photos/', {'user': self.user.pk, 'photo': photo_file})
        obj = PhotoUpload.objects.all()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(obj), 1)
        self.assertEqual(response.data['photo'], obj[0].photo.url)

    def generate_photo_file(self):
        file = BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file
