'''
'trek', 'author', 'mongoose', 'specialized'
'''

bicycles = ['trek', 'author', 'mongoose', 'specialized']
numbers = [0, 1, 2, 3]

print(bicycles[1])

# список неизвестной длины
print(len(bicycles))
print(bicycles[3])

# вариант 2
print(bicycles[-1])

# использования отдельного элемента
print(f'Поздравляю! Вы приобрели велосипед марки {bicycles[2]}! Удачных вам поездок!')

# изменение элемента в списке
print(f'Изначальный вид: {bicycles}')
bicycles[2] = 'GT'
print(f'Измененный вид: {bicycles}')

# добавление элемента (возможно добавление только ОДНОГО элемента за раз)
print(f'Изначальный вид: {bicycles}')
bicycles.append('Lapierre')
# bicycles[2].append('Lapierre') - добавление на конкретное место в списке
print(f'Добавил бренд: {bicycles} \n')

# удаление элементов
cars = ['tesla', 'audi', 'mercedes', 'bmw', 'toyta']
# del cars[0] - не юзаем
cars.pop(0)  # удаление по индексу
cars.remove('mercedes')  # удаление по имени
print(cars)

print(numbers[4])
