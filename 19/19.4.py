# Task 1

# from random import randint
#
# numbers_list = [randint(1, 4) for _ in range(10)]
# new_list = []
# for i_num in numbers_list:
#     if i_num not in new_list:
#         new_list.append(i_num)
# print(numbers_list)
# print(new_list)

# Task 2

# from random import randint
#
# numbers_list = [randint(1, 4) for _ in range(10)]
#
# unique = set(numbers_list)
# print(unique)

# Task 3

# Методы множеств
# nums_1 = {1, 2, 3, 4, 5}
# nums_2 = {4, 5, 6, 7, 8}
# nums_str = 'ildario'
#
# print('Исходные множества:\nnum_1 =', nums_1, '\nnum_2 =', nums_2, '\nnum_str =', nums_str, '\n')
# nums_set = set(nums_str)
# print('Преобразование строки nums_str в множество:\t', nums_set)
#
# # Метод intersection - пересечение множеств
# print('Пересечение nums_1 и nums_2:\t\t\t\t\t', nums_1.intersection(nums_2))
# # print('Пересечение nums_1 и nums_2:\t\t\t\t\t', nums_1 & nums_2)  # & - амперссанд
#
# Метод union - объединение множеств
# print('Объединение nums_1 и nums_2:\t\t\t\t\t', nums_1.union(nums_2))
# # print('Объединение nums_1 и nums_2:\t\t\t\t\t', nums_1 | nums_2)  # | - амперссанд
# nums_sum_list = list(nums_1 | nums_2)
# print('Преобразование объединенных множеств в список:\t', nums_sum_list)
#
# # Метод difference - разность множеств
# print('Разность nums_1 и nums_2:\t\t\t\t\t\t', nums_1.difference(nums_2))
# # print('Разность nums_1 и nums_2:\t\t\t\t\t\t', nums_1 - nums_2)   # "-" - амперссанд
# print('Разность nums_2 и nums_1:\t\t\t\t\t\t', nums_2 - nums_1)
#
# # Метод symmetric_difference - симметрическая разность множеств
# print('Симметрическая разность nums_1 и nums_2:\t\t', nums_1.symmetric_difference(nums_2))
# # print('Симметрическая разность nums_1 и nums_2:\t', nums_1 ^ nums_2)  # "^" - амперссанд
# print('Симметрическая разность nums_2 и nums_1:\t\t', nums_2 ^ nums_1)
#
# nums_1.add(100)
# nums_2.add(200)
# print(nums_1)
# print(nums_2)
# nums_1.discard(2)
# nums_2.discard(5)
# print(nums_1)
# print(nums_2)

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# A.intersection_update(B)
# print(A)
# print(B)
# A = A.union(B)
# print(A)
# print(B)
# A.difference_update(B)
# print(A)
# print(B)
# A.symmetric_difference_update(B)
# print(A)
# print(B)

# Home Work
# 1 ==========================================================================
# string = input('Введите строку: ')
# symbols_set = set('.,;:!?')
#
# count = [string.count(i_sym) for i_sym in symbols_set if i_sym in string]
# print('Количество знаков пунктуации: ', sum(count))
# 2 ==========================================================================
# from random import randint
# nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24,
#           26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8,
#           27, 2, 17, 2, 20, 12, 21, 3, 1]
# nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5,
#           21, 5, 19, 9, 12, 9, 15, 16, 29, 8,
#           16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
# print('1-е множество: ', nums_1)
# print('2-е множество: ', nums_2)
# nums_1 = set(nums_1)
# nums_2 = set(nums_2)
# print('Минимальный элемент 1-го множества:', min(nums_1))
# print('Минимальный элемент 2-го множества:', min(nums_2))
# nums_1.discard(min(nums_1))
# nums_2.discard(min(nums_2))
# rand_nim_1 = randint(100, 200)
# rand_nim_2 = randint(100, 200)
# print('Случайное число для 1-го множества:', rand_nim_1)
# print('Случайное число для 2-го множества:', rand_nim_2)
# nums_1.add(rand_nim_1)
# nums_2.add(rand_nim_2)
# print('Объединение множеств:', nums_1.union(nums_2))
# print('Пересечение множеств:', nums_1.intersection(nums_2))
# print('Элементы, входящие в nums_2, но не входящие в nums_1:', nums_2.difference(nums_1))
# 3 ==========================================================================
string = input('Введите строку: ')

string_set = set(string)
print(string_set)
diff_nums_list = [i_sym for i_sym in string_set if '0' <= i_sym <= '9']
diff_nums_list = ''.join(sorted(diff_nums_list))

print('Различные цифры строки:', diff_nums_list)
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