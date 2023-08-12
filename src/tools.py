import random
from datetime import date

from utils import generateDigit, getRandomValue, listsFromCsv, getRandomRecordFromCsv

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

def nameGenerator(maleNames, femaleNames, gender):
    
    return getRandomValue(maleNames) if gender == "male" else getRandomValue(femaleNames)


def surnameGenerator(surnamesList,num):
    res = ""
    numSurnames = generateDigit(num["min"], num["max"])
    long = len(surnamesList) - 1
    
    for i in range(numSurnames):
        st = surnamesList[generateDigit(max = long)]
        res = res + st + " "

    return res.rstrip()

def birthdateGenerator(initYear = 1940,lastYear = 2015):
    init = date(initYear, 1, 1)
    final =  date(lastYear, 12, 31)

    random_date = init + (final - init) * random.random()
    
    return random_date.isoformat()


def genderGenerator():
    return "male" if random.random() > 0.5 else "female"

def addressGenerator(streetList, location):
    street = getRandomValue(streetList)

def locationGenerator(df):
    locationDict = getRandomRecordFromCsv(df)
    return locationDict.values()

