import csv
import os

horecaFile = open("GH.csv", "r", encoding = "UTF-8")
reader = csv.DictReader(horecaFile, delimiter=";")
horecaList = list(reader)

#TOTALVALUE
totalValue = 0
#NIGHTVALUE 
nightValue = 0
isRunning = True
while isRunning:


    print("1. Bereken het gemiddeld aantal bezoekers binnen.")
    print("2. Bereken alle horeca ondernemingen met meer dan 50 plekken op het terras.")
    print("3. Bereken de hoeveelheid horecaondernemingen met een nachtvergunning.")
    print("4. Maak een top-10 lijst van de oudste horecaondernemingen met vergunningen. ")
    print("\n Druk op X om te stoppen")
    
    choice = int(input("\n Maak uw keuze:"))
    os.system("cls")

    if choice == 1:
        for inside in horecaList:
            totalValue += float(inside['cap_max_intern'])
        print(f"Totaal aantal bezoekers is: {totalValue} \n")
        break
    elif choice == 2:
        print('Jalajajbfsjaflasfnaskjfnlafna')

    elif choice == 2:

        print("Aantal horecaondernemingen met meer dan 50 plekken op hun terras: ")
        terras_horeca = 0
        for onderneming in horecaList:
            if int(onderneming['cap_max_terras']) > 50:
                terras_horeca += 1
        os.system("cls")
        print(f"Aantal horecaondernemingen met meer dan 50 mensen = {terras_horeca}")
        break

    elif choice == 3:
        for nightLicense in horecaList:
            if nightLicense["nachtvergunning"] == "Ja":
                nightValue += 1
        print(f"Totaal aantal horeca met een nachtvergunning: {nightValue}")       
        break

    
            

    

    

