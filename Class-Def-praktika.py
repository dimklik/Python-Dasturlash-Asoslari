import random
from termcolor import colored

class oop_praktika():
    def __init__(self):
        self.ismlar = ['D______z', 'D_____a', 'T_____a', 'B___y', 'D______k', 'U_____k', 'U_____n', 'G______r', 'A_____r']
        self.console = print("Sizga random tarxda (ISM)-lar beriladi shuni topishingiz kerak")
        self.button = input("O'yini boshlash uchun (Enter)-Bosing: ")


    def ismlarni_chiqarish(self):
            return random.choice(self.ismlar)
          

    def shartlar_bajarilishi(self):
        shot = 0
        
        while shot != 5:
            chaqirish = self.ismlarni_chiqarish()
            print(f"{chaqirish} (ISM) {len(chaqirish)} Harf-dan iborat")
            shart_button = input(f"(ISM)-ni Toping ")
            shot += 1

            if shart_button.capitalize() == 'Dilafruz':
                print(colored(f"Javobingiz T'ogri {shart_button.capitalize()}", 'green'))
            elif shart_button.capitalize() == 'Durdona':
                print(colored(f"Javobingiz T'ogri {shart_button.capitalize()}", 'green'))
            elif shart_button.capitalize() == 'Tahmina':
                print(colored(f"Javobingiz T'ogri {shart_button.capitalize()}", 'green'))
            elif shart_button.capitalize() == 'Boboy':
                print(colored(f"Javobingiz T'ogri {shart_button.capitalize()}", 'green'))
            elif shart_button.capitalize() == 'Diyorbek':
                print(colored(f"Javobingiz T'ogri {shart_button.capitalize()}", 'green'))
            elif shart_button.capitalize() == 'Umarbek':
                print(colored(f"Javobingiz T'ogri {shart_button.capitalize()}", 'green'))
            elif shart_button.capitalize() == 'Umedjon':
                print(colored(f"Javobingiz T'ogri {shart_button.capitalize()}", 'green'))
            elif shart_button.capitalize() == 'Gulbahor':
                print(colored(f"Javobingiz T'ogri {shart_button.capitalize()}", 'green'))
            elif shart_button.capitalize() == 'Alisher':
                print(colored(f"Javobingiz T'ogri {shart_button.capitalize()}", 'green'))
            elif not shart_button:
                print(colored(f"Hech qandaey qimmat kiritmadingiz: {shart_button.capitalize()}", 'red'))
            elif shot == 5:
                print("O'yin Yakunlandi:")
                break
            else:
                print(colored(f"Bunday ISM yo'q: {shart_button.capitalize()}", 'red'))
        
if __name__ == "__main__":
    suz_oyini = oop_praktika()
    suz_oyini.shartlar_bajarilishi()



