"""
def hash_string(input): Возвращает хэшированный объект
"""
import hashlib

def hash_string(input):
    hash_object = hashlib.sha256(input.encode())
    return hash_object


str = "";
print('To exit, use exit')
while(str != "exit"):
    str = input('Enter your string: ')
    if (str == "exit"):
        break
    else:
        hash_object = hash_string(str)
        print(hash_object.hexdigest())