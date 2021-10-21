def alphabet(): #Creates and alphabet with the addition of spaces and question marks
    chars = [chr(i) for i in range(ord("a"),ord("z")+1)]
    caps = []
    for letter in chars:
        caps.append(letter.capitalize())
    caps.append(" ")
    caps.append("?")
    return chars+caps

def encrypt(text):#converts input into a code
    encrypt = []
    for letter in text:
        try:
            encrypt.append((key1[letter]))
        except KeyError:
            try:
                letter = int(letter)
                encrypt.append((key2[letter]))
            except:
                encrypt.append(letter)
        else:
            pass
    print(encrypt)

def decrypt(code):#converts code back into readable text
    text = []
    for number in code:
        try:
            text.append(key2[number])
        except KeyError:
            try:
                number = str(number)
                text.append(str(key1[number]))
            except:
                text.append(number)
        else:
            pass
    
    print ("".join(text))


def shuffle(deck,count):#shuffles the alpahbet 
        A = deck
        B = []
        for x in range(count):
            decklen = len(A) #54
            halflen = int(len(A)/2) #27
            for x in range(halflen):
                    B.append(A[decklen-1])
                    B.append(A[halflen-1])
                    halflen -= 1
                    decklen -= 1
            A = B
            B = []
        return A

def setshuffles():#how many times to shuffle  
    while True:
        try:
            shuffles = int(input("Password? "))
        except ValueError:
            print("Please enter a valid value")
            continue
        else:
            return int(shuffles)
            break

def setkey1(shuffles):#using the shuffled alphbet, set the values for letters
    a = alphabet()
    deck = {}
    count = 1
    for x in shuffle(a,shuffles):
        deck [x]=count
        count += 1
    return deck

def setkey2(target): #using the first key, creates a mirrored key
    return dict([(value,key) for key,value in target.items()])


def spacefind(key):#find the value in the key that uses a space as its value
    for value in key:
        if value == " ":
            print (key[value])
            
shuffles = setshuffles()    
key1 = setkey1(shuffles) #text -> numbers
key2 = setkey2(key1)#numbers to text

sometext = "the quick brown fox jumped over the lazy dog"
somecode = [20, 8, 5, 53, 17, 21, 9, 3, 11, 53, 2, 18, 15, 23, 14, 53, 6, 15, 24, 53, 10, 21, 13, 16, 5, 4, 53, 15, 22, 5, 18, 53, 20, 8, 5, 53, 12, 1, 26, 25, 53, 4, 15, 7]
someboth = "th1s 15 and ex4mpl3 of l33t t3xt"
test = """Cos when I went to pay I put my email n stuff ina Nd I got a "welcome go crocs! Here's 20% off" email and I did think cheeky that signing me up but not taking my payment """
numbers = "385385"

#create a gui that allows you to open files into for decryption, and write files and encrypt them.
