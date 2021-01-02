import art

def ceaser(textval, shiftval , directionop) :
    if direction == 'encode' :
        decryptedtext = ""
        for l in textval.lower() :
            if l not in alphabet :
                decryptedtext += l
            else :
                index = alphabet.index(l) - shift
                while index <= -26 :
                    index += 26
                decryptedtext += alphabet[index]
        return decryptedtext
    elif direction == 'decode' :
        encryptedtext = ""
        for l in textval.lower() :
            if l not in alphabet :
                encryptedtext += l
            else :
                index = alphabet.index(l) + shift
                while index >= 26 :
                    index -= 26
                encryptedtext += alphabet[index]
        return encryptedtext

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keepgoing = "yes"

print(art.logo)
while keepgoing == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(ceaser(textval=text, shiftval=shift, directionop=direction))
    keepgoing = input("Do you want to keep going ? (yes/no) ")
else :
    print("Goodbye")