from django.shortcuts import render

from django.http import HttpResponse
from .forms import CaesarCipherForm
import string


def index(request):
    # return HttpResponse("Hello, world. You're at the cryptography index.")
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

    #try:
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
    #except:
    return new_text


def one_time_pad(mask: str, text: str) -> str:

    # supression des espaces
    text = text.replace(' ', '')
    # suppression des majuscules
    text = text.lower()
    alphabets = list(string.ascii_lowercase)
    mask_length = len(mask)
    cipher_text = ''

    for i in range(len(text)):
        # place de l'index du texte dans l'alphabet
        text_alphabet_index = alphabets.index(text[i])
        # place de l'index dans le text
        text_index = i
        # place de l'index dans le mask
        mask_index = text_index % mask_length
        # place du mask dans l'alphabet
        mask_alphabet_index = alphabets.index(mask[mask_index])
        # place du message codé dans l'alphabet
        cipher_index = (mask_alphabet_index + text_alphabet_index) % 26
        # lettre codée
        cipher_char = alphabets[cipher_index]
        # message codé
        cipher_text = cipher_text + cipher_char
        
    return cipher_text
