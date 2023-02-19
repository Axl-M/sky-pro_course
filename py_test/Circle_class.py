import math

class Circle:
    def __init__(self, radius):
        if type(radius) not in [int, float]:
            raise TypeError("Радиус должен быть числом, int или float")
        if radius < 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_diametr(self):
        return self.radius * 2

    def get_perimetr(self):
        return 2 * self.radius * math.pi

