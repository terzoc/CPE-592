letter2Number = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8,
    'i' : 9,
    'j' : 10,
    'k' : 11,
    'l' : 12,
    'm' : 13,
    'n' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26,
    ' ' : 27
}

number2Letter = {
    1 : "a",
    2 : "b",
    3 : "c",
    4 : "d",
    5 : "e",
    6 : "f",
    7 : "g",
    8 : "h",
    9 : "i",
    10 : "j",
    11 : "k",
    12 : "l",
    13 : "m",
    14 : "n",
    15 : "o",
    16 : "p",
    17 : "q",
    18 : "r",
    19 : "s",
    20 : "t",
    21 : "u",
    22 : "v",
    23 : "w",
    24 : "x",
    25 : "y",
    26 : "z",
    27 : " "
}

def encrypt(plainText, publicKey):
    cipherText = []
    e, n = publicKey
    for P in plainText:
        cipherText.append(P ** e % n)
    return cipherText

def decrypt(cipherText, privateKey):
    plainText = []
    name = ""
    d , n = privateKey
    for C in cipherText:
        plainText.append(C ** d % n)
    for num in plainText:
        name += number2Letter[num]
    return name

def name2num(name):
    output = []
    for char in name:
        output.append(letter2Number[char])
    return output

p = 5
q = 11
n = p*q
e = 7
d = 23

publicKey = (e,n)
privateKey = (d,n)

name = "corvin terzo"
plainText = name2num(name)

print("Name: " + name)
print("Plain Text: " + ' '.join(map(str, plainText)))
cipherText = encrypt(plainText, publicKey)
print("Cipher Text: " + ' '.join(map(str, cipherText)))
decrypted = decrypt(cipherText,privateKey)
print("Decrypted Text: " + decrypted)
