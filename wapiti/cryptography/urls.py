from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('caesar/', views.caesar_cipher_form, name='caesar'),
    path('pad/', views.one_time_pad_form, name='one_time_pad')
]