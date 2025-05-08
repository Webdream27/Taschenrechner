"""************************************************
Einsendeaufgabe 3.4
***********************************************"""

# Rechensymbole
# 1 = Addition
# 2 = Subtraktion
# 3 = Multiplikation
# 4 = Division



# Auswahl Liste Rechenoptionen
print("Auswahl der Rechenoptionen:")
print("Bitte geben Sie eine Zahl der gewünschten Rechenoption ein!")
print("Sie haben die Wahl von Zahl 1 bis Zahl 4.")
print("Die Zahl 1 steht für Addition.")
print("Die Zahl 2 steht für Subtraktion.")
print("Die Zahl 3 steht für Multiplikation.")
print("Die Zahl 4 steht für Division.")


rechenoption = float(input("Geben Sie eine Zahl zwischen 1 bis 4 ein:"))


#Berechnung der Rechenoptionen
if rechenoption == 1:
    print("Die Berechnung für die Addition ist bereit.")
elif rechenoption == 2:
    print("Die Berechnung für die Subtraktion ist bereit.")
elif rechenoption == 3:
    print("Die Berechnung für die Multiplikation ist bereit.")
elif rechenoption == 4:
    print("Die Berechnung für die Division ist bereit.")
else:
    print("Dies ist eine ungültige Auswahl. Bitte geben Sie 1,2,3 oder 4 ein.")


zahl1 = float(input("Geben Sie die erste Zahl für die Berechnung ein:"))
zahl2 = float(input("Geben Sie die zweite Zahl für die Berechnung ein:"))





# Die Funktion Addition
def addition():
    ausgabe = zahl1 + zahl2
    print("Das Ergebnis der Addition ist", ausgabe)




# Die Funktion Subtraktion
def subtraktion():
    ausgabe = zahl1 - zahl2
    print("Das Ergebnis der Subtraktion ist", ausgabe)




# Die Funktion Multiplikation
def multiplikation():
    ausgabe = zahl1 * zahl2
    print("Das Ergebnis der Multiplikation ist", ausgabe)




# Die Funktion Division
def division():
    ausgabe = zahl1 / zahl2
    print("Das Ergebnis der Division ist", ausgabe)



# Zuweisug der Rechenoptionen
if(rechenoption  == 1 ):
    addition()
elif(rechenoption == 2):
    subtraktion()
elif(rechenoption == 3):
    multiplikation()
elif(rechenoption == 4):
    division()
else:
    print("Die Eingabe ist nicht korrekt, da eine falsche Eingabe bei der Rechenoption gemacht wurde!")



