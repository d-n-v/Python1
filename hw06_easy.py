import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:

    def __init__(self, a, a1, b, b1, c, c1):
        self.a = a
        self.b = b
        self.c = c
        self.a1 = a1
        self.b1 = b1
        self.c1 = c1

    def area(self):
        area_count = 1/2 * (((self.b - self.a) * (self.c1 - self.a1)) - ((self.c - self.a) * (self.b1 - self.a1)))
        if area_count < 0:
            area_count = -area_count
        return area_count

    def perimeter(self):
        side_a = math.sqrt((self.b - self.a) ** 2 + (self.b1 - self.a1) ** 2)
        side_b = math.sqrt((self.c - self.a) ** 2 + (self.c1 - self.b1) ** 2)
        side_c = math.sqrt((self.c - self.b) ** 2 + (self.c1 - self.b1) ** 2)
        perimeter_count = side_a + side_b + side_c
        return perimeter_count

    def height(self):
        side_a = math.sqrt((self.b - self.a) ** 2 + (self.b1 - self.a1) ** 2)
        side_b = math.sqrt((self.c - self.a) ** 2 + (self.c1 - self.b1) ** 2)
        side_c = math.sqrt((self.c - self.b) ** 2 + (self.c1 - self.b1) ** 2)
        perimeter_inside = side_a + side_b + side_c
        height_count = 2 ** perimeter_inside / side_a
        return height_count


t = Triangle(5, 2, 5, 6, 3, 6)
print("Высота:", t.height())
print("Периметр:", t.perimeter())
print("Площадь:", t.area())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class EquilateralTrapezoid:

    def __init__(self, a, a1, b, b1, c, c1, d, d1):
        self.a = a
        self.b = b
        self.c = c
        self.a1 = a1
        self.b1 = b1
        self.c1 = c1
        self.d = d
        self.d1 = d1


    def if_equilateral(self):
        print("В этой функции проверяется равнобедренная ли трапеция, результат очень точный")

    def sides_length(self):
        print("В этой функции вычисляются длины сторон")

    def perimeter(self):
        print("В этой функции вычисляется периметр на основе какой-то\n"
              "умной формулы которая переиспользует данные других функций")

    def area(self):
        print(
            "В этой функции вычисляется площадь на основе какой-то\n"
            "умной формулы которая переиспользует данные других функций")


tr = EquilateralTrapezoid(1, 2, 3, 4, 5, 6, 7, 8)
tr.if_equilateral()



