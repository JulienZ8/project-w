from django.shortcuts import render

from django.http import HttpResponse
import string


def index(request):
    return HttpResponse("Hello, world. You're at the cryptography index.")


def caesar_cipher(request):
    key = 4
    text = 'salut'
    
    # position dans l'alphabet
    for x in text:
        print(string.ascii_lowercase.index(x) + 1)

    return render(request, 'caesar.html', {'key': key, 'text': text})
