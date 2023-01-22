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


# result = division(12, 0)

# print(result)


def rsa():
    # Choose p and q two prime numbers
    p = prime_number_generator(n=12, first_selected=2, max_value=100)
    print(f'p = {p}')
    q = prime_number_generator(n=12, first_selected=p, max_value=100)
    print(f'q = {q}')
    # n = pq -> module de chiffrement
    n = p * q
    print(f'n = {n}')
    # phi(n)
    phi = (p - 1) * (q - 1)
    print(f'phi = {phi}')
    # Choix d'un nombre premier e inférieur à phi -> exposant de chiffrement
    e = prime_number_generator(n=100, first_selected=2, max_value=phi)
    print(f'e = {e}')
    # d = inverse modulaire de e -> exposant de déchiffrement
    d = phi % e
    print(f'd = {d}')
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


rsa()
