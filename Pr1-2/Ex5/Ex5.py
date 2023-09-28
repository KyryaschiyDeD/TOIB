import requests
import hashlib


def openFile():
    filename = input('Enter filename (default password.txt): ')

    if filename:
        print ('Opening :' + filename + '...')
    else:
        print('using password.txt')
        filename = 'password.txt'
   
    fromFile = ""
    with open(filename, 'r', encoding='utf-8') as file:
        for passwFromFile in file:
                fromFile = goodPass + passwFromFile
    checkPass(fromFile)


def checkPass(passFromFile):
    for line in passFromFile:
        sha1_hash = hashlib.sha1((line.strip()[line.strip().find(',')+1:]).encode())
        sha1_hex = sha1_hash.hexdigest()
        req = requests.get('https://api.pwnedpasswords.com/range/'+sha1_hex[:5])
        reqStr = str(req.content.decode('ascii')).replace('\r','')
        if reqStr.find(sha1_hex[5:].upper()) == -1:
            print("The user's: " + (line.strip()[:line.strip().find(',')]) + " password has not been stolen \n")
        else:
            print("The user's: " + (line.strip()[:line.strip().find(',')]) + " password has been stolen!")

# ------------------------------------------------------
strInput = ""
while (strInput != "E"):
    print ("O - Enter the path to the file")
    print ("G - Generate a file")
    print ("E - exit")
    strInput = input(": ")
    match strInput.split():
        case ["O"]:  
            openFile()
        case ["G"]:  
            generateFile()
        case ["E"]:  
            break;
        case _:
            print("BAD! VERY VAD! Try again...")