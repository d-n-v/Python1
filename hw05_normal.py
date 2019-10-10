import os
import sys
from functions_for_normal import *
import functions_for_normal
print("sys.argv = ", sys.argv)

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

do = {
    "help": print_help,
    "chdir": change_dir,
    "cur_dir": cur_dir,
    "del_dir": delete_dir,
    "mkdir": make_dir
}

try:
    functions_for_normal.dir_name = sys.argv[2]
except IndexError:
    functions_for_normal.dir_name = None


try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if key in do:
        do[key]()
    else:
        print("Неверный ключ")
        print("Укажите ключ Help для получения справки")
