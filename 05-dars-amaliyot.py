'''users = [{"Firs_Name": "Diyorbek", "Last_Namse": "Saidqulov", "Birthday": "27.01.2002"},
{"Firs_Name": "Umarbek", "Last_Name": "Saidqulov", "Birthday": "25.08.2005"}]
Birthday = [i[s]
    for i in users
    for s in i
    if s == "Birthday"

]
First_Name = [q[w]
    for q in users
    for w in q
    if w == "Firs_Name"

]

print(First_Name)
print(Birthday)
'''


#nums = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 0]

#for i in nums:

#    print(i , end=' ')





#a = int(input('Listka nechta qimmat kiritmoqchi siz: '))

#user = []

#b = 0
#while b < a:
#    string = "Ismingiz: " + ": "
#    user.append(input(string))
#    string = "Familyangiz: " + ": "
#    user.append(input(string))
#    b += 1

#print(user)

'''
a = int(input("Sonni kiritng: "))
b = int(input("Ikinchi sonni kiriting: "))

c = input("+, -, /, * ")

if c == "+":
    e = a + b
    print(e)
elif c == "-":
    e = a - b
    print(e)
elif c == "*":
    e = a * b
    print(e)
elif c == "/":
    e = a / b
    print(e)
'''


a = str(input("Login: "))

login = []

string = "Password (Eslab qoling!): "
login.append(input(string))

print("Account " + a.upper())
b = None

while b != login:
    b = input("Password: ")
    if b == login[0]:
        print('Success')
    elif b != login[0]:
        print('Password error')
    if b == login[0]:
        break



