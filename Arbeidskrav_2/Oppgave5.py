import numpy as np


def beregn_areal_figur(diameter, b):
    areal_halvsirkel = np.pi * (diameter/2)**2 / 2
    areal_trekant = diameter * b / 2
    areal_figur = areal_halvsirkel + areal_trekant
    return areal_figur


def beregn_omkrets_figur(diameter, b):
    omkrets_halvsirkel = np.pi * diameter / 2
    langside_trekant = np.sqrt(diameter**2 + b**2)
    omkrets_figur = omkrets_halvsirkel + langside_trekant + b
    return omkrets_figur


a = float(input("Skriv innn et tall a: "))
b = float(input("Skriv inn et tall b: "))

areal_figur = beregn_areal_figur(a, b)

omkrets_figur = beregn_omkrets_figur(a, b)

print("")       # Bare for å få litt luft i terminalen
print(f'Areal av figuren: {areal_figur:.2f}')
print(f'Omkrets av figuren: {omkrets_figur:.2f}')
