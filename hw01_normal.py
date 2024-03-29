__author__ = "Водолаго Дмитрий Николаевич"

#NORMAL
# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

number_int = int((input("Введите целое число: ")))
max_num = 0
while number_int > 0:
    last_number = number_int % 10
    if last_number > max_num:
        max_num = last_number
    number_int = number_int // 10
print("Самая большая цифра числа: ", max_num)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
answer1 = input("Введите первое значение: ")
answer2 = input("Введите второе значение: ")
print("Вы ввели: ", "answer1= ", answer1, "и ", "answer2= ", answer2)
answer1, answer2 = answer2, answer1
print("Если поменять их местами, получим:", answer1, answer2)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a = float(input("Введите значение a"))
b = float(input("Введите значение b"))
c = float(input("Введите значение c"))
d = b ** 2 - 4 * a * c

print("Ваше уравнение:", a, "x²", "+", b, "x", "+", c, "=", "0")
print("Дискриминант =", d)


if a == 0:
    print("Используйте другую программу для решения линейных уравнений")

elif d > 0:
    x1 = (-b + math.sqrt(d)) / (a * 2)
    x2 = (-b - math.sqrt(d)) / (a * 2)
    print("x1 =", x1, "x2 =", x2)
elif d == 0:
    x = -b / (2 * a)
    print("x =", x)
else:
    print("Корней нет")
