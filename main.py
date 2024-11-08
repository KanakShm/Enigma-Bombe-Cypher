import Enigma

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
           "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
           "U", "V", "W", "X", "Y", "Z"]

def main():
    enigma = Enigma.Enigma(0, 0, 0)
    f = open("files/email.txt")
    original = f.read().upper()
    encrypted = ""
    for i in original:
        if letters.__contains__(i):
                encrypted += (enigma.encrypt(i))
        else:
            encrypted += i
    f.close()
    
    f = open("test.txt", "w")
    f.write(encrypted)
    f.close()
    
    # for i in f1.read():
    #     f2.read()[i] = enigma.encrypt(f1.read()[i])
    # f1.close()
    # f2.close()
    
if __name__ == '__main__':
    main()