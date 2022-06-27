"""Работа за преподавателем"""

# Task 1

# def divide(number):
#     return 10 / number
#
#
# def sum_of_devided(left, right):
#     div_sum = 0
#     for i_num in range(left, right + 1):
#         try:
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
#
# answer_file = open('answer.txt', 'w')
# answer_file.write('The answer is: ')
# answer_file.write(str(total))
# answer_file.close()

# Task 2

# def divide(number):
#     return 10 / number
#
#
# def sum_of_devided(left, right):
#     div_sum = 0
#     for i_num in range(left, right + 1):
#         try:
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
#
# answer_file = open('answer.txt', 'w')
# try:
#     answer_file.write('The answer is: ')
#     answer_file.write(str(total))
# except TypeError:
#     print('Ошибка данных в файл: тип данных не строка.')
# answer_file.close()

# Task 3

# def divide(number):
#     return 10 / number
#
#
# def sum_of_devided(left, right):
#     div_sum = 0
#     for i_num in range(left, right + 1):
#         try:
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
#
# answer_file = open('answer.txt', 'w')
# try:
#     answer_file.write('The answer is: ')  # answer_file.write(int('The answer is: '))
#     answer_file.write(str(total))
# except TypeError:
#     print('Ошибка данных в файл: тип данных не строка.')
# else:     # Выполнится только если программа прошла без ошибок
#     print('Программа выполнилась без ошибок.')
# finally:  # Код в этом блоке будет выполняться всегда, независимо от того поймали мы ошибку или нет
#     answer_file.close()
#     print(answer_file.closed)   # Выведем закрыт файл или нет

# Home Work
# 1 ==========================================================================
import os

'''Задача 1. Простая программа
Напишите программу, которая открывает файл и записывает туда введённую 
пользователем строку. Используйте операторы try except else finally. 
Обработайте возможные ошибки:
1.	Проблема при открытии файла.
2.	Нельзя преобразовать данные в целое.
3.	Неожиданная ошибка.
'''
# import os
#
# user_string = input('Введите строку: ')
#
# try:
#     string = int(user_string)
#     file = open('record.txt', 'x', encoding='utf-8')
#     file.write(str(string))
# except ValueError:
#     print('Нельзя преобразовать данные в целое.')
# except FileExistsError:
#     print('Проблема при открытии файла.')
#     os.remove('record.txt')
# except:
#     print('Неожиданная ошибка.')
# else:
#     print('Программа завершилась успешно.')
# finally:
#     try:
#         file.close()
#     except NameError:
#         print('Файл не открывался.')
# 2 ==========================================================================
'''Задача 2. Старая задача
Возьмите любую задачу из домашнего задания, например, предыдущего модуля и 
оформите её решение в виде try except finally (можно ещё и else), обрабатывая 
возможные ошибки.
Посмотрев на то, что получилось, попробуйте ответить себе на такой вопрос: 
когда стоит использовать обработку исключений и когда она будет излишней?
'''
'''Задача 5 модуля 22.6. Сохранение
Мы продолжаем работать над усовершенствованием своего текстового редактора. Конечно же, 
при работе с редактором пользователь, скорее всего, захочет сохранить то, что он написал, 
в отдельный файл. Ну или перезаписать тот, в котором он продолжил работать. 
Пользователь вводит строку text. Реализуйте функцию, которая запрашивает у пользователя, 
куда он хочет сохранить эту строку: вводится последовательность папок и имя файла 
(расширение .txt). Затем в этот файл сохраняется значение переменной text. Если этот 
файл уже существует, то нужно спросить у пользователя, действительно ли он хочет перезаписать его.
Обеспечьте контроль ввода: указанный из папок путь должен существовать на диске.

Пример 1:
Введите строку: testiruyem

Куда хотите сохранить документ? Введите последовательность папок (через пробел):
Users Roman PycharmProjects Skillbox Module22

Введите имя файла: my_document
Файл успешно сохранён!

Содержимое файла:
programm test

Пример 2:
Введите строку: programm test

Куда хотите сохранить документ? Введите последовательность папок (через пробел):
Users Roman PycharmProjects Skillbox Module22

Введите имя файла: my_document
Вы действительно хотите перезаписать файл? да
Файл успешно перезаписан!

Содержимое файла:
testiruyem
'''
import os


def user_choice(text):
    save_dir = input(
        'Куда хотите сохранить документ? Введите последовательность папок (через пробел): ')  # Папка для теста - "1"
    folder_path = os.path.join(*save_dir.split(' '))  # Путь к папке куда нужно сохранить файл

    file_name = '.'.join(
        [input('Введите имя файла (без расширения .txt): '), 'txt'])  # Добавим к имени файла расширение
    file_path = os.path.join(folder_path, file_name)
    try:
        file = open(file_path, 'x', encoding='utf-8')
        file.write(text)
    except FileNotFoundError:
        print('Указанный из папок путь - не существует!')
    except FileExistsError:
        flag = input('Файл с таким именем уже существует, хотите удалить его и перезапустить программу (y/n)? ')
        if flag == 'y':
            os.remove(file_path)
            user_choice(string)
        else:
            print('Вы выбрали не удалять существующий файл.')
    else:
        file.close()
        print('Файл успешно сохранён!')


try:
    string = input('Введите строку: ')
    user_choice(string)
except KeyboardInterrupt:
    print('\n\nПрограмма прервана пользователем!')
except UnboundLocalError:
    print('')
