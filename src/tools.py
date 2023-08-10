import random
from datetime import datetime

def generatePhoneNumber(template = "+34619-000.000."):
    print(template)

def generateBirthdate():
    inicio = datetime(2017, 1, 30)
    final =  datetime(2017, 5, 28)

    random_date = inicio + (final - inicio) * random.random()

    print(random_date)