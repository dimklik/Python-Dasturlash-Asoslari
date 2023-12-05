class malumot:
    name = None
    age = None
    isHappy = None
    school= None

    def __init__(self, name, age, isHappy, school):
        self.set_malumot(name, age, isHappy, school)

        self.get_malumot()

    def set_malumot(self, name, age, isHappy, school):
        self.name = name
        self.age = age
        self.isHappy = isHappy
        self.school = school

    def get_malumot(self):
        print(self.name, 'age', self.age, 'isHappy', self.isHappy, 'School', self.school)

asadbek = malumot('Assadbek', 20, False, 27)
diyor = malumot('Diyorbek', 21, True, 27)


