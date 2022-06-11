'''Работа за преподавателем'''
# Task 1
'''Задача №1 (Участники конференции)
Нам передан в виде текстового файла speakers.txt список выступающих на конференции людей.
В каждой строке текстового файла содержатся фамилия, имя и возраст человека. Написать
программу, которая выведет на экран содержимое файла.
'''
# speakers_file = open('speakers.txt', 'r', encoding='utf-8')
# data = speakers_file.read()
# print(data)
# speakers_file.close()

# Task 2

# speakers_file = open('speakers.txt', 'r',
#                      encoding='utf-8')
#
# data = speakers_file.read()
# another_data = speakers_file.read()
# print('Данные:', data, sep='\n')
# print('\nДругие данные:', another_data)
# speakers_file.close()
# # -------------------------------------------
# speakers_file = open('speakers.txt', 'r',
#                      encoding='utf-8')
# data = speakers_file.read()
#
# speakers_file = open('speakers.txt', 'r',
#                      encoding='utf-8')
# another_data = speakers_file.read()
#
# print('Данные:', data, sep='\n')
# print('\nДругие данные:', another_data, sep='\n')
# speakers_file.close()

# Task 3

# speakers_file = open('speakers.txt', 'r', encoding='utf-8')
#
# for i_line in speakers_file:
#     print(i_line)
# speakers_file.close()

# Task 4

# speakers_file = open('speakers.txt', 'r', encoding='utf-8')
#
# for i_line in speakers_file:
#     print(i_line, end='')
# speakers_file.close()

# Home Work
# 1 ==========================================================================
'''Обработать результаты тестирования двух групп людей. Файл первой группы (group_1.txt) 
находится в папке task (D:\Works of Skillbox\1. Python Basic\folder for working with files\
for lesson 22.3\task), файл второй группы (group_2.txt) — в папке Additional_info 
(D:\Works of Skillbox\1. Python Basic\folder for working with files\for lesson 22.3\task\
Additional_info).

Содержимое файла group_1.txt
Бобровский Игорь 10
Дронов Александр 20
Жуков Виктор 30

Содержимое файла group_2.txt
Павленко Геннадий 20
Щербаков Владимир 35
Marley Bob 15
На экран нужно вывести сумму очков первой группы, затем разность очков опять же 
первой группы и напоследок — произведение очков уже второй группы. '''
# ------------------------------------------------------------------------------------
# import os
#
# # Вариант 1
# # rel_path = '../folder for working with files/for lesson 22.3/task/group_1.txt'
# # Вариант 2
# # abs_path = os.path.join('D', ':', os.path.sep, 'Works of Skillbox', '1. Python Basic',
# #                         'folder for working with files', 'for lesson 22.3', 'task', 'group_1.txt')
# # Вариант 3
# # abs_path_1 = r'D:\Works of Skillbox\1. Python Basic\folder for working with files\for lesson 22.3\task\group_1.txt'
# # Вариант 4
# abs_path_1 = 'D:\\Works of Skillbox\\1. Python Basic\\' \
#            'folder for working with files\\for lesson 22.3\\task\\group_1.txt'
# abs_path_2 = 'D:\\Works of Skillbox\\1. Python Basic\\' \
#            'folder for working with files\\for lesson 22.3\\task\\Additional_info\\group_2.txt'
#
# file = open(abs_path_1, 'r', encoding='utf-8')
# summa = 0
# for i_line in file:
#     info = i_line.split()
#     summa += int(info[2])
# file.close()
#
# file = open(abs_path_1, 'r', encoding='utf-8')
# first = file.readline().split()
# diff = int(first[2])
# for i_line in file:
#     info = i_line.split()
#     diff -= int(info[2])
# file.close()
#
# file = open(abs_path_2, 'r', encoding='utf-8')
# compose = 1
# for i_line in file:
#     info = i_line.split()
#     compose *= int(info[2])
# file.close()
#
# print(summa)
# print(diff)
# print(compose)
# 2 ==========================================================================
'''Задача 2. Поиск файла 2
Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только 
программисту. Таким образом, с ними можно работать точно так же, как и с обычными 
текстовыми файлами.
Используя функцию поиска файла из предыдущего урока, реализуйте программу, которая 
находит внутри указанного пути все файлы с искомым названием и выводит на экран текст 
одного из них (выбор можно сгенерировать случайно).
Подсказка: можно использовать, например, список для сохранения найденного пути.
'''
# --------------------------------------------------------------------------------------
import os
import random

def find_file(path, file_name, path_list=None):
    if path_list == None:
        path_list = []
    for i_elem in os.listdir(path):
        new_path = os.path.abspath(os.path.join(path, i_elem))
        if i_elem == file_name:
            path_list.append(os.path.abspath(os.path.join(path, i_elem)))
        if os.path.isdir(new_path):
            find_file(new_path, file_name, path_list)
    return path_list


abs_path = os.path.abspath(os.path.join('..', '..'))
print('Поиcк ведется в каталоге:', abs_path)
searched_file = input('Какой файл ищем? ')

if find_file(abs_path, searched_file):
    print('Найдены следующие пути:')
    for i_index, i_path in enumerate(find_file(abs_path, searched_file)):
        print('-'*60)
        print(f'{i_index+1}-й файл:', i_path, '\n\t|\tРазмер файла:', os.path.getsize(i_path), 'байт\t|')
    # Случайный выбор пути из списка путей возвращаемого из функции
    chosen_path = random.randint(0, len(find_file(abs_path, searched_file))-1)
    # chosen_path = random.choice(find_file(abs_path, searched_file))
    print('-' * 60)
    print('Содержимое {}-го файла (файл выбран случайно):'.format(chosen_path+1))
    file = open(find_file(abs_path, searched_file)[chosen_path], 'r', encoding='utf-8')
    code_of_file = file.read()
    print(code_of_file)
    file.close()
else:
    print('Файл {} в директории {} не найден!'.format(searched_file, abs_path))
print('-'*60)
