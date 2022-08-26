# Home Work
# 1 ==========================================================================
'''Задача 1. Драка
Вы работаете в команде разработчиков мобильной игры, и вам досталась вот такая 
часть от ТЗ заказчика:
Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье 
в 100 очков. Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровья 
не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара. 
После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у 
противника осталось здоровья. Как только у кого-то заканчивается ресурс здоровья, 
программа завершается сообщением о том, кто одержал победу.
Реализуйте такую программу.
'''
# Пропустил
# 2 ==========================================================================
'''Задача 2. Студенты
Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», 
«Успеваемость» (список из пяти элементов). Затем создайте список из десяти 
студентов и отсортируйте его по возрастанию среднего балла. Выведите результат 
на экран.
'''
# Пропустил
# 3 ==========================================================================
'''Задача 3. Окружность
На координатной плоскости рисуются окружности, у каждой окружности следующие 
параметры: координаты X и Y центра окружности и значение R ― это радиус окружности. 
По умолчанию центр находится в (0, 0), а радиус равен 1.

Реализуйте класс «Окружность», который инициализируется по этим параметрам. 
Круг также может:
1.	Находить и возвращать свою площадь.
2.	Находить и возвращать свой периметр.
3.	Увеличиваться в K раз.
4.	Определять, пересекается ли он с другой окружностью.
'''
# Пропустил
# 4 ==========================================================================
'''Задача 4. Отцы, матери и дети
Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
1.	Имя.
2.	Возраст.
3.	Список детей.
И он может:
1.	Сообщить информацию о себе.
2.	Успокоить ребёнка.
3.	Покормить ребёнка.

У ребёнка есть:
1.	Имя.
2.	Возраст (должен быть меньше возраста родителя хотя бы на 16 лет).
3.	Состояние спокойствия.
4.	Состояние голода.
Реализация состояний на ваше усмотрение! Это может быть и простой «флаг», и 
словарь состояний, и что-нибудь ещё интереснее!
'''
# Пропустил
# 5 ==========================================================================
'''Задача 5. Весёлая ферма 2
Мы продолжаем писать игру «Весёлая ферма» и теперь необходимо её немного 
модернизировать. Всё-таки кому-то же нужно собирать урожай, и для этого нам 
понадобится садовник, который имеет:
1.	Имя.
2.	Грядку с растением, за которым он ухаживает (в нашем случае пока только грядка 
с картошкой).

И может: 
1.	Ухаживать за грядкой.
2.	Собирать с неё урожай (количество картошки ― пустой список).

Модернизируйте программу, используя новый класс «Садовник». На всякий случай вот 
описание картошки и грядки:
У картошки есть её номер в грядке, а также стадия зрелости. Она может предоставлять 
информацию о своей зрелости и расти. Всего у картошки может быть четыре стадии 
зрелости.
Грядка с картошкой содержит список картошки, которая на ней растёт, и может, 
собственно, взращивать всю эту картошку, а также предоставлять информацию о 
зрелости всей картошки на своей территории.

Проверьте работу программы, создав грядку из пяти картошек и отдав эту грядку 
садовнику. Пусть поухаживает за грядкой и соберёт урожай (а, может быть, даже и 
не один).
'''

