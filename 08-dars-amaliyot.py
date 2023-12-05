print("Dasturdan chiqish uchun 'exit' komadasini tering")
print("id-1, id-2, id-3")
b = None

Maktab_27 = {
    'id-1':
        {

        'Nom': 'Diyorbek',
        'Fmiliya': 'Saidqulov',
        'Sinf': '9B',

        },
        'id-2': {

            'Nom': 'Abdullo',
            'Fmiliya': 'Boqimamatov',
            'Sinf': '9A',

        },
        'id-3': {

        'Nom': 'Iskandar',
        'Fmiliya': 'Azizov',
        'Sinf': '8B',

    }

}

while b != 'exit':
    a = input("Qaysi o'quvchi haqida malumot omoqchi siz: ")

    if a == 'id-1':
        for key, value in Maktab_27['id-1'].items():
            print(key, ' - ', value)
    if a == 'id-2':
        for key, value in Maktab_27['id-2'].items():
            print(key, ' - ', value)
    if a == 'id-3':
        for key, value in Maktab_27['id-3'].items():
            print(key, ' - ', value)
    if a == 'exit':
        print('Dastur Yakulandi')
        break