"""
ПЕРЕЧИСЛЕНИЕ (неизменяемый словарь)
набор именованных ЭЛЕМЕНТОВ
"""

from enum import Enum, IntEnum, Flag, auto

class Frameworks(Enum):
    """
    хранит значени любого типа
    может содержать одинаковые значения
    """
    LARAVEL = "Laravel"
    DJANGO = "Django"
    EXPRESS = "Express"
    RAILS = "Ruby on Rails"
    RUBY_ON_RAILS = "Ruby on Rails"

    # обычные методы. Вызываются у метода перечисления
    def describe(self):
        return self.name, self.value
    def __str__(self):
        return str(__class__.__name__) + "." + self.name + ": " + self.value

    # статический метод. Вызывается у самого класса перечислений
    @classmethod
    def get_most_popular(cls):
        return cls.LARAVEL


# test
print(Frameworks.DJANGO)
fr = Frameworks.LARAVEL
print(fr)
print(fr == Frameworks.RAILS)
print(Frameworks.RUBY_ON_RAILS == Frameworks.RAILS)

print(Frameworks.DJANGO.describe())
print(str(Frameworks.EXPRESS))
print(Frameworks.get_most_popular())
print('-' * 10)


class Colors(Enum):
    """
    перечисление с целыми числами
    """
    RED = 1
    GREEN = 2
    BLUE = 3
    WHITE = RED + GREEN + BLUE


class Colors_2(Enum):
    """
    если значения не важны - auto() возвращает целое увеличенное на 1
    """
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    WHITE = auto()

# test
print(Colors_2.RED)
print(Colors_2.GREEN)
print(Colors_2.WHITE)
print(Colors_2.RED)

class Colors_3(IntEnum):
    """
    хранит только ЦЕЛОЧИСЛЕННЫЕ значения
    значения преобразуются в целые числа
    следовательно с ними можно производить арифметические операции
    и сравнение с целыми числами
    """
    RED = 1
    GREEN = 2
    BLUE = 3
    WHITE = RED + GREEN + BLUE


# test
print(Colors_3.GREEN)
print(Colors_3.GREEN + 3)
print(Colors_3.GREEN ** Colors_3.BLUE)
print(Colors_3.WHITE == 6)


class Colors_4(Flag):
    """
    базовый класс для перечислений
    элементы хранят целочисленные значения
    значения элементов могут выступать в качестве операндов для двоичных операторов
    ф-ция auto() здесь последовательно выдает степени числа 2 (1, 2, 4, 8, 16 и т.д.)
    """
    BLACK = 0
    RED = auto()        # 1
    GREEN = auto()      # 2
    BLUE = auto()       # 4
    WHITE = RED | GREEN | BLUE  # 7


print(Frameworks['LARAVEL'])    # обращение в стиле СЛОВАРЕЙ (ключ)
print(Frameworks('Laravel'))    # обращение по значению (круглые скобки) - значение
print(Frameworks.RAILS.name, Frameworks.RAILS.value)
# проверка на вхождение
f = Frameworks.DJANGO
print(f in Frameworks)
print(f in Colors)

print(list(Colors))     # итератор
for f in Frameworks: print(f.value, end=' | ')