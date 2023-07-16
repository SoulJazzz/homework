"""Условия и циклы"""

# # простое

x = 1
y = 0
if x == 1:
    print('True')

# # с иначе

if x == 0:
    print('False')
else:
    print('True')

# # с разветвлениями

if x == 0:
    print('False')
elif y == 0:
    print('True')
else:
    print('False')

# """Арифметический цикл"""

# # цикл с предусловием

for i in range(50):
    if i == 25:
        break  # останавливаем цикл на половине чтобы не засорять log
    print(i)

# # цикл с постусловием

i = 1
while i < 10:
    print(i)
    i += 1

"""Структуры данных"""

# списки

users = ['Den', 'Alyx']
users.extend(['Bill', 'Bob'])
print(users.index('Alyx'))

if 'Bill' in users:
    users.remove('Bill')

for i in users:
    print(i)

# кортежи

tuple_1 = ('Den', 'Alyx', 'Bob', [10, 20])
for i in tuple_1:
    print(i)
tuple_1[3][0] = 11
print(tuple_1[3][0])

# множества

user = {'Den', 'Alyx', 'Bob'}
user.add('Tom')
user.remove('Den')
print('Den' in user)
user_2 = {'Den', 'Tom', 'Ted', 'SoulJazz'}
value = user.union(user_2)
for i in user_2:
    print(i)

# словари

dict_1 = {'Den': 'SoulJazz', 'Alyx': 'Half-Life', 'Bob': 'green'}
for i in dict_1.items():
    print(i)
print(dict_1['Bob'])
dict_1['Bob'] = 'Rain'
print(dict_1['Bob'])

"""Функции"""


# функция без аргументов

def hello_world():
    print('Hello world')


hello_world()


# функция с позиционными аргументами

def hello_python(*args):
    for i in args:
        print(i)


hello_python([1, 2, 'python'])


# функция с именованными аргументами

def player(hp, mp, cp):
    print(f'Жизни {hp}, Мана {mp},показатель боевого духа {cp} ')


player(hp=100, mp=100, cp=100)


# функция с произвольными аргументами

def users(**kwargs):
    for key, value in kwargs.items():
        print(f'Welcome {key, value}')


users(
    player1='Den',
    player2='Bob',
    player3='Alyx'
)


# вложенные функции

def armor():
    def gloves():
        defense = 20
        strength = 100
        return defense, strength

    def helmet():
        pass

    def boots():
        pass

    print(gloves())


armor()


# возврат функции

def number(x):
    return x % 2 == 0


for i in range(1, 21):
    if number(i):
        print(i)


# обработка ввода данных пользователем

def age():
    your_age = int(input('Сколько вам лет?  '))

    if your_age > 18:
        print('Добро пожаловать!')
    else:
        print('Закрыто!')


age()

"""Итераторы и декораторы"""


# создание функции-генератора

def user():
    for i in ['Alyx', 'Den', 'Tom', 'Bob']:
        yield i


for i in user():
    print(i)

# создание выражения-генератора

for i in (x * 3 for x in [1, 2, 3, 4, 5]):
    print(i)

# создание итератора

my_list = [1, 2, 3, 4, 5]
itr = iter(my_list)
print(next(itr))


# создание декоратора

def decorator(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


@decorator
def player(name, clas, lvl):
    print(name, clas, lvl)


player('Alyx', 'Paladin', 20)
