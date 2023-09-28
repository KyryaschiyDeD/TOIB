"""
def generate_password(length = 8): генерирует пароль
def openFile(filename): открывает файл и считывает всё построчно
def checkPass(passFromFile): проверяет пароль и выводит
def generateFile(): генерирует файл
"""
import requests
import hashlib
import string
import random

def generate_password(length = 8):
	chars = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(random.choice(chars) for i in range(length))
	return password

def openFile(filename):
    if filename:
        print ('Opening : ' + filename + '...')
    else:
        print('using password.txt')
        filename = 'password.txt'
   
    linesFromFile = ""
    with open(filename, 'r', encoding='utf-8') as file:
        for passwFromFile in file:
            linesFromFile = linesFromFile + passwFromFile
            
    checkPass(linesFromFile)


def checkPass(passFromFile):
    for line in passFromFile.splitlines():
        sha1_hash = hashlib.sha1((line.strip()[line.strip().find(',')+1:]).encode())
        sha1_hex = sha1_hash.hexdigest()
        req = requests.get('https://api.pwnedpasswords.com/range/'+sha1_hex[:5])
        reqStr = str(req.content.decode('ascii')).replace('\r','')
        if reqStr.find(sha1_hex[5:].upper()) == -1:
            print("The user's: " + (line.strip()[:line.strip().find(',')]) + " password has not been stolen! GOOD GOOD GOOD! \n ")
        else:
            print("The user's: " + (line.strip()[:line.strip().find(',')]) + " password has been stolen! BAD BAD BAD!!!!!")


def generateFile():
    countFromConsole = input('Enter users count: ')
    if countFromConsole:
         if int(countFromConsole):
              count = int(countFromConsole)
         else:
              print('Error')
              return
    else:
         print('Error')
         return
         
    lenghtFromConsole = input('Enter password length (default 8): ')

    if lenghtFromConsole:
        if int(lenghtFromConsole):
            lenght = int(lenghtFromConsole)
        else:
            print('Error (...we are use default...)')     
    
    if (not lenght):
        lenght = 8
           
    filename = "password.txt"
    file = open(filename, "w+")
    number = 0
    for _ in range(count):
        file.write("user" + str(number) + "," + generate_password(lenght)+"\n")
        number = number + 1
    file.close
    return filename
# ------------------------------------------------------
strInput = ""
while (strInput != "E"):
    print ("O - Enter the path to the file")
    print ("G - Generate a file")
    print ("E - exit")
    strInput = input(": ")
    match strInput.split():
        case ["O"]:  
            openFile(input('Enter filename (default password.txt): '))
        case ["G"]:  
            openFile(generateFile())
        case ["E"]:  
            break;
        case _:
            print("BAD! VERY VAD! Try again...")