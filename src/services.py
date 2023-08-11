from pandas import read_csv
import random

def generateDigit(min=0,max=9):
    res = random.randint(min,max)
    return res

def listFromCsv(file):
    with open(file, newline='', encoding="utf-8-sig") as f:
        data = read_csv(f)
        header = data.columns[0]
        return data[header].tolist()

