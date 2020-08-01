dimension = (100, 70)  # <- кортеж

'''for i in dimension:
    print(i)'''

# print(dimension[1])
# нельзя! кортеж не изменяется -> dimension[1] = 50

print(f'Оригинальные размеры прямоугольника: {dimension}')

dimension = (200, 50)
print(f'Измененные размеры прямоугольника: {dimension}')
