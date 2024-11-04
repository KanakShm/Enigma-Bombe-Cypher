import Enigma

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
           "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
           "U", "V", "W", "X", "Y", "Z"]

rotor = "ACYKROZQUWLBIGSNPTDJFVHEXM"

def getRotorConfig():
    wiring = []
    for i, val in enumerate(rotor):
        pair = [i, letters.index(rotor[i])]
        wiring.append(pair)
    return wiring