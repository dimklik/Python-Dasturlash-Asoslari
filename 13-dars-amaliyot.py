from termcolor import colored

print('Dasturdan chiqish uchun "exit" commandasini yozing',)
chiqish = None

class Malumotlar():
    name = None
    age = None
    school = None
    occupation = None

    def malumot_berish(self, name, age, school, occupation):
        self.name = name
        self.age = age
        self.school = school
        self.occupation = occupation

    def malumot_chiqarish(self):
        print('Name -', self.name, 'age -', self.age, 'school -', self.school, 'occupation -', self.occupation,)



while chiqish != 'exit':

    try:
        kirit = input('Kim Haqida Malumot Omoqchi Siz: ')

        if kirit == 'Diyorbek':
            Diyor = Malumotlar()
            Diyor.malumot_berish('Diyorbek,', '21,', '27,', 'Programmer',)
            Diyor.malumot_chiqarish()

        if kirit == 'Umarbek':
            Umar = Malumotlar()
            Umar.malumot_berish('Umarbek', '18,', '27,', 'Driver')
            Umar.malumot_chiqarish()

        if kirit == 'Boboy':
            Bob = Malumotlar()
            Bob.malumot_berish('Boboy', '14,', '27,', 'School')
            Bob.malumot_chiqarish()

        if kirit == 'Umedjon':
            Umed = Malumotlar()
            Umed.malumot_berish('Umedjon', '8,', '1,', 'School')
            Umed.malumot_chiqarish()

        if kirit == 'Durdona':
            Dur = Malumotlar()
            Dur.malumot_berish('Durdona', '19,', '27,', 'Home')
            Dur.malumot_chiqarish()

        if kirit == 'Tahmina':
            Tah = Malumotlar()
            Tah.malumot_berish('Tahmina', '24,', '1,', 'Home')
            Tah.malumot_chiqarish()

        if kirit == 'exit':
            print('Dastur Yakulandi')
            break

        if not kirit:
            print(colored(f'Dasturda Yuq Malumotni Kiritingiz! {kirit}', on_color="red"))

    except KeyError:
        print('Dasturda Yuq Malumotni Kiritingiz!')
        
        