# class Gardener:
#     harvesting_count = {}
#
#     def __init__(self, name, garden_count=1, potato_count=5):
#         self.name = name
#         self.potato_count = potato_count
#         self.gardens = [PotatoGarden(index, potato_count) for index in range(1, garden_count + 1)]
#         Gardener.harvesting_count[self.name] = []
#
#     def garden_care(self):  # Уход за грядкой
#         for index, i_garden in enumerate(self.gardens):  # Идем по экземплярам грядки
#             print(f'Садовник {self.name} выращивает {index+1} грядку:')
#             for _ in range(3):  # Выращиваем картошку на грядке до зрелости
#                 i_garden.grow_all()
#                 i_garden.are_all_ripe()
#             Gardener.harvesting_count[self.name].append(self.potato_count)
#
#     def harvesting(self):   # Сбор урожая
#         print('Садовник {} посадил {} грядки по {} клубня в каждой. Урожай составил {} клубней.\n'.format(
#             self.name, len(Gardener.harvesting_count[self.name]),
#             self.potato_count, sum(Gardener.harvesting_count[self.name])
#         ))
#
#
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
#         print('\tКартошка {} сейчас {}'.format(
#             self.index, Potato.states[self.state]
#         ))
#
#
# class PotatoGarden:
#
#     def __init__(self, garden_index, count):
#         self.garden_index = garden_index
#         self.potatoes = [Potato(index) for index in range(1, count + 1)]
#
#     def grow_all(self):
#         print('\tКартошка прорастает!')
#         for i_potato in self.potatoes:
#             i_potato.grow()
#
#     def are_all_ripe(self):
#         if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
#             print('\tКартошка еще не созрела!\n')
#         else:
#             print('\tВся картошка созрела. Можно собирать!\n')
#
#
# gardener_1 = Gardener('Махмуд', 2, 3)
# gardener_1.garden_care()
#
# gardener_2 = Gardener('Вася', 3, 2)
# gardener_2.garden_care()
#
# gardener_1.harvesting()
# gardener_2.harvesting()
# 6 ==========================================================================
'''Задача 6. Магия (!)
Для одной игры необходимо реализовать механику магии, где при соединении двух 
элементов получается новый. У нас есть четыре базовых элемента: «Вода», «Воздух», 
«Огонь», «Земля». Из них как раз и получаются новые: «Шторм», «Пар», «Грязь», 
«Молния», «Пыль», «Лава».

Вот таблица преобразований:
  Вода + Воздух = Шторм
  Вода + Огонь = Пар
  Вода + Земля = Грязь
  Воздух + Огонь = Молния
  Воздух + Земля = Пыль
  Огонь + Земля = Лава

Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо 
организовать как отдельный класс. Если результат не определён, то возвращается None.

Примечание: сложение объектов можно реализовывать через магический метод __add__, 
вот пример использования:
class Example_1:
    def __add__(self, other):
        return Example_2()

class Example_2:
    answer = 'сложили два класса и вывели'

a = Example_1()
b = Example_2()
c = a + b
print(c.answer)

Дополнительно: придумайте свой элемент (или элементы), а также реализуйте его 
взаимодействие с остальными элементами.
'''


# class Water:
#     def __str__(self):
#         return 'Вода'
#
#     def __add__(self, other):
#         if isinstance(other, Air):
#             return Storm()
#         elif isinstance(other, Fire):
#             return Vapor()
#         elif isinstance(other, Earth):
#             return Dirt()
#         else:
#             return None
#
#
# class Air:
#     def __str__(self):
#         return 'Воздух'
#
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Lightning()
#         elif isinstance(other, Earth):
#             return Dust()
#         else:
#             return None
#
#
# class Fire:
#     def __str__(self):
#         return 'Огонь'
#
#     def __add__(self, other):
#         if isinstance(other, Earth):
#             return Lava()
#         else:
#             return None
#
#
# class Earth:
#     def __str__(self):
#         return 'Земля'
#
#
# class Storm:
#     def __str__(self):
#         return 'Шторм'
#
#
# class Vapor:
#     def __str__(self):
#         return 'Пар'
#
#
# class Dirt:
#     def __str__(self):
#         return 'Грязь'
#
#
# class Lightning:
#     def __str__(self):
#         return 'Молния'
#
#
# class Dust:
#     def __str__(self):
#         return 'Пыль'
#
#
# class Lava:
#     def __str__(self):
#         return 'Лава'
#
#
# water = Water()
# air = Air()
# fire = Fire()
# earth = Earth()
# print(water + air, water + fire, water + earth)
# print(air + fire, air + earth)
# print(fire + earth)
# 7 ==========================================================================
'''Задача 7. Совместное проживание
Для того чтобы понять, стоит ли Артёму жить с кем-то или всё же остаться в гордом 
одиночестве, он решил провести довольно необычное исследование. Для этого он 
реализовал модель человека и модель дома.
Человек может:
1.	Есть (+ сытость, − еда).
2.	Работать (− сытость, + деньги).
3.	Играть (− сытость).
4.	Ходить в магазин за едой (+ еда, − деньги).
У человека есть имя, степень сытости (изначально 50) и дом.
В доме есть холодильник с едой (изначально 50 еды) и тумбочка с деньгами 
(изначально 0 денег).
Если сытость человека становится меньше нуля, то человек умирает.
Логика действий человека определяется следующим образом:
1.	Генерируется число кубика от 1 до 6.
2.	Если сытость < 20, то поесть.
3.	Иначе, если еды в доме < 10, то сходить в магазин.
4.	Иначе, если денег в доме < 50, то работать.
5.	Иначе, если кубик равен 1, то работать.
6.	Иначе, если кубик равен 2, то поесть.
7.	Иначе играть.

По такой логике эксперимента человеку надо прожить 365 дней.

Реализуйте такую программу и создайте двух людей, живущих в одном доме. 
Проверьте работу программы несколько раз. Надеемся, эти люди живы...
'''
# Пропустил
# 8 ==========================================================================
'''Задача 8. Блек-джек
Костя так и не смог завязать с азартными играми. Но перед тем, как в очередной 
раз всё проиграть, он решил как следует подготовиться. И написать программу, на 
которой он будет тренироваться играть в блек-джек.
Блек-джек также известен как 21. Суть игры проста: либо набрать ровно 21 очко, 
либо набрать очков больше, чем в руках у дилера, но ни в коем случае не больше 21. 
Если игрок собирает больше 21, он «сгорает». В случае ничьей игрок и дилер остаются 
при своих.

Карты имеют такие «ценовые» значения:
•	от двойки до десятки — от 2 до 10 соответственно,
•	у туза — 1 или 11 (11, пока общая сумма не больше 21, далее 1),
•	у «картинок» (король, дама, валет) — 10.

Напишите программу, которая в начале случайным образом выдаёт пользователю и 
компьютеру по две карты и затем запрашивает у пользователя действие: взять карту 
или остановиться. На экран должна выдаваться информация о руке пользователя. 
После того как игрок останавливается, выведите на экран победителя.
Представление карты реализуйте с помощью класса.

Дополнительно: сделайте так, чтобы карты не могли повторяться.
'''
# Пропустил
# 9 ==========================================================================
'''Задача 9. Крестики-нолики (необязательная)
Напишите программу, которая реализует игру «Крестики-нолики». Да, это всё 
условие задачи. 
'''


