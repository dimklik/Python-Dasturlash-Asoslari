'''
kirit = input('Yozing: ')

file = open('file/text.txt', 'w')

file.write(kirit + '\n')

file.close()
'''


word = open('file/text.txt', 'r')
mylist = [line.strip('\n') for line in word]
if mylist == 'admin':
    print('admin panel topildi')
print(mylist)


