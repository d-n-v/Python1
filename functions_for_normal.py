import os
dir_name = ""


def print_help():
    print("1. Перейти в папку chdir <dir_name>")
    print("2. Просмотреть содержимое текущей папки cur_dir ")
    print("3. Удалить папку del_dir <dir_name>")
    print("4. Создать папку mkdir <dir_name>")


def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print("Вы перешли в директорию {}".format(dir_name))
    except IOError:
        print("Такой директории не существует")


def cur_dir():
    print(os.listdir(os.getcwd()))


def delete_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print("Вы удалили директорию {}".format(dir_name))
    except IOError:
        print("Такой директории не существует")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print("Такая директория уже существует")
