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
	    

for _ in range(count):
	password = generate_password()
	print(password)