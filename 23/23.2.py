"""Работа за преподавателем"""
# Task 1

# numbers_file = open('numbers_1.txt', 'r')
# for i_line in numbers_file:
#     print(i_line, end='')
# numbers_file.close()

# Task 2

# try:
#     numbers_file = open('numbers_1.txt', 'r')
#     for i_line in numbers_file:
#         print(i_line, end='')
#     numbers_file.close()
# except:
#     print('Что-то пошло не так!')

# Task 3

# try:
#     numbers_file = open('numbers_1.txt', 'r')
#     for i_line in numbers_file:
#         print(i_line, end='')
#     numbers_file.close()
# except FileNotFoundError:
#     print('Такого файла не существует.')

# Task 4

# nums_sum = 0
# nums_count = 0
# try:
#     numbers_file = open('numbers.txt', 'r')
#     for i_line in numbers_file:
#         nums_count += 1
#         nums_sum += int(i_line)
#     numbers_file.close()
#     print('Среднее арифм.:', nums_sum / nums_count)
# except FileNotFoundError:   # Или можно так: (FileNotFoundError, ValueError)
#     print('Такого файла не существует.')
# except ValueError:
#     print('Нельзя преобразовать данные в целое число!')

# Task 5

# def divide(number):
#     return 10 / number
#
#
# def sum_of_devided(left, right):
#     div_sum = 0
#     for i_num in range(left, right + 1):
#         try:                            # Тут try ... except - в цикле!
#             div_sum += divide(i_num)
#             print(div_sum)
#         except ZeroDivisionError:
#             print('На ноль делить нельзя!')
#     return div_sum
#
#
# total = 0
# try:
#     number_file = open('numbers_2.txt', 'r')
#     for i_line in number_file:
#         nums_list = i_line.split()
#         first_num = int(nums_list[0])
#         second_num = int(nums_list[1])
#
#         total += sum_of_devided(first_num, second_num)
#     print('Общая сумма:', total)
#
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')

# Task 6

# def divide(number):
#     return 10 / number
#
#
# def sum_of_devided(left, right):
#     div_sum = 0
#     for i_num in range(left, right + 1):
#         try:                            # Тут try ... except - в цикле!
#             div_sum += divide(i_num)
#             print(div_sum)
#         except ZeroDivisionError:
#             print('На ноль делить нельзя!')
#     return div_sum
#
#
# total = 0
# number_file = open('numbers_2.txt', 'r')
# for i_line in number_file:
#     nums_list = i_line.split()
#     first_num = int(nums_list[0])
#     second_num = int(nums_list[1])
#
#     total += sum_of_devided(first_num, second_num)
# print('Общая сумма:', total)

# Home Work
# 1 ==========================================================================
'''Задача 1. Пятый элемент
В курсе по программированию студенту дали простую задачу: умножить константу (число 42) на пятый 
элемент строки, введённой пользователем. Вот код студента:

BRUCE_WILLIS = 42

input_data = input('Введите строку: ')
leeloo = int(input_data[4])
result = BRUCE_WILLIS * leeloo
print(f'- Leeloo Dallas! Multi-pass № {result}!')

Модифицируйте этот код, обработав исключения для произвольных входных параметров:
•	ValueError — невозможно преобразовать к числу,
•	IndexError — выход за границы списка,
•	остальные исключения.
Для каждого типа исключений выведите на консоль соответствующее сообщение.
'''
# BRUCE_WILLIS = 42
# try:
#     input_data = input('Введите строку: ')
#     leeloo = int(input_data[4])
#     result = BRUCE_WILLIS * leeloo
#     print(f'- Leeloo Dallas! Multi-pass № {result}!')
# except ValueError:
#     print('Необходимо ввести строку из цифр!')
# except IndexError:
#     print('Необходимо ввести строку минимум из пяти символов!')
# except:
#     print('Что-то пошло не так!')
# 2 ==========================================================================
'''Задача 2. Возраст
Дан файл ages.txt, в котором построчно хранятся десять возрастов для каждого человека.
Напишите программу, которая считывает файл, даёт имя для каждого возраста (можно просто использовать 
буквы алфавита) и выводит результат в новый файл result.txt в формате «имя — возраст». Программа должна 
обрабатывать следующие ошибки и выводить сообщение на экран:
1.	Попытка создания файла, который уже существует.
2.	На чтение ожидался файл, но это оказалась директория.
3.	Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).
При желании воспользуйтесь подсказкой, чтобы найти подходящие имена ошибок.
'''
import string
import os

try:
    file_inp = open('ages.txt', 'r')
    file_out = open('result.txt', 'x')
    for i_ind, i_age in enumerate(file_inp.readlines()):
        file_out.write(' - '.join([string.ascii_uppercase[i_ind], i_age]))
    file_inp.close()
    file_out.close()
except FileExistsError:
    choice = input('Попытка создания файла, который уже существует. Хотите удалить его? (Да/Нет): ')
    if choice == 'Да':
        os.remove('result.txt')
        print('Файл result.txt - удален, запустите программу заново.')
except FileNotFoundError:
    print('Файл или директория не существует.')
except IsADirectoryError:           # Не смог инициировать это исключение, при указании папки вместо файла
    print('Это не файл, а папка.')  # возникает исключение PermissionError, а не IsADirectoryError
except PermissionError:
    print('Отсутствуют права на доступ к файлу или папке.')
except (TypeError, ValueError):     # Не смог инициировать это исключение
    print('Неверный тип данных или некорректное значение.')
except OSError:                     # Это указал просто так, до кучи как говориться
    print("Неустановленная ошибка.")
