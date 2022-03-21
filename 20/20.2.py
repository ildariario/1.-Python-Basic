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
# 4 ==========================================================================

# 5 ==========================================================================

# 6 ==========================================================================

# 7 ==========================================================================

# 8 ==========================================================================

# 9 ==========================================================================

# 10 ==========================================================================

# 11 ==========================================================================

# 12 ==========================================================================

# 13 ==========================================================================

# 14 ==========================================================================

# 15 ==========================================================================
