
import sys, os
sys.path.append(os.path.abspath(".."))

import Enigma
import itertools
import datetime
import time

class Bombe:

    alphabet = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]

    def __init__(self, cypherText, plainText):        
        self.cypherText = cypherText
        self.plainText = plainText
        self.counter = 0

    def iterateRotor(self):
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    print("(", i, ") (", j,  ") (", k, ")")
                    time.sleep(2.7)
                    enigma1 = Enigma.Enigma(k, j, i, self.plugBoardWiring)
                    count = 0
                    while True:
                        if enigma1.encrypt(self.plainText[count]) == self.cypherText[count]:
                            if count >= (len(self.plainText)-1): return [i, j, k]
                            count += 1
                            continue
                        else:
                            break
        return -1

    def iteratePlugboard(self):
        choose10 = list(itertools.combinations(self.alphabet, 20))
        for lst in choose10:
            for x in self.all_pairs(list(lst)):
                self.plugBoardWiring = x
                self.iterateRotor()

                self.counter += (26*26*26)
                isPlugCorrect = self.iterateRotor()

                if isPlugCorrect != -1:
                    return [isPlugCorrect, self.plugBoardWiring]

    def all_pairs(self, lst):
        if len(lst) < 2:
            yield lst
            return
        a = lst[0]
        for i in range(1,len(lst)):
            pair = [a,lst[i]]
            for rest in self.all_pairs(lst[1:i]+lst[i+1:]):
                yield [pair] + rest


bombe1 = Bombe("WETTERBERICHT", "ODHCOKPPIVESP")

print("Enigma Settings are : " + str(bombe1.iteratePlugboard()))


# import Enigma
# import time
# import copy
# import itertools

# letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
#            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
#            "U", "V", "W", "X", "Y", "Z"]

# wiring = [
#         # Rotor 1 TCIXAGDHRZLVPKEMSNQFBWYJOU
#         [[0, 19], [1, 2], [2, 8], [3, 23], [4, 0], [5, 6], [6, 3], [7, 7],
#         [8, 17], [9, 25], [10, 11], [11, 21], [12, 15], [13, 10], [14, 4],
#         [15, 12], [16, 18], [17, 13], [18, 16], [19, 5], [20, 1], [21, 22],
#         [22, 24], [23, 9], [24, 14], [25, 20]],
        
#         # Rotor 2 KJTDLXWFPIMYSOUHEVCRBAQGZN
#         [[0, 10], [1, 9], [2, 19], [3, 3], [4, 11], [5, 23], [6, 22], [7, 5],
#         [8, 15], [9, 8], [10, 12], [11, 24], [12, 18], [13, 14], [14, 20],
#         [15, 7], [16, 4], [17, 21], [18, 2], [19, 17], [20, 1], [21, 0],
#         [22, 16], [23, 6], [24, 25], [25, 13]],
        
#         # Rotor 3 ACYKROZQUWLBIGSNPTDJFVHEXM
#         [[0, 0], [1, 2], [2, 24], [3, 10], [4, 17], [5, 14], [6, 25], [7, 16],
#         [8, 20], [9, 22], [10, 11], [11, 1], [12, 8], [13, 6], [14, 18],
#         [15, 13], [16, 15], [17, 19], [18, 3], [19, 9], [20, 5], [21, 21], 
#         [22, 7], [23, 4], [24, 23], [25, 12]]
#         ]

# reflector = ["E", "S", "O", "V", "P", "Z", "J", "A", "Y", "Q",
#              "U", "I", "R", "H", "X", "L", "N", "F", "T", "G",
#              "K", "D", "C", "M", "W", "B"]

# class Bombe:
#     def __init__(self, plainText, cypherText):
#         self.plainText = plainText.upper()
#         self.cypherText = cypherText.upper()
        
#         self.__rotor1 = 0
#         self.__rotor2 = 0
#         self.__rotor3 = 0
        
#         self.__rotorPositions = wiring
#         self.__letterMappings = self.__get_mappings_by_most_common_letters()
#         self.counter = 0
        
#     def __moveRotor(self, wiringStart, n):
#         wiringCopy = copy.deepcopy(wiringStart)
#         for i in range (n):
#             # Move the first rotor one place
#             wiringCopy[0] = wiringCopy[0][-1:] + wiringCopy[0][:-1]
#             self.__rotor1 += 1
            
#             # If the first rotor completes a revolution move the second rotor one place
#             if wiringCopy[0] == wiring[0]:
#                 wiringCopy[1] = wiringCopy[1][-1:] + wiringCopy[1][:-1]
#                 self.__rotor1 = 0
#                 self.__rotor2 += 1
                
#                 # If the second rotor completes a revolution move the third rotor one place
#                 if wiringCopy[1] == wiring[1]:
#                     wiringCopy[2] = wiringCopy[2][-1:] + wiringCopy[2][:-1]
#                     self.__rotor2 = 0
#                     self.__rotor3 += 1
                    
#                     # If the third rotor completes a revolution reset all rotors
#                     if wiringCopy[2] == wiring[2]:
#                         wiringCopy[0] = copy.deepcopy(wiring[0])
#                         wiringCopy[1] = copy.deepcopy(wiring[1])
#                         wiringCopy[2] = copy.deepcopy(wiring[2])
#                         self.__rotor3 = 0
#         return wiringCopy
    
#     def __get_mappings_by_most_common_letters(self):
#         # Ensure both strings are of the same length
#         if len(self.cypherText) != len(self.plainText):
#             print("Strings must be of the same length.")
        
