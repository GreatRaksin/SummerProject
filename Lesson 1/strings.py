name = 'demid raksin'
name1 = 'DEMID RAKSIN'
print(name.title())  # Каждое новое слово начинается с большой буквы
print(name.upper())  # Каждая буква переводится в верхний регистр (капс)
print(name1.lower())  # Каждая буква переводится в нижний регистр

# Конкатенация
first_name = 'Demid'
last_name = 'Raksin'
full_name = first_name + ' ' + last_name

print(full_name)

# Удаление пропусков
r_strip = 'python '
print(f'Вывод с пробелом: {r_strip}')
print(f'Вывод без пробела: {r_strip.rstrip()}')
