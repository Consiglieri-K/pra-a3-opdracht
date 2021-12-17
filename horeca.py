import csv
import os
from datetime import datetime

horecaFile = open("GH.csv", "r", encoding = "UTF-8")
reader = csv.DictReader(horecaFile, delimiter=";")
horecaList = list(reader)
outFile = open("outFile.txt", "a")


#NIGHTVALUE 
nightValue = 0
isRunning = True
while isRunning:

    print("1. Bereken het gemiddeld aantal bezoekers binnen.")
    print("2. Bereken alle horeca ondernemingen met meer dan 50 plekken op het terras.")
    print("3. Bereken de hoeveelheid horecaondernemingen met een nachtvergunning.")
    print("4. Maak een top-10 lijst van de oudste horecaondernemingen met vergunningen. ")
    print("\n Druk op X om te stoppen")
    
    choice = input("\n Maak uw keuze:")
    os.system("cls")

    if choice == "1":
        totalValue = 0
        for inside in horecaList:
            totalValue += float(inside['cap_max_intern'])
        print("-------------------------------------- \n")
        outFile.write("-------------------------------------- \n")
        print(f"Totaal aantal bezoekers is: {totalValue} \n")
        outFile.write(f"Totaal aantal bezoekers is: {totalValue} \n")
        

    elif choice == "2":

        print("Aantal horecaondernemingen met meer dan 50 plekken op hun terras: ")
        terras_horeca = 0
        for onderneming in horecaList:
            if int(onderneming['cap_max_terras']) > 50:
                terras_horeca += 1
        os.system("cls")
        print("-------------------------------------- \n")
        outFile.write("-------------------------------------- \n")
        print(f"Aantal horecaondernemingen met meer dan 50 mensen = {terras_horeca} \n")
        outFile.write(f"Aantal horecaondernemingen met meer dan 50 mensen = {terras_horeca} \n")
        

    elif choice == "3":
        for nightLicense in horecaList:
            if nightLicense["nachtvergunning"] == "Ja":
                nightValue += 1
        print("-------------------------------------- \n")
        outFile.write("-------------------------------------- \n")
        print(f"Totaal aantal horeca met een nachtvergunning: {nightValue} \n")    
        outFile.write(f"Totaal aantal horeca met een nachtvergunning: {nightValue} \n")  
       

    
    elif choice == "4":
        top10 = []
        i = 0
        timestamps = []
        list = ""

        for i in horecaList:
            timestamps.append(i["datumEersteAanvraag"])
        
        dates = [datetime.strptime(ts, "%d-%m-%Y") for ts in timestamps]
        dates.sort()
        sorteddates = [datetime.strftime(ts, "%d-%m-%Y") for ts in dates]
        for x in range(10):
            list += f"{sorteddates[x]}\n"
            os.system("cls")
        print("-------------------------------------- \n")
        outFile.write("-------------------------------------- \n")
        print(f"Top 10 oudste vergunningen: \n {list}")
        outFile.write(f"Top 10 oudste vergunningen: \n {list}")
        print("-------------------------------------- \n")
        outFile.write("-------------------------------------- \n")
        
    elif choice.upper() == "X":
        isRunning = False
    

horecaFile.close()
outFile.close()

            

    

    