#         # Manually count frequency of each character in both strings
#         frequency = {}
#         for char in self.cypherText + self.plainText:
#             if char in letters:
#                 continue
#             if char in frequency:
#                 frequency[char] += 1
#             else:
#                 frequency[char] = 1

#         # Collect mappings with their indices
#         mappings = [
#             {
#                 'char1': char1,
#                 'char2': char2,
#                 'index': index,
#                 'frequency': frequency[char1] + frequency[char2]
#             }
#             for index, (char1, char2) in enumerate(zip(self.cypherText, self.plainText))
#             if char1 in letters and char2 in letters
#         ]
        
#         # Sort mappings by the frequency of the most common character in each pair
#         mappings_sorted = sorted(mappings, key=lambda x: max(frequency[x['char1']], frequency[x['char2']]), reverse=True)
        
#         return mappings_sorted
    
#     def __getRotorMapping(self, rotorNo, char, isReflected):
#         rotor = self.__rotorPositions[rotorNo]
#         for i, val in enumerate(rotor):
#             if isReflected:
#                 if rotor[i][1] == letters.index(char):
#                     return letters[rotor[i][0]], i
#             else:   
#                 if rotor[i][0] == letters.index(char):
#                     return letters[rotor[i][1]], i
    
#     def __feedThroughRotor(self, char):
#         # Function to get the mapping of letters through enigma 
#         r1Char, i1 = self.__getRotorMapping(0, char, False)
#         r2Char, i2 = self.__getRotorMapping(1, letters[self.__rotorPositions[1][i1][0]], False)
#         r3Char, i3 = self.__getRotorMapping(2, letters[self.__rotorPositions[2][i2][0]], False)
        
#         reflectedChar = reflector[letters.index(r3Char)]
        
#         r3Char2, i4 = self.__getRotorMapping(2, reflectedChar, True)
#         r2Char2, i5 = self.__getRotorMapping(1, letters[self.__rotorPositions[1][i4][1]], True)
#         r1Char2, i6 = self.__getRotorMapping(0, letters[self.__rotorPositions[0][i5][1]], True)
        
#         self.__rotorPositions = self.__moveRotor(self.__rotorPositions, 1)
#         return r1Char2
    
#     # This function gives one possible plugboard configuration for the current rotor positions or 
#     # returns False if it doesn't exist.
#     def __getPlugboardConfig(self, incorrectPairs):
#         plugboardCurr = []

#         for i, char in enumerate(self.plainText):
#             if not letters.__contains__(char):
#                 continue
#             for letter in range(26):
#                 plugboardCurr.clear()
#                 guess = [char, letters[letter]]
#                 plugboardCurr.append(guess)

#                 while True:
#                     rotorOutput = self.__feedThroughRotor(char)
#                     deduction = [rotorOutput, self.cypherText[i]]
                    
#                     # If deduction conflicts with existing config, remove and skip further testing
#                     if deduction in plugboardCurr or deduction in incorrectPairs:
#                         print("deduction: ", deduction)
#                         break
                
#                     plugboardCurr.append(deduction)
                    
#                     print("PlugboardCurr: ", plugboardCurr)

#         # Return the plugboard configuration if successful
#         return plugboardCurr if plugboardCurr else False

#     def run(self):
#         for k in range(26):
#             for j in range(26):
#                 for i in range(26):
#                     # print("(", k, ") (", j, ") (", i, ")")
#                     enigma = Enigma(i, j, k, self.plugboardConfig)
#                     count = 0
#                     while True:
#                         if enigma.encrypt(self.plainText[count] == self.cypherText[count]):
#                             if count >= (len(self.plainText) - 1): return [i, j, k]
#                             count += 1
#                             continue
#                         else:
#                             break
                        
#         print("No configurations found :(")
#         return -1
    
#     def iteratePlugboard(self):
#         choose10 = list(itertools.combinations(letters, 20))
#         for lst in choose10:
#             for x in self.all_pairs(list(lst)):
#                 self.plugboardWiring = x
#                 self.plugboardWiring.update({v: k for k, v in self.plugBoardWiring.iteritems()})
#                 self.iterateRotor()

#                 self.counter += (26*26*26)
#                 isPlugCorrect = self.iterateRotor()

#                 if isPlugCorrect != -1:
#                     return [isPlugCorrect, self.plugBoardWiring]
    
#     def all_pairs(self, lst):
#         if len(lst) < 2:
#             yield lst
#             return
#         a = lst[0]
#         for i in range(1, len(lst)):
#             pair = (a, lst[i])
#             for rest in self.all_pairs(lst[1:i] + lst[i+1:]):
#                 yield [pair] + rest             
#         # Move the rotors to the current position
#         # self.__rotorPositions = self.__moveRotor(wiring, k * pow(26, 0) + j * pow(26, 1) + i * pow(26, 2))
#         # incorrectPairs = []
        
#         # plugboardConfig = self.__getPlugboardConfig(incorrectPairs)
#         # print("Setting found: ", plugboardConfig)
#         # time.sleep(1)

#         # if not plugboardConfig:
#         #     continue
        
#         # decypheredText = ""
        
#         # for char in self.cypherText():
#         #     if letters.__contains__(char):
#         #         decypheredText += enigma.encrypt(char)
#         #     else:
#         #         decypheredText += char
                            
#         # if decypheredText == self.plainText:
#         #     print("Solution found!!!")
#         #     return