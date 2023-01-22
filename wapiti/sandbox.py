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





rsa()





