"""Работа за преподавателем"""
# Task 1


# class Employee:
#     name = 'Tom'
#     salary = 10000
#
#     def print_info(self):
#         print(
#             'Name: {}\nSalary: {}'.format(self.name, self.salary)
#         )
#
#
# emp_1 = Employee()
# emp_1.print_info()
#
# emp_2 = Employee()
# emp_2.name = 'Bob'
# emp_2.salary = 20000
# emp_2.print_info()

# Task 2


# class Employee:
#
#     def __init__(self, name='Jack', salary=50000):
#         self.name = name
#         self.salary = salary
#
#     def print_info(self):
#         print(
#             'Name: {}\nSalary: {}\n'.format(self.name, self.salary)
#         )
#
#
# emp_1 = Employee('Bob', 10000)
# emp_2 = Employee('Tom', 20000)
#
# emp_1.print_info()
# emp_2.print_info()
#
# emp_3 = Employee()
# emp_3.print_info()

# Task 3

# class Potato:
#     states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}
#
#     def __init__(self, index):
#         self.index = index
#         self.state = 0
#
#     def grow(self):
#         if self.state < 3:
#             self.state += 1
#         self.print_state()
#
#     def is_ripe(self):
#         if self.state == 3:
#             return True
#         return False
#
#     def print_state(self):
#         print('Картошка {} сейчас {}'.format(
#             # self.index, self.states[self.state]
#             self.index, Potato.states[self.state]
#         ))
#
#
# class PotatoGarden:
#
#     def __init__(self, count):
#         self.potatoes = [Potato(index) for index in range(1, count + 1)]
#
#     def grow_all(self):
#         print('Картошка прорастает!')
#         for i_potato in self.potatoes:
#             i_potato.grow()
#
#     def are_all_ripe(self):
#         # for i_potato in self.potatoes:
#         #     if not i_potato.is_ripe():
#         #         print('Картошка еще не созрела!\n')
#         #         break
#         # или
#         if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
#             print('Картошка еще не созрела!\n')
#         else:
#             print('Вся картошка созрела. Можно собирать!\n')
#
#
# my_garden = PotatoGarden(5)
# my_garden.are_all_ripe()
# for _ in range(3):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()

# Home Work
# 1 ==========================================================================
'''Задача 1. Машина 3
Вам предстоит снова немного видоизменить класс Toyota из прошлого урока. На всякий 
случай вот описание класса.
Четыре атрибута:
1.	цвет машины (например, красный),
2.	цена (один миллион),
3.	максимальная скорость (200),
4.	текущая скорость (ноль).
Два метода:
1.	Отображение информации об объекте класса.
2.	Метод, который позволяет устанавливать текущую скорость машины.
Теперь все четыре атрибута должны инициализироваться при создании экземпляра 
класса (то есть передаваться в init). Реализуйте такое изменение класса.
'''

# class Toyota:
#
#     def __init__(self, color='red', price=10 ** 6, max_speed=200, cur_speed=0):
#         self.color = color
#         self.price = price
#         self.max_speed = max_speed
#         self.cur_speed = cur_speed
#
#     def print_info(self):
#         print('Цвет: {}\nЦена: {}\nМаксимальная скорость: {}\nТекущая скорость: {}\n'.format(
#             self.color, self.price, self.max_speed, self.cur_speed
#         ))
#
#     def set_cur_speed(self, cur_speed):
#         self.cur_speed = cur_speed
#
#
# machine_1 = Toyota('Green', 10 ** 7, 300, cur_speed=80)
# machine_1.print_info()
# 2 ==========================================================================
'''Задача 2. Координаты точки
Объект «Точка» на плоскости имеет координаты X и Y. При создании новой точки 
могут передаваться пользовательские значения координат, по умолчанию x = 0, y = 0.
Реализуйте класс, который будет представлять эту точку, и напишите метод, который 
предоставляет информацию о ней. Также внутри класса пропишите счётчик, который 
будет отвечать за количество созданных точек.
Подсказка: счётчик можно объявить внутри самого класса и увеличивать его в 
методе __init__.
'''


# class Dot:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Dot.count += 1  # Тут self.count += 1 - работать не будет! Видимо обращение к статическим атрибутам
#                         # класса д/б именно ч/з имя класса
#
#     def dot_info(self):
#         print('{}-я точка:\n\tкоордината X: {}\n\tкоордината Y: {}'.format(self.count, self.x, self.y))
#
#
# print(Dot.count)
# dot_1 = Dot(1, 1)
# print(dot_1.count)
# dot_1.dot_info()
#
# dot_2 = Dot(2, 2)
# print(dot_2.count)
# dot_2.dot_info()
#
# print(dot_1.count)
# 3 ==========================================================================
'''Задача 3. Весёлая ферма
Для игры «Весёлая ферма» необходимо прописать два класса: класс «Картошка» и 
класс «Грядка картошки».
У картошки есть её номер в грядке, а также стадия зрелости. Она может предоставлять 
информацию о своей зрелости и расти. Всего у картошки может быть четыре стадии 
зрелости.
Грядка с картошкой содержит список картошки, которая на ней растёт, и может, 
собственно, взращивать всю эту картошку, а также предоставлять информацию о 
зрелости всей картошки на своей территории.

Реализуйте оба класса и проверьте их работу: создайте экземпляр грядки из пяти 
картошек и три раза взрастите грядку.

Пример результата (проверка на зрелость и три взращивания):
Картошка ещё не созрела!

Картошка прорастает!
Картошка 1 сейчас Росток
Картошка 2 сейчас Росток
Картошка 3 сейчас Росток
Картошка 4 сейчас Росток
Картошка 5 сейчас Росток
Картошка ещё не созрела!

Картошка прорастает!
Картошка 1 сейчас Зелёная
Картошка 2 сейчас Зелёная
Картошка 3 сейчас Зелёная
Картошка 4 сейчас Зелёная
Картошка 5 сейчас Зелёная
Картошка ещё не созрела!

Картошка прорастает!
Картошка 1 сейчас Зрелая
Картошка 2 сейчас Зрелая
Картошка 3 сейчас Зрелая
Картошка 4 сейчас Зрелая
Картошка 5 сейчас Зрелая
Вся картошка созрела. Можно собирать!
'''


class Potato:
    maturity_states = {0: 'Еще не вылезла', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.cur_stage = 0

    def grow(self):
        if self.cur_stage < 3:
            self.cur_stage += 1
        self.info()

    def maturity_check(self):
        if self.cur_stage == 3:
            return True
        return False

    def info(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.maturity_states[self.cur_stage]))


class PotatoGarden:

    def __init__(self, count):
        self.potato_list = [Potato(index) for index in range(1, count+1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potato_list:
            i_potato.grow()
        self.maturity_info()

    def maturity_info(self):
        if all([i_potato.maturity_check() for i_potato in self.potato_list]):
            print('Вся картошка созрела. Можно собирать!')
        else:
            print('Картошка ещё не созрела!\n')


garden_1 = PotatoGarden(5)
garden_1.maturity_info()
for _ in range(3):
    garden_1.grow_all()
