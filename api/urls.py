from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^artboard$', views.get_image),
    url(r'^artboard/(?P<artboard_id>\d+)$', views.image_detail),
    url(r'^upload/s3$', views.upload_s3),
]
