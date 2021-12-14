import csv
import os

horecaFile = open("GH.csv", "r", encoding = "UTF-8")
reader = csv.DictReader(horecaFile)
horecaList = list(reader)

isRunning = True
while isRunning:
    os.system("cls")
    print("1. Bereken het gemiddeld aantal bezoekers binnen.")
    print("2. Bereken alle horeca ondernemingen met meer dan 50 plekken op het terras.")
    print("3. Bereken de hoeveelheid horecaondernemingen met een nachtvergunning.")
    print("4. Maak een top-10 lijst van de oudste horecaondernemingen met vergunningen. ")
    print("\nDruk op X om te stoppen")
    
    choice = input("\n Maak uw keuze:")
    os.system("cls")
    if choice == "1":
        print(f"test")
    elif choice == "2":
        print(f"test2")
    elif choice == "3":   
        print(f"test3")
    elif choice == "4":
        print(f"test4")

