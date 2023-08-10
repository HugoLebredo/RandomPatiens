import random
import csv

from tools import generatePhoneNumber, generateBirthdate

gender = "male" if random.random() > 0.5 else "female"

def main():
    print(gender)
    generatePhoneNumber()
    generateBirthdate()

if __name__ == '__main__':
    main()

