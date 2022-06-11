'''Работа за преподавателем'''
# Task 1
'''Задача №1 (Участники конференции 2)
Нам передан в виде текстового файла speakers.txt список выступающих на конференции
людей. В каждой строке текстового файла содержатся фамилия, имя и возраст человека.
Чтобы понять, сколько места в базе данных (БД) будет занимать каждый участник, нужно
посчитать из скольких символов состоит каждая строчка (т.е. каждый участник) и
вывести ответы в отдельный файл.
'''
# speakers_file = open('speakers.txt', 'r', encoding='utf-8')
# sym_count = []
# for i_line in speakers_file:
#     print(i_line, end='')
#     sym_count.append(str(len(i_line)))
# print()
# sym_count_str = '\n'.join(sym_count)
# speakers_file.close()
# print(sym_count_str)

# Task 2

# speakers_file = open('speakers.txt', 'r', encoding='utf-8')
# sym_count = []
# for i_line in speakers_file:
#     print(i_line, end='')
#     sym_count.append(str(len(i_line)))
# sym_count_str = '\n'.join(sym_count)
# speakers_file.close()
#
# counts_file = open('sym_counts.txt', 'w')
# counts_file.write(sym_count_str)
# counts_file.write('\n'+str(50))
# counts_file.close()

# Task 3
'''Задача №2 (История поиска)
Нам нужно создать что-то вроде истории поиска. Написать программу, которая каждый 
раз при запуске программы будет сохранять в текстовый файл абсолютный путь 
искомого файла. 
'''
# import os
#
# def find_file(cur_path, file_name):
#     print('Переходим в:', cur_path)
#
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         print('\tсмотрим:', path)
#
#         if i_elem == file_name:
#             return path
#         if os.path.isdir(path):
#             print(f'\t{i_elem} - это директория')
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# # searched_file = 'hello.py'
# searched_file = 'checkUp_1.py'
# file_path = find_file(os.path.abspath(os.path.join('..', '..', 'Hh')), searched_file)
# history_file = open('search_history.txt', 'a', encoding='utf-8')
# if file_path:
#     print('\nФайл найден!\nАбсолютный путь к файлу:', file_path)
#     history_file.write(file_path+'\n')
# else:
#     print('\nФайл не найден.')
# history_file.close()

# Home Work
# 1 ==========================================================================
'''Описание
Задача 1. Сумма чисел
Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке. 
Напишите программу, которая выводит их сумму в выходной файл answer.txt.
Пример:
Содержимое файла numbers.txt:
1
2
3
4
10
Содержимое файла answer.txt
20
'''
# input_file = open('numbers.txt', 'r')
# output_file = open('answer.txt', 'w')
#
# summ = 0
# for i_string in input_file:
#     summ += int(i_string)
# output_file.write(str(summ))
#
# input_file.close()
# output_file.close()
# 2 ==========================================================================
'''Напишите программу, которая копирует код каждого скрипта в папке 22 проекта 
python_basic в файл scripts.txt, разделяя код строкой из 40 символов *.
Пример содержимого файла scripts.txt:
import platform
import sys

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
)
print(info)

with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)
****************************************
print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

print("Уравнение прямой, проходящей через эти точки:")
x_diff = x1 - x2
y_diff = y1 - y2
if x_diff == 0:
    print("x = ", x1)
elif y_diff == 0:
    print("y = ", y1)
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("y = ", k, " * x + ", b)
****************************************
...
'''
import os

out_file = open('scripts.txt', 'w', encoding='utf-8')

for i_ind, i_path in enumerate(os.listdir()):
    if not i_path.endswith('txt'):
        print('Файл:', i_path)
        inp_file = open(i_path, 'r', encoding='utf-8')
        content_file = inp_file.read()
        out_file.write('\n'.join([''.join([str(i_ind+1), '-й файл: ', i_path]), content_file, '*' * 120, '']))
        # out_file.write(''.join([i_path, ':\n', content_file, '\n', '*'*120, '\n', '*'*120, '\n']))
        inp_file.close()
out_file.close()
