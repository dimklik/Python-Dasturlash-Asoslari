import random
from termcolor import colored

def suzlar_toplami():
    ''' S'ozlar toplami degan Funksiay hama ishni shu funksiay bajaradi '''

    line = ['D______z', 'D_____a', 'T_____a', 'B___y', 'D______k', 'U_____k', 'U_____n', 'G______r', 'A_____r',
     'A___r', 'O___k', 'A_____o', 'F______z', 'S______z', 'D______d', 'O___a', 'H_____a', 'D_____a', 'S_____t']

    print(colored("O'yin Qoidasi faqat ISM-larni Topish", 'magenta'))
    butt = input(colored("O'yini boshlash uchun (Enter) bosing: ", 'magenta'))
    shot = 0

    while shot != 15:
        tasodifiy_suz = random.choice(line)
        print(colored(f"{tasodifiy_suz} ISM-ni uzunligi {len(tasodifiy_suz)}", 'blue'))
        
        shot += 1
        button1 = input(colored("ISM-ni Toping: ", 'blue')).capitalize()

        if button1.capitalize() == 'Dilafruz':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Durdona':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Tahmina':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Boboy':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Diyorbek':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Umarbek':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Umedjon':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Gulbahor':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Alisher':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Anvar':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Oybek':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Abdullo':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Farangiz':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Sarvinoz':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Dilmurod':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Oysha':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Hadicha':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Dilnoza':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif button1.capitalize() == 'Shuhrat':
            print(colored(f"Javobingiz To'gri! {button1} ", 'green'))
        elif not button1:
            print(colored(f"Hech qandaey qimmat kiritmadingiz: {button1}", 'red'))
        else:
            print(colored(f"Bunday ISM yo'q: {button1}", 'red'))
        if shot == 15:
            print(colored(f"O'yin tugadi Hama (ISM)-larni Topdingiz {shot}"))
            break


suzlar_toplami()




