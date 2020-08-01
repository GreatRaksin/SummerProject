# dictionary = {} <- словарь

user = {
    'username': 'Zodiac',
    'email': 'zodi@ya.ru',
    'password': '********',
    'avatar': None,
    'orders': ['tooth paste', 'microphone', 'pizza', 'camera']
}

print(f'Привет, {user["username"]}')

print(f'Ты заказывал: {user["orders"][1]}')

# добавление в словарь -> user['history'] = 32847293847
car = {}

car['door'] = 4
car['engine'] = 2.5

print(car)
car['door'] = 2
print(car)
# удаление пары ключ:значение из словаря
del car['door']
print(car)

############
'''Перебор элементов словаря'''

for key, value in user.items():
    print(f'Ключ: {key}')
    print(f'Значение: {value}\n')

# перебор ТОЛЬКО ключей, на выходе получу кортежи из (ключ, значение)-> for key, value in user.title()
# перебор ТОЛЬКО ключей, на выходе получу названия ключей -> for key in user
