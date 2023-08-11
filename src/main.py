import json

from tools import numberGenerator, birthdateGenerator, genderGenerator, nameGenerator, surnameGenerator

def main():
    with open("config.json", "r") as config_file:
        data = json.load(config_file)
        templatesPath = data["templatesPath"]
        country = data["defaultCountry"]

    with open(f"{templatesPath}/{country}/setup.json", "r") as config_file:
        data = json.load(config_file)
        countryCode = data["countryCode"]
        phoneNumTemplate = data["phoneNumber"]
        surnamesNum = data["surnamesNum"]
        idTemplate = data["documentID"]

        files = data["files"]

    gender = genderGenerator()
    name = nameGenerator(f"{templatesPath}/{country}/{files[gender]}")
    surname = surnameGenerator(f"{templatesPath}/{country}/{files['surnames']}",surnamesNum)
    phone = numberGenerator(phoneNumTemplate, countryCode = countryCode)
    idNumber = numberGenerator(idTemplate)

    print(name)
    print(surname)
    print(phone)
    print(idNumber)

if __name__ == '__main__':
    main()

