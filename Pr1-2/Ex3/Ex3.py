gimport string

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

print('<-- xD -->')
print ('To exit, use exit')
print('<-- xD -->')

passwStr = ""
while (passwStr != "exit"):
    passwStr = input("Enter password (default QwErTy1!2): ")
    if (not passwStr):
        passwStr = "QwErTy1!2"
    
    if (passwStr == "exit"):
        break

    if (good_password(passwStr)):
        print ("Valid password!!!")
    else:
        print ("The password does not meet the requirements :-(")
