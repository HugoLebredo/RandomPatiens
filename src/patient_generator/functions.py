import json
import random

from datetime import date
from pathlib import Path

from .utils import generateDigit, getRandomValue, getRandomRecordFromCsv, listsFromCsv, loadDataframe

def loadData(path,files, colnames):
    res = {}

    namesDic = listsFromCsv(f"{path}/{files['names']}", colnames["names"])
    streetsDic = listsFromCsv(f"{path}/{files['streets']}", colnames["streets"])
    
    res.update(namesDic)
    res.update(streetsDic)

    return res

def loadConfig(base_path):
    with open(f"{base_path}/config.json", "r") as config_file:
        configData = json.load(config_file)
        return configData

def loadSetup(path):
    with open(f"{path}/setup.json", "r") as setup_file:
        setupData = json.load(setup_file)
        return setupData

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

def locationGenerator(df):
    locationDict = getRandomRecordFromCsv(df)
    return locationDict

def addressGenerator(locations, streets):
    address = locationGenerator(locations)
    place = f"{getRandomValue(streets)} {generateDigit(1,99)}"
    address.update({"place":place})
    return address

def patientGenerator(data,locationsDf,surnamesNum,phoneNumTemplate,idTemplate,countryCode):
    patient = {}
    
    patient.update({"gender": genderGenerator()})
    patient.update({"name":nameGenerator(data["maleNames"],data["femaleNames"],patient["gender"])})
    patient.update({"surname":surnameGenerator(data["surnames"], surnamesNum)})
    patient.update({"phone":numberGenerator(phoneNumTemplate, countryCode = countryCode)})
    patient.update({"idNumber":numberGenerator(idTemplate)})
    patient.update({"birthday":birthdateGenerator()})
    patient.update({"birthday":addressGenerator(locationsDf, data["streets"])})
    print(patient)
    return patient

def createPartients(numberPatiens = 10, defCountry = False):
    base_path = Path(__file__).parent
    # Cargar archivos de configuración
    config = loadConfig(base_path)

    country = defCountry if defCountry != False else config["defaultCountry"]

    path = f"{base_path}/{config['templatesPath']}/{country}"

    setup = loadSetup(path)

    # Cargar datos
    data = loadData(path,setup["files"], config["colnames"])
    locationsDf = loadDataframe(path,setup["files"]["locations"], config["colnames"])

    patients = []
    for i in range(numberPatiens):
       newPatient = patientGenerator(data,locationsDf,setup["surnamesNum"],setup["phoneNumber"],setup["documentID"],setup["countryCode"])
       patients.append(newPatient)
    return patients
