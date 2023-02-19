import math


def double(value):
    new_value = value * 2
    return new_value

def get_circle_square(radius):
    if type(radius) not in [int, float]:
        raise TypeError('Должно быть int или float и быть больше 0')
    if radius < 0:
        raise ValueError('Должно быть int или float и быть больше 0')
    return radius ** 2 * math.pi

def get_verbal_grade(grade):
    if type(grade) != int: raise TypeError("Должно быть целое между 2 и 5")
    if grade < 2 or grade > 5: raise ValueError("Должно быть между 2 и 5")
    if grade == 2: return "Плохо"
    elif grade == 3: return "Удовлетворительно"
    elif grade == 4: return "Хорошо"
    elif grade == 5: return "Отлично"