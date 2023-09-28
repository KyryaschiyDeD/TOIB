import string
import random
import time
from time import strftime
from time import gmtime
from itertools import product
from random import sample


characters = string.ascii_letters + string.digits + string.punctuation

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
        
    print ('Ломаем: ' + password)  
    kol = 239000000
    for guess in product(characters, repeat=len(password)):
        guessed_password = ''.join(guess) 
        if password != guessed_password: 
            kol = kol + 1
            if (kol % 1000000 == 0):
                print (f'Попытка #{_format(kol)} | Прошло времени: {time.perf_counter() - tic:0.4f} секунд')
        else:
            break    

    toc = time.perf_counter()

    print (f'Сломали пароль: {guessed_password} за {"{: }".format(kol)} попыток ({_format(kol)}).')
    tmpStr = strftime("%H:%M:%S", gmtime(toc - tic))
    print(f"Прошло времени {toc - tic:0.4f} секунд ({tmpStr})")

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
    print ("O - Ввести пароль")
    print ("G - Сгенерировать пароль")
    print ("E - выйти")
    strInput = input(": ")
    match strInput.split():
        case ["O"]:  
            password_bruteforce(input('Введите пароль (default 1234): '))
        case ["G"]:  
            password_bruteforce(generate_password(input('Введите длину пароля (default 4): ')))
        case ["E"]:  
            break;
        case _:
            print("BAD! VERY BAD! Попробуйте снова...")
    print('\n')