from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the cryptography index.")


def caesar_cipher(request):
    key = 4
    text = 'salut'
    return render(request, 'caesar.html', {'key': key, 'text': text})
