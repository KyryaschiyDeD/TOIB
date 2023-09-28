import string
import random

def generate_password(length = 8):
	chars = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(random.choice(chars) for i in range(length))
	return password

num = [i for i in range(0,10)]
letdown = list(string.ascii_lowercase)
letup = list(string.ascii_uppercase)
spec = "!@#$%&"

def good_password(password):
    hasNum=False
    hasUp=False
    hasDown=False
    hasSpec=False
    for char in password:
        if char.isdigit():
            if int(char) in num:
                hasNum = True
        if char in letdown:
            hasDown = True
        if char in letup:
            hasUp = True
        if char in spec:
            hasSpec = True
    return hasNum and hasDown and hasUp and hasSpec and (len(password) >= 8)

def generateFile():
    countFromConsole = input('Enter password count: ')
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
            
    file = open("password.txt", "w")
    for _ in range(count):
        file.write(generate_password(lenght)+"\n")
    file.close
    
    goodPass = ""
    with open('password.txt', 'r', encoding='utf-8') as file:
        for passwFromFile in file:
            isGood = good_password(passwFromFile)
            print(passwFromFile.replace("\n","")+" ::: "+str(isGood))
            if (isGood):
                goodPass = goodPass + passwFromFile
                
    print ("\n<-------------------------->\n")
    print ("Good passwords:")
    print (goodPass)
    print ("<-------------------------->")
    
 
def openFile():
    filename = input('Enter filename (default password.txt): ')

    if filename:
        print ('Opening :' + filename + '...')
    else:
        print('using password.txt')
        filename = 'password.txt'
   
    goodPass = ""
    with open(filename, 'r', encoding='utf-8') as file:
        for passwFromFile in file:
            isGood = good_password(passwFromFile)
            print(passwFromFile.replace("\n","")+" ::: "+str(isGood))
            if (isGood):
                goodPass = goodPass + passwFromFile
                
    print ("\n<-------------------------->\n")
    print ("Good passwords:")
    print (goodPass)
    print ("<-------------------------->")    

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


