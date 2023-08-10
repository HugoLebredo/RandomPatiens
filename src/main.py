import json
import csv

from tools import phoneNumberGenerator, birthdateGenerator, genderGenerator

def main():
    with open("config.json", "r") as config_file:
        data = json.load(config_file)
        templatesPath = data["templatesPath"]
        country = data["defaultCountry"]

    with open(f"{templatesPath}/{country}/setup.json", "r") as config_file:
        data = json.load(config_file)
        countryCode = data["countryCode"]
        defNumber = data['defNumber']

    genderGenerator()
    phoneNumberGenerator(countryCode,defNumber)
    birthdateGenerator()

if __name__ == '__main__':
    main()

