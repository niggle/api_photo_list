from django.conf.urls import url

from photos.views import PhotoUploadListCreate

urlpatterns = [
    url(r'^', PhotoUploadListCreate.as_view()),
]