''' Program by 
Gary Khodayari
20/11/2019
'''
import os
import csv
########################
def decryptor(key , text):
    decryptedtext = ''
    for i in text :
        if ord('a') < ord(i) < ord('z'):
            char = ord(i) + key
            if char > ord('z'):
                char -= 26
            decryptedtext += chr(char)
        elif ord('A') < ord(i) < ord('Z'):
            char = ord(i) + key
            if char > ord('Z'):
                char -= 26
            decryptedtext += chr(char)
        else :
            decryptedtext += i
    return decryptedtext
while True:
    encryptedtext = input('Type in your encrypted meesage: ')
    command = input('Would like test all the possible keys ?(Y/N) ')
    if command == 'Y' or command == 'y' :
        command = input('Would you like to save the log afterwards ?(Y/N) ')
        for n in range(1,26):
            normaltext = decryptor(n , encryptedtext)
            print('With the key %d text is %s' % (n , normaltext))
            if command == 'Y' or command == 'y' :
                with open(( encryptedtext[:4] +'_ceasar_decryptor_log.txt') , 'a') as file :
                    #csvfile = csv.writer(file)
                    #csvfile.writerow([n , normaltext])
                    file.write(str(n) + '  ' + normaltext + '\n')
            else :
                continue
    elif command == 'N' or command =='n' :
        normaltext = decryptor(int(input('What Key would you like to use ? ')) , encryptedtext)
        print(normaltext)
    else :
        print('404\nBad Input')