def main(num, player_name_1, player_name_2):    # Основная функция программы
    if num == 0:
        print('Итак, играем!')
    else:
        print('Отлично, продолжаем!')
    desk_instance = create_desk_instances(num)
    desk_instance.desk_info()
    first_player = priority(num, player_name_1, player_name_2)
    player_instances = create_player_instances(player_name_1, player_name_2, first_player)
    switch_players(desk_instance, first_player, player_instances[0], player_instances[1])


def switch_players(some_desk, flag, player_1, player_2):    # Переключение игроков между ходами
    while len(some_desk.positions) != 0:
        if flag == 1:
            player_1.choice(some_desk)
            flag = 2
        else:
            player_2.choice(some_desk)
            flag = 1
        if len(some_desk.positions) <= 7:
            if stop_game(flag, player_1, player_2, some_desk):
                break
    else:
        some_desk.print_desk()
        print('=' * 50)
        print('У вас ничья!', end=' ')


def stop_game(flag, player_1, player_2, some_desk):     # Остановка игры в случае выигрыша какого либо игрока
    if some_desk.check_win():
        some_desk.print_desk()
        print('='*50)
        if flag == 2:
            print('\tСтоп Игра! Игрок {} - выиграл!'.format(player_1.name))
            Desk.number_of_wins_1 += 1
        else:
            print('\tСтоп Игра! Игрок {} - выиграл!'.format(player_2.name))
            Desk.number_of_wins_2 += 1
        print('-' * 50)
        print('\tКоличество побед игрока {}: {}'.format(player_1.name, Desk.number_of_wins_1))
        print('\tКоличество побед игрока {}: {}'.format(player_2.name, Desk.number_of_wins_2))
        print('=' * 50)
        return True
    return False


def repeat(cnt, name_1, name_2):    # Функция отвечающая за повтор игры сначала
    if cnt != 0:
        action = int(input('Играем еще раз? (1-Да, 0-Нет): '))
        print('=' * 50)
        while action not in [0, 1]:
            action = int(input('Неверный выбор, доступны варианты (1-Да, 0-Нет): '))
        if action:
            main(cnt, name_1, name_2)
            return False
        else:
            print('Тогда до скорых встреч! Возвращайтесь скорее :)')
            return True
    else:
        main(cnt, name_1, name_2)
        return False


