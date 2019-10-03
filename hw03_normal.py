from math import sqrt


#1
def fibonacci(n, m):
    i = 1
    fn = 0
    f = 1

    while i <= m:
        if i >= n:
            print(f)
        f += fn
        fn = f - fn
        i += 1


#2
def sort_to_max(origin_list):
    changed = True
    while changed:
        changed = False
        for i in range(len(origin_list) - 1):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
                changed = True


#3
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


#4
def par(a1, b1, c1, d1):
    a = sqrt((b1[0] - a1[0]) ** 2 + (b1[1] - a1[1]) ** 2)

    b = sqrt((c1[0] - d1[0]) ** 2 + (c1[1] - d1[1]) ** 2)

    c = sqrt((d1[0] - a1[0]) ** 2 + (d1[1] - a1[1]) ** 2)

    d = sqrt((c1[0] - b1[0]) ** 2 + (c1[1] - b1[1]) ** 2)
    if a == b and c == d:
        return "Это параллелограм"
    else:
        return "Это не параллелограм"

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


fibonacci(1, 7)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# list_sorted = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
# sort_to_max(list_sorted)
# print(list_sorted)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# list_to_filter = [-2, -1, 0, 1]
# res = own_filter(func, list_to_filter)
# print(res)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# a_var = [1, 3]
# b_var = [4, 7]
# c_var = [2, 8]
# d_var = [-1, 4]
#
# print(par(a_var, b_var, c_var, d_var))
