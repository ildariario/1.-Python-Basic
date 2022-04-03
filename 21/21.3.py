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

# Task 2



# Task 3



# Home Work
# 1 ==========================================================================
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
# 3 ==========================================================================

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