from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('caesar/', views.cipher_form, name='caesar')
]