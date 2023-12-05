word = 'Tajikistan, dushanbe, khujand'
#print(len(word))
#print(word.count("a"))
print(word.upper())
print(word.isupper())
print(word.islower())
print(word.lower())
print(word.capitalize())
print(word.find('i'))
print(word.split(', '))

hobby = word.split(', ')
print(hobby[1])

for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

print(hobby)

for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

result = ', '.join(hobby)
print(result)


word = 'Football'

print(word[0:4])

word = 'Football'
print(word[4:8])



word = 'Football'

print(word[0:4:2])


list = [6, 4, 'Stroka', True, 6.8]
print(list[2:-1])
print(list[:4:])


