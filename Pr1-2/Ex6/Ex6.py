import string
import random
import time
from time import strftime
from time import gmtime
from itertools import product
from string import digits, ascii_letters
from random import sample


characters = ascii_letters + digits + "!@#$%&"

def _format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

def password_bruteforce(password): 
    kol = 0  
    tic = time.perf_counter()
    
    
    if (not password):
        password = '1234'
        
    print ('Breaking: ' + password)  
    
    for guess in product(characters, repeat=len(password)):
        guessed_password = ''.join(guess) 
        if password != guessed_password: 
            kol = kol + 1
            if (kol % 1000000 == 0):
                print (f'Attempt #{_format(kol)} execution time: {time.perf_counter() - tic:0.4f} seconds')
        else:
            break    

    toc = time.perf_counter()

    print (f'The program picked up the password: {guessed_password} on the {"{: }".format(kol)}th attempt ({_format(kol)}).')
    tmpStr = strftime("%H:%M:%S", gmtime(toc - tic))
    print(f"The calculation took {toc - tic:0.4f} seconds ({tmpStr})")

def generate_password(strPass):
    if (strPass):
        if (int(strPass)):
            length = int(strPass)
        else:
            length = 4 
    else:
        length = 4 
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
            password_bruteforce(input('Enter password (default 1234): '))
        case ["G"]:  
            password_bruteforce(generate_password(input('Enter password length (default 4): ')))
        case ["E"]:  
            break;
        case _:
            print("BAD! VERY VAD! Try again...")
    print('\n')