"""Работа за преподавателем"""
# Task 1


# class User:
#     user_name = 'Admin'
#     password = 'qwerty'
#     is_banned = False
#
#
# user_1 = User()
# print(user_1)

# Task 2

# class User:
#     user_name = 'Admin'
#     password = 'qwerty'
#     is_banned = False
#
#
# user_1 = User()
# user_2 = User()
# user_2.user_name = 'Tom'
# print(user_1.user_name, user_2.user_name)
# User.user_name = 'Noname'
# print(user_1.user_name, user_2.user_name)

# Home Work
# 1 ==========================================================================
'''Задача 1. Машина
Напишите класс Toyota, состоящий из четырёх статических атрибутов: 
•	цвет машины (например, красный),
•	цена (один миллион),
•	максимальная скорость (200),
•	текущая скорость (ноль).
Создайте три экземпляра класса и каждому из них поменяйте значение текущей 
скорости на случайное число от нуля до 200.
'''
# import random
#
#
# class Toyota:
#     color = 'red'
#     price = 1000000
#     max_speed = 200
#     cur_speed = 0
#
#
# car_1 = Toyota()
# car_1.cur_speed = random.randint(0, 200)
#
# car_2 = Toyota()
# car_2.cur_speed = random.randint(0, 200)
#
# car_3 = Toyota()
# car_3.cur_speed = random.randint(0, 200)
#
# print(f'Текущая скорость 1-ой машины: {car_1.cur_speed}\n'
#       f'Текущая скорость 2-ой машины: {car_2.cur_speed}\n'
#       f'Текущая скорость 3-ой машины: {car_3.cur_speed}\n')
# 2 ==========================================================================
'''Задача 2. Однотипные объекты
В офис заказали небольшую партию из четырёх мониторов и трёх наушников. У монитора 
есть четыре характеристики: название производителя, матрица, разрешение и частота 
обновления экрана. Все четыре монитора отличаются только частотой.
У наушников три характеристики: название производителя, чувствительность и наличие 
микрофона. Отличие только в наличии микрофона.

Для внесения в базу программист начал писать такой код:

monitor_name_1 = 'Samsung'
monitor_matrix_1 = 'VA'
monitor_res_1 = 'WQHD'
monitor_freq_1 = 60
monitor_name_2 = 'Samsung'
monitor_matrix_2 = 'VA'
monitor_res_2 = 'WQHD'
monitor_freq_2 = 144
monitor_name_3 = 'Samsung'
monitor_matrix_3 = 'VA'
monitor_res_3 = 'WQHD'
monitor_freq_3 = 70
monitor_name_4 = 'Samsung'
monitor_matrix_4 = 'VA'
monitor_res_4 = 'WQHD'
monitor_freq_4 = 60

headphones_name_1 = 'Sony'
headphones_sensitivity_1 = 108
headphones_micro_1 = False
headphones_name_2 = 'Sony'
headphones_sensitivity_2 = 108
headphones_micro_2 = True
headphones_name_3 = 'Sony'
headphones_sensitivity_3 = 108
headphones_micro_3 = True

Поправьте программиста: перепишите код, используя классы и экземпляры классов.
'''


class BaseOfMonitors:
    monitor_name = 'Samsung'    # название производителя
    monitor_matrix = 'VA'       # матрица монитора
    monitor_resolution = 'WQHD' # разрешение монитора
    monitor_frequency = 60      # частота обновления экрана


class BaseOfHeadphones:
    headphones_name = 'Sony'        # название производителя
    headphones_sensitivity = 108    # чувствительность наушников
    headphones_micro = True         # наличие микрофона


monitor_1 = BaseOfMonitors()
monitor_2 = BaseOfMonitors()
monitor_2.monitor_frequency = 144
monitor_3 = BaseOfMonitors()
monitor_3.monitor_frequency = 70
monitor_4 = BaseOfMonitors()

headphone_1 = BaseOfHeadphones()
headphone_1.headphones_micro = False
headphone_2 = BaseOfHeadphones()
headphone_3 = BaseOfHeadphones()

print(f'monitor_fr_1: {monitor_1.monitor_frequency}\nmonitor_fr_2: {monitor_2.monitor_frequency}\n'
      f'monitor_fr_3: {monitor_3.monitor_frequency}\nmonitor_fr_4: {monitor_4.monitor_frequency}')
print(f'headphones_micro_1: {headphone_1.headphones_micro}\nheadphones_micro_2: {headphone_2.headphones_micro}\n'
      f'headphones_micro_3: {headphone_3.headphones_micro}')
