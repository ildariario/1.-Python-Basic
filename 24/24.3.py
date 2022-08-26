"""Работа за преподавателем"""
# Task 1


# class User:
#     user_name = 'Admin'
#     password = 'qwerty'
#     is_banned = False
#     friends = []
#
#     def print_info(self):
#         print(
#             'Name: {}\nPassword: {}\nBan status: {}'.format(
#                 self.user_name, self.password, self.is_banned)
#         )
#
#     def add_friend(self, friend):
#         self.friends.append(friend)
#
#
# user_1 = User()
# user_1.print_info()
#
# user_1.add_friend('Bob')
# print(user_1.friends)

# Task 2

# class User:
#     user_name = 'Admin'
#     password = 'qwerty'
#     is_banned = False
#     friends = []
#
#     def print_info(self):
#         print(
#             'Name: {}\nPassword: {}\nBan status: {}'.format(
#                 self.user_name, self.password, self.is_banned)
#         )
#
#     def add_friend(self, friend):
#         if isinstance(friend, User):
#             self.friends.append(friend.user_name)
#         else:
#             self.friends.append(friend)
#
#
# user_1 = User()
# user_2 = User()
# user_2.user_name = 'Alina'
#
# print(user_1.user_name, user_2.user_name)
#
# user_1.add_friend('Bob')
# user_1.add_friend(user_2)
#
# print(user_1.friends, user_2.friends)   # При добавлении друга 'Bob' для 1-го юзера он добавится
#                                         # в список frends кот. явл-ся статич-им атрибутом класса
#                                         # User. Поэтому этот список friends будет распространяться
#                                         # и на все другие экземпляры класса User, т.е. и у 2-го
#                                         # пользователя будет тот же список друзей.
# print(id(User))
# print(id(user_1))
# print(id(user_2))
# print(id(user_1.friends))
# print(id(user_2.friends))

# Task 3

# class User:
#     user_name = 'Admin'
#     password = 'qwerty'
#     is_banned = False
#     friends = []
#
#     def print_info(self):
#         print(
#             'Name: {}\nPassword: {}\nBan status: {}\nFriends: {}\n'.format(
#                 self.user_name, self.password, self.is_banned, self.friends)
#         )
#
#     def add_friend(self, friend):
#         if isinstance(friend, User):
#             self.friends.append(friend.user_name)
#         else:
#             self.friends.append(friend)
#
#
# user_1 = User()
# user_2 = User()
# user_2.user_name = 'Alina'
# user_3 = User()
# user_3.user_name = 'Gosha'
#
# user_1.print_info()
#
# user_1.friends = []
# user_1.add_friend(user_2)
#
# user_2.friends = []
# user_2.add_friend('Masha')
#
# user_3.add_friend('Bob')
#
# user_1.print_info()
# user_2.print_info()
# user_3.print_info()
#
# print(id(User))
# print(id(user_1))
# print(id(user_2))
# print(id(user_1.friends))
# print(id(user_2.friends))

# Task 4

# class Family:
#     surname = 'Common family'
#     money = 10 ** 5
#     have_a_house = False
#
#     def info(self):
#         print(
#             'Family name: {}\nFamily funds: {}\nHaving a house: {}\n'.format(
#                 self.surname, self.money, self.have_a_house
#             )
#         )
#
#     def earn_money(self, amount):
#         self.money += amount
#         print('Earned {} money! Current value: {}'.format(amount, self.money))
#
#     def buy_house(self, house_price, discount=0):
#         house_price -= house_price * discount / 100
#         if self.money >= house_price:
#             self.money -= house_price
#             self.have_a_house = True
#             print('House purchased! Current money: {}\n'.format(self.money))
#         else:
#             print('Not enough money!\n')
#
#
# my_family = Family()
# my_family.info()
#
# print('Try to buy a house')
# my_family.buy_house(10 ** 6)
#
# if not my_family.have_a_house:
#     my_family.earn_money(800000)
#     print('Try to buy a house again')
#     my_family.buy_house(10 ** 6, 10)
#
# my_family.info()

# Home Work
# 1 ==========================================================================
'''Задача 1. Машина 2
Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
•	цвет машины (например, красный),
•	цена (один миллион),
•	максимальная скорость (200),
•	текущая скорость (ноль).

Добавьте два метода класса:
1.	Отображение информации об объекте класса.
2.	Метод, который позволяет устанавливать текущую скорость машины.
Проверьте работу этих методов.
'''


# class Toyota:
#     color = 'red'
#     price = 10 ** 6
#     max_speed = 200
#     cur_speed = 0
#
#     def info(self):
#         print('Car color: {}\nCar price: {} Rub\nMaximum speed: {} km/h\nCurrent speed: {} km/h\n'.format(
#             self.color, self.price, self.max_speed, self.cur_speed
#         ))
#
#     def set_cur_speed(self, current_speed):
#         self.cur_speed = current_speed
#
#
# car_1 = Toyota()
# car_1.info()
#
# car_1.set_cur_speed(80)
# car_1.info()
# 2 ==========================================================================
'''Задача 2. Семья
Реализуйте класс «Семья», который состоит из атрибутов «Имя», Деньги» и «Наличие дома» 
и объекты которого могут выполнять следующие действия:
1.	Отобразить информацию о себе.
2.	Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
3.	Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»). Вывести 
соответствующее сообщение об успешной/неуспешной покупке дома.
Создайте как минимум один экземпляр класса и проверьте работу методов.

Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):

Family name: Common family
Family funds: 100000
Having a house: False

Try to buy a house
Not enough money!

Earned 800000 money! Current value: 900000
Try to buy a house again
House purchased! Current money: 0.0

Family name: Common family
Family funds: 0.0
Having a house: True
'''


class Family:
    name = 'Common family'
    money = 100000
    have_a_house = False

    def info(self):
        print('Family name: {}\nFamily funds: {}\nHaving a house: {}\n'.format(
            self.name, self.money, self.have_a_house)
        )

    def earn_money(self, amount):
        self.money += amount
        print('Earned {} money! Current money balance: {}\n'.format(
            amount, self.money)
        )

    def buy_house(self, price, discount=0):
        price -= price * discount / 100
        print('Try to buy a house:')
        if self.money >= price:
            self.money -= price
            print('Congratulations! We purchased a house. Current money balance: {}\n'.format(self.money))
            self.have_a_house = True
        else:
            print('Not enough money!\n')


family_1 = Family()
family_1.info()

if not family_1.have_a_house:
    family_1.earn_money(800000)
    family_1.buy_house(10 ** 6, 10)

family_1.info()
