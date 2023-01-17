from django.shortcuts import render

#from django.http import HttpResponse
from .forms import CaesarCipherForm, OneTimePadForm
from . import cipher_algorithms as ca


def index(request):
    # return HttpResponse("Hello, world. You're at the cryptography index.")
    return render(request, 'index.html')


def caesar_cipher_form(request):

    new_text = ""
    if request.method == 'POST':
        form = CaesarCipherForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key_field']
            text = form.cleaned_data['text_field']

            new_text = ca.caesar_cipher(key=key, text=text)

    form = CaesarCipherForm()  # to check if necessary
    return render(request, 'caesar.html', {'new_text': new_text, 'form': form})


def one_time_pad_form(request):

    new_text = ''
    if request.method == 'POST':
        form = OneTimePadForm(request.POST)
        if form.is_valid():
            mask = form.cleaned_data['mask_field']
            text = form.cleaned_data['text_field']

            new_text = ca.one_time_pad(mask=mask, text=text)

    form = OneTimePadForm()  # to check if necessary
    return render(request, 'pad.html', {'new_text': new_text, 'form': form})
