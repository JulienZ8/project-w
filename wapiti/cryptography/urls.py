from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('caesar/', views.caesar_cipher, name='caesar')
]