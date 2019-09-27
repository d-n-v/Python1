import math
import random
import datetime

def fill_list(list):
    length = int(input("Введите размер списка:"))
    while length > 0:
        list.append(random.randint(-100, 100))
        length -= 1



# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

list_int = [2, 4, 6, -12, 49, 49]
list_int2 = []

for li in list_int:
    if li >= 0 and math.sqrt(li) % 1 == 0:
        list_int2.append(int(math.sqrt(li)))

print(list_int2)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

# date = input("Введите дату дд.мм.гггг")
#
# datetime.strftime(date)



# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

list_random = []

fill_list(list_random)

print(list_random)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

list_items = [16, 15, 20, 20, 300, 300, 1, -7]
list_buffer = []
buffer_dict = {}
list_items_nodupl = []
list_items_unique = []
buffer_value = 0

for li in list_items:
    if li not in list_buffer:
        list_buffer.append(li)
list_items_nodupl = list_buffer
print(list_items_nodupl)


for li1 in list_items:
    if li1 not in buffer_dict.keys():
        buffer_dict[li1] = "1"
    elif li1 in buffer_dict.keys():
        buffer_dict[li1] = int(buffer_dict[li1]) + 1

for li2 in buffer_dict:
    if li2 in buffer_dict.keys() and int(buffer_dict[li2]) == 1:
        list_items_unique.append(li2)
print(list_items_unique)
