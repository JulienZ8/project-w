import string


def caesar_cipher(key: int, text: str) -> str:
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
