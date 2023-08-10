from datetime import datetime
import random

def phoneNumberGenerator(countryCode, defNumber):

    template = defNumber["template"]
    symbols = defNumber["symbols"]

    result = "+%s "%(countryCode)

    for d in template:
        res = d if not d in symbols else generateDigit(symbols[d]["min"],symbols[d]["max"])
        result += res

    print(result)

def generateDigit(min=0,max=9):
    res = random.randint(min,max)
    return str(res)


def birthdateGenerator():
    inicio = datetime(2017, 1, 30)
    final =  datetime(2017, 5, 28)

    random_date = inicio + (final - inicio) * random.random()

def genderGenerator():
    return "male" if random.random() > 0.5 else "female"