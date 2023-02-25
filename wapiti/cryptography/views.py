from django.shortcuts import render

# from django.http import HttpResponse
from .forms import CaesarCipherForm, CaesarDecipherForm, OneTimePadForm, OneTimePadDecipherForm, RsaForm, \
    DecipherRsaForm
from . import cipher_algorithms as ca


def index(request):
    # return HttpResponse("Hello, world. You're at the cryptography index.")
    return render(request, 'index.html')


def caesar_cipher_form(request):
    new_text = ''
    key = ''
    if request.method == 'POST':
        form = CaesarCipherForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key_field']
            text = form.cleaned_data['text_field']

            new_text = ca.caesar_cipher(key=key, text=text)

    form = CaesarCipherForm()  # to check if necessary
    return render(request, 'cipher/caesar.html', {'new_text': new_text, 'form': form, 'key': key})


def caesar_decipher_form(request):
    new_text = ''
    key = ''
    if request.method == 'POST':
        form = CaesarDecipherForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text_field']
            key = form.cleaned_data['key_field']

            new_text = ca.caesar_decipher(cipher=text, key=key)

    form = CaesarDecipherForm()  # to check if necessary
    return render(request, 'cipher/caesar_decipher.html', {'new_text': new_text, 'form': form, 'key': key})


def one_time_pad_form(request):
    new_text = ''
    mask = ''
    if request.method == 'POST':
        form = OneTimePadForm(request.POST)
        if form.is_valid():
            mask = form.cleaned_data['mask_field']
            text = form.cleaned_data['text_field']

            new_text = ca.one_time_pad(mask=mask, text=text)

    form = OneTimePadForm()  # to check if necessary
    return render(request, 'cipher/pad.html', {'new_text': new_text, 'form': form, 'mask': mask})


def one_time_pad_decipher_form(request):
    new_text = ''
    mask = ''
    if request.method == 'POST':
        form = OneTimePadDecipherForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text_field']
            mask = form.cleaned_data['mask_field']

            new_text = ca.one_time_pad_decipher(mask=mask, text=text)

    form = OneTimePadDecipherForm()  # to check if necessary
    return render(request, 'cipher/pad_decipher.html', {'new_text': new_text, 'form': form, 'mask': mask})


def rsa_cipher_form(request):
    ciphered_message = ''
    public_key = ''
    private_key = ''

    if request.method == 'POST':
        form = RsaForm(request.POST)
        if form.is_valid():
            text_field = form.cleaned_data['text_field']

            public_key, private_key, ciphered_message = ca.rsa_cipher(1000, text_field)

    form = RsaForm()  # to check if necessary
    return render(request, 'cipher/rsa_cipher.html', {'ciphered_message': ciphered_message, 'form': form,
                                                      'public_key': public_key, 'private_key': private_key})


def rsa_decipher_form(request):
    deciphered_message = ''

    if request.method == 'POST':
        form = DecipherRsaForm(request.POST)
        if form.is_valid():
            ciphered_message = form.cleaned_data['text_field']
            private_key = form.cleaned_data['private_key_field']

            # cast private_key
            for character in '()':
                private_key = private_key.replace(character, '')
            split = private_key.split(',')
            cast_int = [int(i) for i in split]
            private_key = tuple(cast_int)

            deciphered_message = ca.rsa_decipher(private_key=private_key, encripted_message=ciphered_message)

    form = DecipherRsaForm()
    return render(request, 'cipher/rsa_decipher.html', {'deciphered_message': deciphered_message, 'form': form})
