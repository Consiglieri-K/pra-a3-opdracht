import csv
import os

horecaFile = open("GH.csv", "r", encoding = "UTF-8")
reader = csv.DictReader(horecaFile)
horecaList = list(reader)

