## Dies ist ein kleines Cheat Sheet fuer die 
## Verwendung von Python fuer C und C++ Programmierer

# Variable

# int eineZahl = 43;

eineVariable = 13
print("eineVariable:" , eineVariable)
eineVariable = "blablabla"
print("eineVariable:", eineVariable)

# Typisierung in Python: Duchtyping

# Daher: bitte immer nach Moeglichkeit typisieren:
eineZweiteVariable : int = 14
print("eineZwiteVariable:", eineZweiteVariable**3)
eineZweiteVariable = "TEXT"
# print("ZweiteVariable:", eineZweiteVariable**3)
# erzeugt leider erst zur fehler zur Laufzeit

dateinTyp = type(eineVariable)
print("Datentyp von eineVariable:", dateinTyp)
eineVariable = 15

dateinTyp = type(eineVariable)
print("Datentyp von eineVariable:", dateinTyp)

# Formatierte Ausgabe
# C:. printf("Zahl lautet %i und ist Cool!", eineVariable);
# print("Zahl lautet %i und ist Cool!", eineVariable)
einText = f"Zahl lautet {eineVariable} \n und ist Cool!"
# Typ Umwandeln
# (Type-Conversion)
einString = str((eineVariable**2)) # Wandle Zahl in Text um

# Korrigiert: str() hinzugefügt, da man int nicht direkt mit + verketten kann
alternativText = "Zahl lautet " + str(eineVariable) + "\n und ist Cool..!"

print(einText)
print("Alternative Text: ", alternativText)

# Eingaben von der Kommonadozeile
# int i=0;
#  printf("Bitte zahl eingaben:\n")
#  scanf(&i);

eingeleseneZahl = int(input("Bitte Zahl eingeben:"))
print("Zahl eingelesen vom Typ", type(eingeleseneZahl))

# FUnktionen
#int main(void) {
 #   printf("HAllo Funktion!"):
#}
 
def main():{
    print("Hallo Main!")
}
 
main()
 