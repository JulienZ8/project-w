import string
import random


def caesar_cipher(key: int, text: str) -> str:
    cipher = ""

    for i in text:
        # ignores all none alphabetic or ascii characters
        if not ((i.isalpha()) and i.isascii()):
            cipher = cipher + i
        else:
            # if letter is lower case
            if i.islower():
                # sum of alphabet index of text and alphabet index of key. if >26, back to 0
                new_letter = string.ascii_lowercase[(string.ascii_lowercase.index(i) + key) % 26]
                cipher = cipher + new_letter
            # if letter is upper case
            else:
                # sum of alphabet index of text and alphabet index of key. if >26, back to 0
                new_letter = string.ascii_uppercase[(string.ascii_uppercase.index(i) + key) % 26]
                cipher = cipher + new_letter

    return cipher


def caesar_decipher(cipher: str, key: int) -> str:
    decipher = ""

    for i in cipher:

        if not ((i.isalpha()) and i.isascii()):
            decipher = decipher + i
        else:
            if i.islower():
                new_letter = string.ascii_lowercase[(string.ascii_lowercase.index(i) - key) % 26]
                decipher = decipher + new_letter
            else:
                new_letter = string.ascii_uppercase[(string.ascii_uppercase.index(i) - key) % 26]
                decipher = decipher + new_letter
    # except:
    return decipher


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


def one_time_pad_decipher(text: str, mask: str):
    text = text.replace(' ', '')
    cipher = ''

    for i in range(len(text)):
        # alphabet index of text
        text_alphabet_index = (string.ascii_lowercase.index(text[i]))
        # index of text in mask
        mask_index = i % len(mask)
        # alphabet index of mask
        mask_alphabet_index = (string.ascii_lowercase.index(mask[mask_index]))
        # sum of alphabet index of text and alphabet index of mask. if >26, back to 0
        cipher_index = (text_alphabet_index + mask_alphabet_index) % 26
        cipher = cipher + string.ascii_lowercase[cipher_index]

    return cipher


def rsa():
    # Choose p and q two prime numbers
    p = prime_number_generator(n=100, first_selected=2, max_value=100)
    q = prime_number_generator(n=100, first_selected=p, max_value=100)

    # n = pq -> module de chiffrement
    n = p * q

    # phi(n)
    phi = (p - 1) * (q - 1)

    # Choix d'un nombre premier e inférieur à phi -> exposant de chiffrement
    e = prime_number_generator(n=100, first_selected=2, max_value=phi)

    # d = inverse modulaire de e -> exposant de déchiffrement
    d = phi % e

    public_key = f'{n}, {e}'

    private_key = f'{n}, {d}'

    print(public_key)
    print(private_key)

    return


def prime_number_generator(n: int, first_selected: int, max_value: int) -> int:
    """
    :param n: longueur de la liste dans laquelle chercher les nombres premiers
    :param first_selected: nombre premier p à ne pas prendre à double
    :param max_value: pour le choix de e qui doit être plus petit que phi
    :return: nombre
    """
    prime_numbers = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, num)):
            prime_numbers.append(num)

    # on enlève p
    prime_numbers.remove(first_selected)

    # on ne prend que les valeurs en dessous de max_value
    prime_numbers = [element for element in prime_numbers if element < max_value]

    # choix de l'élément
    random_number = random.choice(prime_numbers)

    return random_number
