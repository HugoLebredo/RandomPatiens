import json
from pandas import read_csv
from tools import numberGenerator, birthdateGenerator, genderGenerator, nameGenerator, surnameGenerator, locationGenerator
from utils import listsFromCsv

def loadData(path,files, colnames):
    res = {}

    namesDic = listsFromCsv(f"{path}/{files['names']}", colnames["names"])
    streetsDic = listsFromCsv(f"{path}/{files['streets']}", colnames["streets"])
    
    res.update(namesDic)
    res.update(streetsDic)

    return res

def loadDataframe(path,file, colnames):
    return read_csv(f"{path}/{file}", sep=";", encoding="utf-8-sig", skiprows=[0,], names = colnames["locations"])

def main():
    with open("config.json", "r") as config_file:
        configData = json.load(config_file)
        templatesPath = configData["templatesPath"]
        country = configData["defaultCountry"]
        colnames = configData["colnames"]

        path = f"{templatesPath}/{country}"

    with open(f"{path}/setup.json", "r") as setup_file:
        setupData = json.load(setup_file)
        countryCode = setupData["countryCode"]
        phoneNumTemplate = setupData["phoneNumber"]
        surnamesNum = setupData["surnamesNum"]
        idTemplate = setupData["documentID"]
        files = setupData["files"]

# Cargar datos
    data = loadData(path,files, colnames)
    locationsDf = loadDataframe(path,files["locations"], colnames)

# Generar pacientes
    gender = genderGenerator()
    name = nameGenerator(data["maleNames"],data["femaleNames"],gender)
    surname = surnameGenerator(data["surnames"], surnamesNum)
    phone = numberGenerator(phoneNumTemplate, countryCode = countryCode)
    idNumber = numberGenerator(idTemplate)
    birthday = birthdateGenerator()
    region, town, postalCode = locationGenerator(locationsDf)
   # address = addressGenerator()
    print(region, town, postalCode)
if __name__ == '__main__':
    main()

