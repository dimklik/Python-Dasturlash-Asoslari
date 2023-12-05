b = input('Tanlang: ')

class malumot:
    name = None
    age = None
    isHappy = None
    school= None



    def set_malumot(self, name, age, isHappy, school):
        self.name = name
        self.age = age
        self.isHappy = isHappy
        self.school = school

    def get_malumot(self):
        print(self.name, 'age', self.age, 'isHappy', self.isHappy, 'School', self.school)

if b == 'Assadbek':
    asadbek = malumot()
    asadbek.set_malumot('Assadbek', 20, False, 27)
    asadbek.get_malumot()

if b == 'Diyorbek':
    diyor = malumot()
    diyor.set_malumot('Diyorbek', 21, True, 27)
    diyor.get_malumot()