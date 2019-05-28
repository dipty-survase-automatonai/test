import re
pwd=input("enter passwd: ")
flag = 0
while True:
    if (len(pwd) < 8 or len(pwd)>15):
        flag = -1
        break
    elif not re.search("[a-z]", pwd):
        flag = -1
        break
    elif not re.search("[A-Z]", pwd):
        flag = -1
        break
    elif not re.search("[0-9]", pwd):
        flag = -1
        break
    elif not re.search("[#@$]", pwd):
        flag = -1
        break
    elif re.search("\s", pwd):
        flag = -1
        break
    else:
        flag = 0
        print("Password is correct")
        break

if flag == -1:
    print("Password is incorrect")
