lower = [chr(i) for i in range(97, 123)]
upper = [chr(i) for i in range(65, 91)]
spchr = ['@', '#', '$', '&', '*']
num = [str(i) for i in range(0, 10)]
password = input("Enter your password to know it's better or not\t")


lflag = uflag = sflag = nflag = False
for i in password:
    if i in upper:
        uflag = True
    elif i in lower:
        lflag = True

    elif i in spchr:
        sflag = True
    elif i in num:
        nflag = True

if (len(password) >= 8):
    if (lflag == True) and (uflag == True) and (sflag == True) and (nflag == True):
        print("strong")
    else:
        print("weak and easy to crack")
else:
    print("length of password is too short")
