import random
import copy

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
           "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
           "U", "V", "W", "X", "Y", "Z"]


wiring = [
        # Rotor 1 TCIXAGDHRZLVPKEMSNQFBWYJOU
        [[0, 19], [1, 2], [2, 8], [3, 23], [4, 0], [5, 6], [6, 3], [7, 7],
        [8, 17], [9, 25], [10, 11], [11, 21], [12, 15], [13, 10], [14, 4],
        [15, 12], [16, 18], [17, 13], [18, 16], [19, 5], [20, 1], [21, 22],
        [22, 24], [23, 9], [24, 14], [25, 20]],
        
        # Rotor 2 KJTDLXWFPIMYSOUHEVCRBAQGZN
        [[0, 10], [1, 9], [2, 19], [3, 3], [4, 11], [5, 23], [6, 22], [7, 5],
        [8, 15], [9, 8], [10, 12], [11, 24], [12, 18], [13, 14], [14, 20],
        [15, 7], [16, 4], [17, 21], [18, 2], [19, 17], [20, 1], [21, 0],
        [22, 16], [23, 6], [24, 25], [25, 13]],
        
        # Rotor 3 ACYKROZQUWLBIGSNPTDJFVHEXM
        [[0, 0], [1, 2], [2, 24], [3, 10], [4, 17], [5, 14], [6, 25], [7, 16],
        [8, 20], [9, 22], [10, 11], [11, 1], [12, 8], [13, 6], [14, 18],
        [15, 13], [16, 15], [17, 19], [18, 3], [19, 9], [20, 5], [21, 21], 
        [22, 7], [23, 4], [24, 23], [25, 12]]
        ]

reflector = ["E", "S", "O", "V", "P", "Z", "J", "A", "Y", "Q",
             "U", "I", "R", "H", "X", "L", "N", "F", "T", "G",
             "K", "D", "C", "M", "W", "B"]

class Enigma:
    def __init__(self, *args):
        if len(args) == 0:
            self.__mrotor1 = random.randint(0, 25)
            self.__mrotor2 = random.randint(0, 25)
            self.__mrotor3 = random.randint(0, 25)
            
            self.__rotor1 = 0
            self.__rotor2 = 0
            self.__rotor3 = 0

        if len(args) == 3:
            self.__mrotor1 = args[0]
            self.__mrotor2 = args[1]
            self.__mrotor3 = args[2]
            
            self.__rotor1 = 0
            self.__rotor2 = 0
            self.__rotor3 = 0
            
        self.__plugboardConfig = self.__getConfig()
        self.__rotorWiring = self.__moveRotor(wiring, self.__mrotor1 * pow(26, 0) + self.__mrotor2 * pow(26, 1) + self.__mrotor3 * pow(26, 2))
    
    def __getConfig(self):
        lettersCopy = copy.deepcopy(letters)
        config = []
        for i in range (10):
            idx1 = random.randint(0, len(lettersCopy) - 1)
            letter1 = lettersCopy[idx1]
            del lettersCopy[idx1]

            idx2 = random.randint(0, len(lettersCopy) - 1)
            letter2 = lettersCopy[idx2]
            del lettersCopy[idx2]
            
            pair = [letter1, letter2]
            config.append(pair)
        return config
        
    def __moveRotor(self, wiringStart, n):
        wiringCopy = copy.deepcopy(wiringStart)
        for i in range (n):
            # Move the first rotor one place
            wiringCopy[0] = wiringCopy[0][-1:] + wiringCopy[0][:-1]
            self.__rotor1 += 1
            
            # If the first rotor completes a revolution move the second rotor one place
            if wiringCopy[0] == wiring[0]:
                wiringCopy[1] = wiringCopy[1][-1:] + wiringCopy[1][:-1]
                self.__rotor1 = 0
                self.__rotor2 += 1
                
                # If the second rotor completes a revolution move the third rotor one place
                if wiringCopy[1] == wiring[1]:
                    wiringCopy[2] = wiringCopy[2][-1:] + wiringCopy[2][:-1]
                    self.__rotor2 = 0
                    self.__rotor3 += 1
                    
                    # If the third rotor completes a revolution reset all rotors
                    if wiringCopy[2] == wiring[2]:
                        wiringCopy[0] = copy.deepcopy(wiring[0])
                        wiringCopy[1] = copy.deepcopy(wiring[1])
                        wiringCopy[2] = copy.deepcopy(wiring[2])
                        self.__rotor3 = 0
        return wiringCopy
    
    def __getPlugboardMapping(self, char):
        plugboardChar = char
        
        for i, _ in enumerate(self.__plugboardConfig):
            for j, _ in enumerate(self.__plugboardConfig[i]):
                if char == self.__plugboardConfig[i][j]:
                    plugboardChar = self.__plugboardConfig[i][0] if j == 1 else self.__plugboardConfig[i][1]
                    
        return plugboardChar
    
    def __getRotorMapping(self, rotorNo, char, isReflected):
        rotor = self.__rotorWiring[rotorNo]
        for i, val in enumerate(rotor):
            if isReflected:
                if rotor[i][1] == letters.index(char):
                    return letters[rotor[i][0]], i
            else:   
                if rotor[i][0] == letters.index(char):
                    return letters[rotor[i][1]], i
            
        print("SOMETHING BAD HAPPENED :(")
    
    def encrypt(self, char):
        # Plugboard
        plugboardMap = self.__getPlugboardMapping(char)
                
        r1Char, i1 = self.__getRotorMapping(0, plugboardMap, False)
        r2Char, i2 = self.__getRotorMapping(1, letters[self.__rotorWiring[1][i1][0]], False)
        r3Char, i3 = self.__getRotorMapping(2, letters[self.__rotorWiring[2][i2][0]], False)
        
        reflectedChar = reflector[letters.index(r3Char)]
        
        r3Char2, i4 = self.__getRotorMapping(2, reflectedChar, True)
        r2Char2, i5 = self.__getRotorMapping(1, letters[self.__rotorWiring[1][i4][1]], True)
        r1Char2, i6 = self.__getRotorMapping(0, letters[self.__rotorWiring[0][i5][1]], True)
        
        # Plugboard
        encryptedChar = self.__getPlugboardMapping(r1Char2)
        
        # print(char, "->", plugboardMap, "-> (", r1Char, i1, ") -> (", r2Char, i2, ") -> (", r3Char, i3, ") -> (", 
        #       reflectedChar, ") -> (", r3Char2, i4, ") -> (", r2Char2, i5, ") -> (", r1Char2, i6, ") ->", encryptedChar)
        
        self.__rotorWiring = self.__moveRotor(self.__rotorWiring, 1)
        
        return encryptedChar
    
    def resetRotors(self):
        self.rotor1 = self.__mrotor1
        self.rotor2 = self.__mrotor2
        self.rotor3 = self.__mrotor3
        self.__rotorWiring = self.__moveRotor(wiring, self.__rotor1 * pow(26, 0) + self.__rotor2 * pow(26, 1) + self.__rotor3 * pow(26, 2))
    
    def getInfo(self):
        print("------Start of Info-----")
        print("Starting rotor number")
        print("Rotor 1: ", self.__mrotor1)
        print("Rotor 2: ", self.__mrotor2)
        print("Rotor 3: ", self.__mrotor3)
        print("------------------------")
        print("Current rotor number")
        print("Rotor 1: ", self.__rotor1)
        print("Rotor 2: ", self.__rotor2)
        print("Rotor 3: ", self.__rotor3)
        print("------------------------")
        print("Plugboard Configuration:")
        print(self.__plugboardConfig)
        print("--------End of Info-----")
        print()