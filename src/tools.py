import random
from datetime import datetime

from services import generateDigit, listFromCsv

def numberGenerator( defNumber, countryCode = False):

    template = defNumber["template"]
    symbols = defNumber["symbols"]

    res = ""

    if countryCode:
        res = "+%s "%(countryCode)

    for d in template:

        if not d in symbols:
            res += d
        else:
            if symbols[d]["isDigit"]:
                res += str(generateDigit(min = symbols[d]["min"],max = symbols[d]["max"]))
            else:
                long = len(symbols[d]["characters"]) - 1
                res += symbols[d]["characters"][generateDigit(max = long)]

    return res

def nameGenerator(file):
    namesList = listFromCsv(file)
    long = len(namesList) - 1
    return (namesList[generateDigit(max = long)])

def surnameGenerator(file,num):
    res = ""
    numSurnames = generateDigit(num["min"], num["max"])
    surnamesList = listFromCsv(file)
    long = len(surnamesList) - 1
    
    for i in range(numSurnames):
        st = surnamesList[generateDigit(max = long)]
        res = res + st + " "

    return res.rstrip()

def birthdateGenerator():
    inicio = datetime(2017, 1, 30)
    final =  datetime(2017, 5, 28)

    random_date = inicio + (final - inicio) * random.random()

def genderGenerator():
    return "male" if random.random() > 0.5 else "female"