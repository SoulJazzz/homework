"""Булевы значения"""

# Возвращает False так как X не равен Y
x = 0
y = 1
print(bool(x == y))

# Возвращает False так как X None
x = None
print(bool(x))

# Возвращает True так как X строка
x = 'Python'
print(bool(x))

"""Целочисленные переменные"""

x = 99
print(type(x))

"""числа с плавающей точкой"""

x = 99.1
print(type(x))

"""Массивоподобные структуры"""

# списки
list_1 = ['Hellow', 99, 'Python', 99.1, '10']
print(list_1[2])

# кортежи
tuple_1 = ('Hellow', 99, 'Python', 99.1, '10')
print(tuple_1[:1])

# словари
dict_1 = {'яблоко': 'красное', 'банан': 'жёлтый', 'авокадо': 'зелёный'}
print(dict_1.keys())
print(dict_1['банан'])

# множества
words = set('hellow')
print(words)

words_1 = ['DARK SOULS I', 'DARK SOULS III', 'DARK SOULS II', 'DARK SOULS III']
print(set(words_1))

"""Операции"""

a = 100
b = 500

# сложение
print(a + b)

# вычитание
print(a - b)

# умножение
print(a * b)

# деление
print(a / b)

# возведение в степень
print(a ** b)

"""Форматирование строк"""

# format
name = 'world'
print('Hellow', format(name))

# f-строки
name = 'world'
print(f'Hellow {name}')
