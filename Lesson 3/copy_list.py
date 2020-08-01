food = ['pizza', 'falafel', 'shawarma', 'burger']
delivery_food = food[:]

delivery_food.append('cola')  # добавляю ИМЕННО в доставку
food.append('potato')  # добавляю ИМЕННО в основное меню

print(f'Все меню ресторана: {food}')
print(f'Меню на доставку: {delivery_food}')
