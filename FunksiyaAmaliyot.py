import random
from termcolor import colored

def sontop(x=10):
    ''' 1-dan 10-gacha random tarzda raqam saylash fuksiyasini tuzdim!
    Funksiyaga majburiy qiymat berib kettim (x=10) '''
    
    tasodifiy_son = random.randint(1, x)
    print(colored(f"Men 1 dan {x} son o'yladim topa olasizmi? ", 'blue'))
    shot = 0

    while True:
        shot +=1
        kiritilgan_son = int(input(colored("O'ylagan soningizi kiriting: ", 'green')))
        if kiritilgan_son < tasodifiy_son:
            print(colored(f"Xato. Men o'ylagan son bundan kattaroq. Yana harakat qilib kuring:", 'red'))
        elif kiritilgan_son > tasodifiy_son:
            print(colored(f"Xato. Men o'ylagan son bundan kichikroq. Yana harakat qilib kuring:", 'red'))
        else:
            break
    print(colored(f"Tabriklaymiz {shot} taxmin bilan toptingiz!", 'blue'))
    return shot



def sontop_pc(x=10):
    ''' PC - Biz O'ylagan soni topuvchi Funksiya Yozdim'''

    input(colored(f"1-dan {x} - gacha son o'ylang man topaman: Istalgan tugmani bosing: ", 'green'))
    boshlanishi = 1
    ohiri = x
    shot = 0

    while True:
        shot += 1
        if boshlanishi != ohiri:
            pc_oylagan_son = random.randint(boshlanishi, ohiri)
        else:
            pc_oylagan_son = ohiri

        pc_oylagan_son_topish = str(input(colored(f"Siz {pc_oylagan_son} sonini o'yladingiz: To'gri (T),"
        f"Man o'ylagan son bundan kataroq (+), Yoki kichikroq (-): ".capitalize(), 'blue')))

        if pc_oylagan_son_topish == "+":
            boshlanishi = pc_oylagan_son + 1
        elif pc_oylagan_son_topish == "-":
            ohiri = pc_oylagan_son - 1
        else:
            break
    print(colored(f"Man {shot} tahmin bilan topdim", 'blue'))
    return pc_oylagan_son



def play(x=10):
    while True:
        qayta_oynash = True
        Users = sontop(x)
        PC = sontop_pc(x)

        if Users < PC:
            print(colored(f"PC - Man Yutdim!", 'green'))
        elif PC < Users:
            print(colored(f"User - Siz Yutdingiz!", 'green'))
        else:
            print(colored("Durrang", 'green'))

        qayta_oynash = int(input(colored("Yana O'ynaysizmi? Ha (1) / Yo'q (0):", 'blue')))
        if qayta_oynash == False:
            print(colored("Dastur Yakulandi: Rahmat", 'green'))
            break
play()







