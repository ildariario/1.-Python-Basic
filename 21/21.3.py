'''Работа за преподавателем'''
# Task 1

# def try_to_change_values(some_list, num):
#     for i_index, i_val in enumerate(some_list):
#         some_list[i_index] += 10
#     num += 10
#
#
# my_list = [1, 2, 3]
# number = 100
#
# try_to_change_values(my_list, number)
# print(my_list, number)

# Home Work
# 1 ==========================================================================
'''Задача 1. Ошибка
В одном проекте на 10 000 строк кода произошла критическая ошибка. Хорошо, что старший 
разработчик быстро её нашёл и исправил. Он решил проверить, смогли бы вы её исправить, 
если бы его не было на месте. Поэтому он написал для вас код с аналогичной ошибкой:

import random

def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)


nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}
common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}

change_dict(common_dict)
print(common_dict)

Суть кода в том, что у вас есть общий словарь из нескольких ключей, значения которых 
равны ранее объявленным переменным. Затем вызывается функция, которая должна изменять 
значения словаря, добавляя к значениям случайное число, в зависимости от типа данных. 
Но при этом меняются и ранее объявленные переменные. Исправьте эту ошибку и убедитесь, 
что nums_list, some_dict и uniq_nums не меняются.
'''
# import random
#
# def change_dict(dct):
#     num = random.randint(1, 100)
#     for i_key, i_value in dct.items():
#         if isinstance(i_value, list):
#             new_list = i_value[:] + [num]
#             dct[i_key] = new_list
#         if isinstance(i_value, dict):
#             new_dict = {j_key: j_value for j_key, j_value in i_value.items()}
#             new_dict[num] = i_key
#             dct[i_key] = new_dict
#         if isinstance(i_value, set):
#             new_set = {j_key for j_key in i_value}
#             new_set.add(num)
#             dct[i_key] = new_set
#
#
# nums_list = [1, 2, 3]
# some_dict = {1: 'text', 2: 'another text'}
# uniq_nums = {1, 2, 3}
# common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
#
# change_dict(common_dict)
# print(common_dict)
# print()
# print(nums_list)
# print(some_dict)
# print(uniq_nums)
# 2 ==========================================================================
'''Задача 2. Непонятно!
Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками, 
объектами и их id. Видя, как он мучается, вы решили добить помочь ему и объяснить эту 
тему наглядно.
Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых 
данных, информацию о его изменяемости, а также id этого объекта.

Пример 1:
Введите данные: привет

Тип данных: str (строка)
Неизменяемый (immutable)
Id объекта: 1705156583984

Пример 2:
Введите данные: {‘a’: 10, ‘b’: 20}

Тип данных: dict (словарь)
Изменяемый (mutable)
Id объекта: 1705205308536
'''
def get_data(obj):
    immutable = ['int', 'float', 'bool', 'str', 'tuple']

    if obj.isdigit():
        type_data = 'int'
        name = 'целочисленный'
    elif obj == 'True' or obj == 'False':
        type_data = 'bool'
        name = 'логический'
    elif obj.startswith('['):
        type_data = 'list'
        name = 'список'
    elif obj.startswith('{'):
        if ':' in obj:
            type_data = 'dict'
            name = 'словарь'
        else:
            type_data = 'set'
            name = 'множество'
    elif obj.startswith('('):
        type_data = 'tuple'
        name = 'кортеж'
    else:
        if obj.count('.') == 1:
            type_data = 'float'
            name = 'вещественный'
        else:
            type_data = 'str'
            name = 'строковый'

    print(f'Тип данных: {type_data} ({name})')
    if type_data in immutable:
        print('Неизменяемый (immutable)')
    else:
        print('Изменяемый (mutable)')
    print('Id объекта: ', id(type_data))

some_object = input('Введите данные: ')
get_data(some_object)
