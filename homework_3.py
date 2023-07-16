import logging
import random
from enum import Enum


# создание класса и объекта (корзина покупок)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, new):
        self.items.append(new)

    def remove_item(self, remove):
        self.items.remove(remove)

    def total_price(self):
        total = 0
        for i in self.items:
            total += i.price

        return total

    def empty(self):
        return len(self.items) == 0


item = Item('GEFORSE', 99999)
item1 = Item('RTX', 9000)
shopping_cart = ShoppingCart()
shopping_cart.add_item(item)
shopping_cart.add_item(item1)
print(shopping_cart.total_price())


# реализация класса, содержащего методы разных типов
# (метод экземпляра, метод класса, статический метод)

class Object:
    HP = 100
    MP = 100

    @classmethod
    def classmethod(cls):
        print('Я метод класса')
        return cls.HP, cls.MP

    def instancemetod(self):
        print('Я метод экземпляра класса')

    @staticmethod
    def staticmethod():
        print('Я статический метод')


player = Object()
player.instancemetod()
Object.classmethod()
Object.staticmethod()


# реализация иерархии наследования на примере геометрических фигур
# реализация полиморфизма

class Shape:

    def __init__(self, x_pos, y_pos, ):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self):
        raise NotImplementedError('не найден draw')


class Square(Shape):
    def __init__(self, x_pos, y_pos, x):
        super().__init__(x_pos, y_pos)
        self.x = x

    def draw(self):
        return 4 * self.x


class Rectangle(Shape):
    def __init__(self, x_pos, y_pos, w, h):
        super().__init__(x_pos, y_pos)
        self.w = w
        self.h = h

    def draw(self):
        return 2 * (self.w, self.h)


class Triangle(Shape):
    def __init__(self, x_pos, y_pos, a, b, c):
        super().__init__(x_pos, y_pos)
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        return self.a + self.b + self.c


geom = [
    Square(50, 50, 10),
    Rectangle(20, 20, 5, 10),
    Triangle(70, 70, 15, 15, 15)
]

for i in geom:
    print(i.draw())


# реализация инкапсуляции

class Incapsulate:
    def __init__(self):
        self.__variable = 'Инкапсулированная переменная'

    def set_var(self, value):
        print(self.__variable)
        self.__variable = value

    def get_var(self):
        return self.__variable


incapsulate = Incapsulate()
incapsulate.set_var('Меня изменили')
print(incapsulate.get_var())
try:
    incapsulate.__variable
except Exception as e:
    print('Ошибка: попытка изменения приватной переменной. Пользуйтесь инкапсуляцией set_var / get_var', e)


########################################################################### Угадай Число
class DifficultLevel(Enum):
    EASY = 0
    NORMAL = 1
    HARD = 2


def generate_number(minMax: []) -> int:
    return random.randint(minMax[0], minMax[1])


def retry() -> int:
    print("Ещё одну игру (y/n)?: ", end="")
    one_more_game = input()
    if one_more_game == 'y':
        return 0
    elif one_more_game == 'n':
        return 1
    else:
        print("Ожидался ввод y или n, вы ввели: ", one_more_game, ". Игра начнётся с установки сложности.")
        return 2


class Game:

    def __init__(self):
        self.required_number = 0
        self.attempts = 0
        self.range = [0, 9]
        self.difficult_level = 0

    def set_difficult_level_to(self, new_level: DifficultLevel):
        self.difficult_level = new_level
        if new_level == DifficultLevel.EASY:
            self.range = [0, 9]
            self.refresh(3, generate_number(self.range))
        elif new_level == DifficultLevel.NORMAL:
            self.range = [0, 50]
            self.refresh(4, generate_number(self.range))
        elif new_level == DifficultLevel.HARD:
            self.range = [0, 99]
            self.refresh(5, generate_number(self.range))

        print("Уровень сложности установлена на: ", self.difficult_level.name)
        print("У вас будет {} попыток, мин. и макс. число будет в пределах {}".format(self.attempts, self.range))
        print("Удачи!")

    def refresh(self, new_attempts, new_required_number):
        self.attempts = new_attempts
        self.required_number = new_required_number

    def start(self):
        print("Выбор сложности:")
        print("[0] Лёгкий")
        print("[1] Нормальный")
        print("[2] Тяжёлый")

        new_level = None
        try:
            result = int(input())
            logging.info(result)
            if result == DifficultLevel.HARD.value:
                new_level = DifficultLevel.HARD
            elif result == DifficultLevel.NORMAL.value:
                new_level = DifficultLevel.NORMAL
            elif result == DifficultLevel.EASY.value:
                new_level = DifficultLevel.EASY
            else:
                raise ValueError("Неверный ввод.")
        except ValueError as e:
            print("Ввод должен быть от 0 до 2, вы совершили ошибку, попробуйте ещё раз.")
            self.start()
        except Exception as e:
            logging.exception(e)
            self.start()

        self.set_difficult_level_to(new_level)

        while True:
            try:
                print("Введите число: ", end="")
                number = int(input())
            except ValueError as e:
                print(
                    "Ошибка в ведённом значении. Для вводы допускаются только цифры в диапазоне: {}".format(self.range))
                continue

            if number == self.required_number:
                print("Поздравляю! Вы угадали загаданное число!")
                retry_type = retry()
                if retry_type == 0:
                    self.refresh(self.attempts, generate_number(self.range))
                    continue
                elif retry_type == 1:
                    break
                elif retry_type == 2:
                    self.start()
            else:
                diff = number - self.required_number
                print("Вы не угадали! Нужно {}!"
                      .format("больше" if diff < 0 else "меньше"))
                self.attempts -= 1
                if self.attempts <= 0:
                    print("К сожалению вы не справились и попыток не осталось =(, удачи в следующий раз!")
                    self.start()
                else:
                    print("У вас осталось: {} попыток.".format(self.attempts))


game = Game()
game.start()
