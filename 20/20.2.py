'''Работа за преподавателем'''
# Task 1

# def add_num(seq, number):
#     for i_num in range(len(seq)):
#         seq[i_num] += number
#
#
# origin_list = [3, 1, 4, 1, 5]
# add_num(origin_list, 5)
# print(origin_list)

# Task 2

# def add_num(seq, number):
#     for i_num in range(len(seq)):
#         seq[i_num] += number
#
#
# origin_list = [3, 1, 4, 1, 5]
# changed_list = origin_list[:]
# add_num(changed_list, 5)
# print(origin_list)
# print(changed_list)

# Task 3

# def add_num(seq, number):
#     seq = list(seq)
#     for i_num in range(len(seq)):
#         seq[i_num] += number
#     return seq
#
#
# origin_tuple = (3, 1, 4, 1, 5)
# changed_list = add_num(origin_tuple, 5)
# print(origin_tuple)
# print(changed_list)

# Home Work
# 1 ==========================================================================
'''Задача 1. Создание кортежей
Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно. 
Также заполните второй кортеж числами от −5 до 0. Объедините два кортежа, создав тем 
самым третий кортеж. С помощью метода кортежа определите в нём количество нулей. 
Выведите на экран третий кортеж и количество нулей в нём.
'''
# from random import randint
#
# first_tuple = tuple([randint(0, 5) for _ in range(5)])
# second_tuple = tuple([randint(-5, 0) for _ in range(5)])
#
# third_tuple = list(first_tuple[:])
# third_tuple.extend(second_tuple)   # Третий список расширяем кортежем
# third_tuple = tuple(third_tuple)
#
# print('first_tuple:', first_tuple)
# print('second_tuple:', second_tuple)
# print('third_tuple:', third_tuple)
# print('Количество нулей в third_tuple:', third_tuple.count(0))
# 2 ==========================================================================
'''Задача 2. Цилиндр
Андрей однажды уже писал функции для расчёта площади сферы и объёма шара. И теперь для 
своей курсовой работы ему пришлось связаться с цилиндрами.
Пользователь вводит два значения: радиувуа и высоту. Напишите функцию для расчёта площади 
боковой поверхности цилиндра и его полной площади. Функция должна возвращать два эти 
значения. После этого в основной программе выводятся оба ответа в две строки.
Площадь боковой поверхности (r — радиус, h — высота):
side = 2*pi*r*h
Полная площадь (S — площадь круга):
full = side + 2*S
'''
# from math import pi
#
#
# def squares_cylinder(radius, height):
#     side = 2 * pi * radius * height
#     full = side + 2 * (pi * radius ** 2)
#     return side, full
#
#
# r = int(input('Введите радиус цилиндра: '))
# h = int(input('Введите высоту цилиндра: '))
#
# side, full = squares_cylinder(r, h)
#
# print('Площадь боковой поверхности:', side)
# print('Полная площадь:', full)
# 3 ==========================================================================
'''Задача 3. Неправильный код
Дан код, в котором должно происходить следующее: изначально есть кортеж из пяти чисел. 
Затем вызывается функция, которая получает на вход кортеж чисел, генерирует случайный 
индекс и случайное значение, а затем по этим индексу и значению меняет сам кортеж. 
Функция должна возвращать кортеж и случайное значение.
В основном коде функция используется два раза, и на экран два раза выводится новый кортеж 
и случайное значение. Причём второй раз выводится сумма первого случайного значения и второго.
Однако код, который вам дали, оказался нерабочим. Исправьте его в соответствии с описанием.
import random

def change(nums):
    index = random.randint(0, 5)
    value = random.randint(100, 1000)
    nums[index] = value
    return nums, value

my_nums = 1, 2, 3, 4, 5

new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums = change(new_nums)
rand_val += change(new_nums)
print(new_nums, rand_val)
'''
import random


def change(nums):
    nums = list(nums)
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    nums[index] = value
    nums = tuple(nums)
    return nums, value


my_nums = 1, 2, 3, 4, 5

new_nums, rand_val_1 = change(my_nums)
print(new_nums, rand_val_1)
new_nums, rand_val_2 = change(new_nums)
rand_val_2 += rand_val_1
print(new_nums, rand_val_2)
