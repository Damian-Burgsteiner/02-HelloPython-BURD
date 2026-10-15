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