def priority(num, name_1, name_2):  # Функция в которая возвращает, кто ходит первым
    if num == 0:
        is_first = int(input(f'Кто будет ходить первым? (1-{name_1}, 2-{name_2}): '))
    else:
        is_first = int(input(f'Кто первый на этот раз? (1-{name_1}, 2-{name_2}): '))
    if is_first not in [1, 2]:
        print('Нет игрока с таким номером! Попробуйте еще раз.')
        is_first = priority(num, name_1, name_2)
    return is_first


def create_player_instances(name_1, name_2, first):     # Создание экземпляров игроков класса player
    sign_choice = int(input('Что выбираете X или 0? (1-крестик, 2-нолик): '))
    while sign_choice not in [0, 1]:
        sign_choice = int(input('Внимательней! Выбрать можно только (1-крестик, 2-нолик): '))
    if first == 1 and sign_choice == 1:
        player_1 = Player('X', name_1)
        player_2 = Player('0', name_2)
        print(f'Значит игроку {name_2} достается нолик :)')
    elif first == 1 and sign_choice == 2:
        player_1 = Player('0', name_1)
        player_2 = Player('X', name_2)
        print(f'Значит игроку {name_2} достается крестик :)')
    elif first == 2 and sign_choice == 1:
        player_1 = Player('0', name_1)
        player_2 = Player('X', name_2)
        print(f'Значит игроку {name_1} достается нолик :)')
    else:  # first == 2 and sign_choice == '0'
        player_1 = Player('X', name_1)
        player_2 = Player('0', name_2)
        print(f'Значит игроку {name_1} достается крестик :)')
    return player_1, player_2


def create_desk_instances(num):     # Создание экземпляра доски для очередной игры
    board = Desk(num)
    return board


class Desk:
    """Класс описывающий игровую доску"""

    number_of_wins_1 = 0
    number_of_wins_2 = 0

    win_positions_list = [[1, 3, 5], [9, 11, 13], [17, 19, 21],
                          [1, 9, 17], [3, 11, 19], [5, 13, 21],
                          [1, 11, 21], [5, 11, 17]]

    start_desk = ['\t ', 1, ' | ', 2, ' | ', 3, '\n',
                  '\t-----------\n',
                  '\t ', 4, ' | ', 5, ' | ', 6, '\n',
                  '\t-----------\n',
                  '\t ', 7, ' | ', 8, ' | ', 9, '\n']

    def __init__(self, number):
        self.number = number
        self.positions = {'1': 1, '2': 3, '3': 5, '4': 9, '5': 11, '6': 13, '7': 17, '8': 19, '9': 21}

        self.desk = ['\t ', ' ', ' | ', ' ', ' | ', ' ', '\n',
                     '\t-----------\n',
                     '\t ', ' ', ' | ', ' ', ' | ', ' ', '\n',
                     '\t-----------\n',
                     '\t ', ' ', ' | ', ' ', ' | ', ' ', '\n']

    def desk_info(self):
        print('Карта доступных ходов:')
        for i in range(len(self.start_desk) - 1):
            print(self.start_desk[i], end='')
        print()

    def print_desk(self):
        for i in range(len(self.desk) - 1):
            print(self.desk[i], end='')
        print()

    def update_desk(self, position, sign):
        del self.desk[self.positions[position]]
        self.desk.insert(self.positions[position], sign)
        del self.positions[position]

    def check_win(self):
        for i_sign in self.win_positions_list:
            if all(self.desk[j_elem] == 'X' for j_elem in i_sign) or all(self.desk[j_elem] == '0' for j_elem in i_sign):
                # или if not [j_elem for j_elem in i_sign if self.desk[j_elem] != 'X']:
                return True
        return False


class Player:
    """Это класс описывающий игрока"""

    def __init__(self, sign, name):
        self.sign = sign
        self.name = name

    def check_choice(self, cell_num, desk_ins):
        if cell_num not in desk_ins.positions.keys():
            print('Неверный ход! Попробуйте еще раз.')
            self.choice(desk_ins)
        else:
            desk_ins.update_desk(cell_num, self.sign)

    def choice(self, desk_ins):
        desk_ins.print_desk()
        cell_number = input('Ходит - {} (выберите номер клетки): '.format(self.name))
        self.check_choice(cell_number, desk_ins)


count = 0
pl_name_1 = input('Введите имя 1-го игрока: ')
pl_name_2 = input('Введите имя 2-го игрока: ')
while True:
    stop = repeat(count, pl_name_1, pl_name_2)
    if stop:
        input('\nНажмите enter для выхода...')
        break
    count += 1
