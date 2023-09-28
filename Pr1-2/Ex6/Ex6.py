"""
def _format(num): Превращает большое число в читабельный вид

def password_bruteforce(password): ломает пароль (можно было сравнивать в виде SHA-256, но также не стал бить 
изначальную строку на символы и их подбирать, ГЫ)

def message(kol,tic): выводит информационное сообщение о том, что мы ещё работаем

def generate_password(strPass): генерирует пароль заданной длины, либо 4

"""
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

def message(kol,tic):
    tmpStr = strftime("%H:%M:%S", gmtime(time.perf_counter() - tic))
    print (f'Попытка #{_format(kol)} | Прошло времени: {time.perf_counter() - tic:0.4f} секунд ({tmpStr})')  

def password_bruteforce(password): 
    kol = 0  
    tic = time.perf_counter()
    
    
    if (not password):
        password = '1234'
        
    print ('Ломаем: ' + password)  
    kol = 0
    for guess in product(characters, repeat=len(password)):
        guessed_password = ''.join(guess) 
        if password != guessed_password: 
            kol = kol + 1
            if (kol < 10000000): #Менее 10ти миллионов
                if (kol % 1000000 == 0): #Раз в 1 миллион попыток выводим сообщение
                    message(kol,tic)
            elif (kol < 100000000): #Менее 100
                if (kol % 10000000 == 0): #Раз в 10
                    message(kol,tic)
            elif (kol < 500000000): #Менее 500
                if (kol % 50000000 == 0): #Раз в 50
                    message(kol,tic)
            else: #Более 500
                if (kol % 100000000 == 0): #Раз в 100
                    message(kol,tic)
        else:
            message(kol,tic)
            break    

    toc = time.perf_counter()

    print (f'Сломали пароль: {guessed_password} за {"{: }".format(kol)} попыток ({_format(kol)}).')
    tmpStr = strftime("%H:%M:%S", gmtime(toc - tic))
    print(f"Прошло времени {toc - tic:0.4f} секунд ({tmpStr})")

def generate_password(strPass):
    if (strPass):
        if (str.isdigit(strPass)):
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