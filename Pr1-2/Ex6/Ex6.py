from itertools import product
import string
import random
from string import digits, ascii_letters
from random import sample


characters = ascii_letters + digits

def password_bruteforce(password): 
    kol = 0  
    for guess in product(characters, repeat=len(password)):
        guessed_password = ''.join(guess) 
        if password != guessed_password: 
            kol += 1
        else:
            break 
    print (f'The program picked up the password: {guessed_password} on the {kol}th attempt.')

def generate_password(strPass):
    if (strPass):
        if (int(strPass)):
            length = int(strPass)
        else:
            length = 8 
    else:
        length = 8 
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

strInput = ""
while (strInput != "E"):
    print ("O - Enter the password")
    print ("G - Generate a password")
    print ("E - exit")
    strInput = input(": ")
    match strInput.split():
        case ["O"]:  
            password_bruteforce(input('Enter password (default 12345678): '))
        case ["G"]:  
            password_bruteforce(generate_password(input('Enter password length (default 8): ')))
        case ["E"]:  
            break;
        case _:
            print("BAD! VERY VAD! Try again...")
    print('\n')