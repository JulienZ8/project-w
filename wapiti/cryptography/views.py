from django.shortcuts import render

from django.http import HttpResponse
from .forms import CaesarCipherForm
import string


def index(request):
    #return HttpResponse("Hello, world. You're at the cryptography index.")
    return render(request, 'index.html')


def cipher_form(request):

    new_text = ""
    if request.method == 'POST':
        form = CaesarCipherForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key_field']
            text = form.cleaned_data['text_field']

            new_text = caesar_cipher(key=key, text=text)


    form = CaesarCipherForm()
    return render(request, 'caesar.html', {'new_text': new_text, 'form': form})


def caesar_cipher(key: int, text: str):

    new_text = ""

    for i in text:

        if not ((i.isalpha()) and i.isascii()):
            new_text = new_text + i
        else:
            if i.islower():
                new_letter = string.ascii_lowercase[(string.ascii_lowercase.index(i) + key) % 26]
                new_text = new_text + new_letter
            else:
                new_letter = string.ascii_uppercase[(string.ascii_uppercase.index(i) + key) % 26]
                new_text = new_text + new_letter
    return new_text
