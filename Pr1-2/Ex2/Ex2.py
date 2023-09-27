import random
import string

def generate_password(length = 8):
	chars = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(random.choice(chars) for i in range(length))
	return password

countFromConsole = input('Enter password count (default 1): ')

if countFromConsole:
	if int(countFromConsole):
		count = int(countFromConsole)
	else:
		print('Error')
else:
	count = 1
	    

lenghtFromConsole = input('Enter password length (default 8): ')

if lenghtFromConsole:
	if int(lenghtFromConsole):
		lenght = int(lenghtFromConsole)
	else:
		print('Error')
else:
	lenght = 8

print('<-- xD -->')

for _ in range(count):
	password = generate_password(lenght)
	print(password)
	
print('<-- xD -->')