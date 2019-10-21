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


class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, lesson: str, name):
        self.lesson = lesson
        super().__init__(name)


class Group:
    def __init__(self, name):
        self.name = name
        self._teachers = []

    def add_teacher(self, teacher: Teacher):
        self._teachers.append(teacher)

    def get_lessons(self):
        return {x.lesson for x in self._teachers}

    def get_teachers(self):
        return self._teachers


class Pupil(Person):
    def __init__(self, group: Group, name, father: Person = None, mother: Person = None):
        self.group = group
        self.father = father
        self.mother = mother
        super().__init__(name)

    def get_name(self):
        return self.name

    def get_lessons(self):
        return self.group.get_lessons()

    def get_parents(self):
        return self.father, self.mother


class School:
    def __init__(self):
        self.pupils = set()

    def add_pupil(self, pupil: Pupil):
        self.pupils.add(pupil)

    def get_groups(self):
        return {x.group for x in self.pupils}

    def get_group_pupils(self, group: Group):
        return {x for x in self.pupils if x.group == group}


if __name__ == '__main__':
    chem_teacher = Teacher("Химия", "Менделеев")
    math_teacher = Teacher("Математика", "Архимед")
    phys_teacher = Teacher("Физкультура", "Петр Василич")

    group_5a = Group("5a")
    group_5a.add_teacher(chem_teacher)
    group_5a.add_teacher(math_teacher)

    group_11b = Group("11b")
    group_11b.add_teacher(phys_teacher)

    pupil1 = Pupil(group_5a, "Петров", "П", "М")
    pupil2 = Pupil(group_5a, "Иванова", "П1", "М1")
    pupil3 = Pupil(group_11b, "Сергеев", "П2", "М2")
    pupil4 = Pupil(group_11b, "Николаева", "П2", "М2")

    school = School()
    school.add_pupil(pupil1)
    school.add_pupil(pupil2)
    school.add_pupil(pupil3)
    school.add_pupil(pupil4)

    for group in school.get_groups():
        print(group.name)

    for pupil in school.get_group_pupils(group_5a):
        print(pupil.get_name())

    for lesson in pupil3.get_lessons():
        print(lesson)

    print(pupil1.get_parents())

    for teacher in group_5a.get_teachers():
        print(teacher.name)








