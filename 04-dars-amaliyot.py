'''
Login sasasasas
parol 123123213
18 xo'sh kelibsiz 17 site siz uchun block disin


print("Facebook")

str(input("Loqin: "))
int(input("Parol: "))
button = int(input("Yoshingizni kiriting: "))
if button >= 18:
    print("X'osh kelibsiz")
else:
    print("Site siz uchun block")
'''

#wordlist = "admin", "pass", "domen", "html", "php"

#for i in wordlist:
#    if i == None:
#        break
#    if i == "php":
#        continue

#print(i)


import random

Boboy = 0
Komp = 0

Uyin = 0

while Uyin != 3:
    print("\nKompyuter qaysi moshini tanlaganini topishingiz kerak!")
    print("\n\"BMW\"\t\"TESLA\"\t\"AUDI\"\t\"BENTLEY\"\n")
    button = input("Qaysi Moshini olasiz: ")
    list = ['BMW', 'TESLA', 'AUDI', 'BENTLEY']
    r = random.choice(list)

    print("kompyuter " + r + " Modelni tanladi")

    if button == r:
        Boboy += 1
        print("Toptingiz:")
        print("Boboy:" + str(Boboy))

    elif button != 'BMW' and button != 'TESLA' and button != 'AUDI' and button != 'BENTLEY':
        print("Lista bundey Model yuq")
    else:
        print("Model Topilmadi:")
        print("Boboy:" + str(Boboy))

    if Boboy == 3:
        print("Yuin Tugadi")
        break



