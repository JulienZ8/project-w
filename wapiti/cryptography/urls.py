from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('caesar/', views.caesar_cipher_form, name='caesar'),
    path('caesar_decipher/', views.caesar_decipher_form, name='caesar_decipher'),
    path('pad/', views.one_time_pad_form, name='one_time_pad'),
    path('pad_decipher/', views.one_time_pad_decipher_form, name='one_time_pad_decipher')
]