import time
def Diyor(name = None, age = None, city = None):
    #time.sleep(1)
    #name.__add__('Diyorbek')
    #print(name)

    res = name + age + city


    a = input('kirit: ')

    if a == 'Diyorbek':
        #print(' name - ' + name + ' age - ' + age + ' city - ' + city)
        print(res)

    if a == 'Assadbek':
        print('name - ' + name + ' age - ' + age + ' city - ' + city)
        print(res)
        print(c)

c = Diyor('Diyorbek,', '22,', 'Proletarsk')
Diyor(c)

b = Diyor('Assadbek,', '22,', 'Proletarsk')
Diyor(b)

'''

    malumot = {
        'Diyorbek':
        {
            'name': 'Diyorbek',
            'age': 22,
            'city': 'Proletarsk'
        },
        'Asadbek':
            {
          'name': 'Asadbek',
          'age': 20,
          'city': 'Proletars'
        },
        'Abdullo':
            {
            'name': 'Abdullo',
            'age': 21,
            'city': 'Gulhona'
        },
        'Iskandar':
            {
            'name': 'Iskandar',
            'age': 19,
            'city': 'Proletarsk'
        }
    }

    print('Diyorbek', 'Asadbek', 'Abdullo', 'Iskandar')
    kirit = input('kim haqida malumot omoqchi siz: ')

    print('name -', name, 'age -', age, 'city -', city)

    if kirit.capitalize() == 'Diyorbek':
        for key, value in malumot['Diyorbek'].items():
            print(key, ' - ', value)

'''





