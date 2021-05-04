from django.urls import path,include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('', views.home, name = 'home'),
    path('logout', views.logout, name = 'logout'),
]
