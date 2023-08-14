from pandas import read_csv
import random

def generateDigit(min=0,max=9):
    res = random.randint(min,max)
    return res

def getRandomValue(list):
    long = len(list) - 1
    return (list[generateDigit(max = long)])

def fromDftoDic(df):
    res = {}
    headers = df.columns

    for col in headers:
        list = df[col].dropna().tolist()
        res.update({col:list})
    
    return res

def listsFromCsv(file, colnames):
    df = read_csv(file, sep=";", encoding="utf-8-sig", skiprows=[0,], names = colnames)
    return fromDftoDic(df)


def getRandomRecordFromCsv(df):
    dict = df.sample().to_dict(orient='records')[0]
    return dict

def loadDataframe(path,file, colnames):
    return read_csv(f"{path}/{file}", sep=";", encoding="utf-8-sig", skiprows=[0,], names = colnames["locations"])
