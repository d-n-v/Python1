# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:

    def __init__(self, groups_list, lessons_list):
        self.groups_list = groups_list
        self.lessons_list = lessons_list

    def school_groups(self):
        print(self.groups_list)


class Group(School):

    def __init__(self, pupils):
        self.pupils = pupils

    def pupils_list(self):
        print(Group.pupils)

    def teachers_list(self):
        pass
#
#
# class Pupil(Group):
#
#     def lessons_list(self):
#         pass
#
#     def parents_names(self):
#         pass
#
#
# class Teacher(School):
#
#     def __init__(self, teacher_name):
#         self.teacher_name = teacher_name
#
#
# class Lesson(School):
#
#     def __init__(self, lesson_name):
#         self.lesson_name = lesson_name


s = School({"5а", "6б", "7в"}, ["Математика", "Физкультура", "Музыка"])
s.school_groups()

