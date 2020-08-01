# если я хочу определенную функцию из библиотеки
from random import randint

'''
# если я хочу сразу всю библиотеку
from random import *

randint(1, 100) - случайное целое число от 1 до 100

# я не знаю, чего я хочу
import random -> random.randint(1, 100) - случайное целое число от 1 до 100
import random as r -> r.randint(1, 100) - случайное целое число от 1 до 100

'''

list_1 = []
for digit in range(1, 12):
    list_1.append(randint(1, 20))

print(list_1)

list_2 = [randint(1, 20) for digit in range(1, 12)]

print(list_2)
