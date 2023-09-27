import hashlib


def hash_string(input):
    byte_input = input.encode()
    hash_object = hashlib.sha256(byte_input)
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