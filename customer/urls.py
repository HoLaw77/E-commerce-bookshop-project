from django.urls import path
from . import views
from .views import show_profile

urlpatterns = [
    path('profile', views.show_profile, name='profile'),
    path('test', views.test, name='test'),
]