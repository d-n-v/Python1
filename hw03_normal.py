from math import sqrt
import copy


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
# def fib():
#     a, b = 1, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# def fibonacci(n, m):
#     for index, fibonacci_number in zip(range(n, m), fib()):
#         return '{i:3}: {f:3}'.format(i=index, f=fibonacci_number)
#
#
# print(fibonacci(1, 10))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    changed = True
    while changed:
        changed = False
        for i in range(len(origin_list) - 1):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
                changed = True


list_sorted = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(list_sorted)
print(list_sorted)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def func(x):
    if x > 0:
        return True
    else:
        return False


def own_filter(function, iterable):
    for i in iterable:
        result = []
        if function(i):
            result.append(i)
    return result


list_to_filter = [-2, -1, 0, 1]
res = own_filter(func, list_to_filter)
print(res)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# a = (1, 3)
# b = (4, 7)
# c = (2, 8)
# d = (-1, 4)
#
# ab = sqrt((a[0] - b[1]) ** 2 + (b[0] - b[1]) ** 2)
# dc = sqrt((a[0] - 1) ** 2 + (b[0] - b[1]) ** 2)
# ad = sqrt((a[0] - 1) ** 2 + (b[0] - b[1]) ** 2)
# bc = sqrt((a[0] - 1) ** 2 + (b[0] - b[1]) ** 2)
