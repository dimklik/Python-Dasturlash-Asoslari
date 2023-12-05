class MalumotlarBazasi:
    def __init__(self):
        self.line = []

    def malumot_kiritish(self):
        print('"exit" - commandasi Dasturni yakunlash uchun')
        kirit = input('Maulomotlaringizi kiritishingiz mumkin: ')
        if kirit.lower() == 'exit':
            print("Dastur Yakunlandi.")
            return False
        self.line.append(kirit)
        return True
    
   
   # def Kiritilmadi(self):
   #     if not self.kirit:
   #         return 'Malumot Kiritmadingiz'
    

    def malumot_kurish(self):
        print("Malumotigizni Kurishni Hohlasengiz - 'K' - commandasini bosing")
        kammanda = input()
        if kammanda.capitalize() == 'K':
            for value in self.line:
                print(value)

    def povtor(self):
        while True:
            if not self.malumot_kiritish():
                break
            self.malumot_kurish()


if __name__ == "__main__":
    malumotlar_bazasi = MalumotlarBazasi()
    malumotlar_bazasi.povtor()




