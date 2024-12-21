import csv

def getCSVData(filneName):
    rows = []
    dataFile = open(filneName, "r")
    reader = csv.reader(dataFile)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows


