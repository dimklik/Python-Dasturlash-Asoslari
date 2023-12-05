ism = 'diyorbek, umarbek, boboy, tahmina'

r = ism.split('b ')
i = 0

for i in range(len(r)):

    r[i] = r[i].capitalize()
    if i == ism.count('d'):
        print(i)
        i += 1


result = 'b '.join(r)

print(result)





