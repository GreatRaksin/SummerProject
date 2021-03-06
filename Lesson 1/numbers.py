# Математические операции (стандарт)
print(2 + 4)
print(5 * 6)
print(10 - 4)
print(10 / 3)

print()

# Расширенная версия
print(3 ** 2)  # возведение в степень
print(10 // 3)  # целочисленное деление
print(10 % 3)  # возврат остатка от деления

print()

# Приведение типов
float_point_number = 2.6
print(f'Вывод дробного числа {float_point_number}')
print(f'Вывод целого числа {int(float_point_number)}')  # просто отбрасываем дробную часть
print(
    f'Вывод округленного целого числа {round(float_point_number)}')  # округляем число до целого по правилам математики

b = int(input('Введи число: '))  # Превращаем возврат инпута в число
print(b + 14)
