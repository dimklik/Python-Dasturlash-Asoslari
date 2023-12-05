country = {'code': 'TJ', 'name': 'Tajikistan', 'population': '10M'}

for key, value in country.items():

    print(key, " - ", value)


print(country.get('name'))
country.clear()
#country.pop('name')
#country.popitem()
country['name'] = 'None'



