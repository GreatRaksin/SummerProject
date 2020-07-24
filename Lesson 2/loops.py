# ну-ка повтори...
'''
1) for
2) управляющая_переменная (i)
3) in
4) что_итерируем (range или список)
5) :
6) отступы

for i in range(10)/my_list:
--->commands
'''

numbers = [13, 65, 87, 84, 48, 63, 86, 63, 33, 99, 96, 4, 98, 91, 18, 61, 11, 16, 82, 23, 77, 86, 42, 94, 81, 41, 65,
           24, 80, 39]

# вывод КАЖДОГО элемента (по отдельности)

divided_numbers = []
for number in numbers:  # Для каждого элемента в массиве numbers
    print(f'{number} / 3 = {number / 3}')
    divided_numbers.append(number / 3)

print(divided_numbers)

######################

'''Функция range

range(10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(1, 10) -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
range(1, 10, 2) -> [1, 3, 5, 7, 9]
'''
for i in range(0, 101, 5):
    print(i)
    print('Помни про отступы')
    print(i ** 2)
