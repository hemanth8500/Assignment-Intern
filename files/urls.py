from django.urls import path,include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.upload, name = 'upload'),
]
