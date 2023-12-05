from termcolor import colored

kirit = input(colored( "Sozni toping: ", 'blue'))

print(colored( 'as', 'blue'))

word = open('file/text.txt', 'w')
for line in word:
    if kirit == line:
        print("S'oz topildi")
        break

