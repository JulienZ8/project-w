import datetime
import random


def division(nominator: int, denominator: int) -> float:
    try:
        result = nominator / denominator
    except ZeroDivisionError:
        print('La division par zéro n''est pas possible')
    except Exception as e:
        f = open('errormessage.txt', 'a')
        date_time = datetime.datetime.now()
        f.write(
            f'\n date and time: {date_time} \n Error message: \n {e} \n nominator: {nominator}, denominator: {denominator} \n')
        f.close()
    else:
        return result


def rsa_key_generator(max_value: int):
    """
    Algorithme chiffrement RSA
    :param max_value: longueur de la liste dans laquelle chercher les nombres premiers
    :return: clé public et clé privé
    """
    # Choose p and q two prime numbers
    p = prime_number_generator(n=max_value, first_selected=127, max_value=max_value)
    q = prime_number_generator(n=max_value, first_selected=p, max_value=max_value)

    # n = pq -> module de chiffrement
    n = p * q

    # phi(n)
    phi = (p - 1) * (q - 1)

    # Choix d'un nombre premier e inférieur à phi -> exposant de chiffrement
    e = prime_number_generator(n=max_value, first_selected=127, max_value=phi)

    # d = inverse modulaire de e pour la multiplication modulo phi -> exposant de déchiffrement
    gcd, x, y = euclide_extended(e, phi)
    d = x

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


def prime_number_generator(n: int, first_selected: int, max_value: int) -> int:
    """
    :param n: longueur de la liste dans laquelle chercher les nombres premiers
    :param first_selected: nombre premier p à ne pas prendre à double
    :param max_value: pour le choix de e qui doit être plus petit que phi
    :return: nombre
    """
    prime_numbers = []
    for num in range(125, n + 1):
        if all(num % i != 0 for i in range(2, num)):
            prime_numbers.append(num)

    # on enlève p
    prime_numbers.remove(first_selected)

    # on ne prend que les valeurs en dessous de max_value
    prime_numbers = [element for element in prime_numbers if element < max_value]

    # choix de l'élément
    random_number = random.choice(prime_numbers)

    return random_number


def euclide_extended(a, b):
    """
    Algorithme d'Euclide étendu pour trouver l'inverse modulaire
    :param a: exposant de chiffrement e
    :param b: phi
    :return: x inverse of a modulob, y inverse of b modulo a
    """
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = euclide_extended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def rsa_cipher(max_value: int, clear_message: str):
    encripted_message = ''
    private_key = (-1, -1)
    public_key = (-1, -1)

    while private_key[0] < 2:  # TODO voir pourquoi négatif ou egale à 1
        public_key, private_key = rsa_key_generator(max_value)

    for char in clear_message:
        encripted_char = f'{ord(char) ** public_key[0] % public_key[1]}-'
        encripted_message = encripted_message + encripted_char

    return public_key, private_key, encripted_message[0:-1]


def rsa_decipher(private_key, encripted_message: str):
    clear_message = ''
    clear_message_splited = encripted_message.split('-')
    for char in clear_message_splited:
        clear_char_number = int(char) ** private_key[0] % private_key[1]
        clear_char = chr(clear_char_number)
        clear_message = clear_message + clear_char

    return clear_message


decipher = 'hello ski'
i = 0
while decipher == 'hello ski':
    public_key, private_key, message = rsa_cipher(1000, 'hello ski')
    decipher = rsa_decipher(private_key=private_key, encripted_message=message)
    i += 1
    print(f'{i}-{decipher}')
