import Enigma

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
           "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
           "U", "V", "W", "X", "Y", "Z"]

def main():
    enigma = Enigma.Enigma()
    while True:
        # enigma.getInfo()
        print("Enter a string:    ", end="")
        string = input().upper()
        encrypted = []
        for i, val in enumerate(string):
            if letters.__contains__(string[i]):
                encrypted.append(enigma.encrypt(string[i]))
            else:
                encrypted.append(string[i])
            
        # Format output
        encrypted = ''.join(encrypted)
        print("Encrypted string: ", encrypted)
        print("***********************")
    
if __name__ == '__main__':
    main()