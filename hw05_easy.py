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

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.