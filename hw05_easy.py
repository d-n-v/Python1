import os


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

dir_path = os.path.join(os.getcwd(), 'dir')
for i in range(1, 10):
    try:
        os.mkdir('{}{}{}'.format(dir_path, '_', i))
    except FileExistsError:
        print("Такая директория уже существует")

dir_path = os.path.join(os.getcwd(), 'dir')
for i in range(1, 10):
    try:
        os.rmdir('{}{}{}'.format(dir_path, '_', i))
    except FileNotFoundError or OSError:
        print("Невозможно удалить папку. Возможно, она не пустая")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

allfiles_list = os.listdir(os.getcwd())
current_dirs_list = []


def finddirs(list1, list2):
    for i in list1:
        if os.path.isdir(i):
            list2.append(i)


finddirs(allfiles_list, current_dirs_list)
print(current_dirs_list)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

