'''Работа за преподавателем'''
# Task 1

# import os
#
# def print_dirs(project):
#     print('\nСодержимое директории', project)
#     for i_elem in os.listdir(project):
#         path = os.path.join(project, i_elem)
#         print('    ', path)
#
# projects_list = ['Prod', '1. Python Basic', 'Hh']
# for i_project in projects_list:
#     path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
#     # print(path_to_project)
#     print_dirs(path_to_project)

# Task 2

# import os
#
# def print_dirs(project):
#     print('\nСодержимое директории', project)
#     if os.path.exists(project):
#         for i_elem in os.listdir(project):
#             path = os.path.join(project, i_elem)
#             print('    ', path)
#     else:
#         print('     Такого каталога проекта не существует.')
#
# projects_list = ['Prod', '1. Python Basic', 'Hh']
# for i_project in projects_list:
#     path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
#     print_dirs(path_to_project)

# Task 3
'''Задача №1 (Поиск)
Нужно написать функцию, которая ищет нужный нам файл внутри директории, а затем
выводит его абсолютный путь на экран.
'''

# import os
#
# def find_file(cur_path, file_name):
#     print('Переходим в:', cur_path)
#     print(f'    список содержимого папки {cur_path}:', os.listdir(cur_path))
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         print('    смотрим:', path)
#         if i_elem == file_name:
#             return path
#         if os.path.isdir(path):
#             print(f'    {i_elem} - это директория')
#             result = find_file(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# print()
# searched_file = 'hello.py'
# file_path = find_file(os.path.abspath(os.path.join('..', '..', 'Hh')), searched_file)
#
# if file_path:
#     print('\nФайл найден!\nАбсолютный путь к файлу:', file_path)
#     print(f'Размер файла {os.path.getsize(file_path)} байт.')
# else:
#     print('\nФайл не найден.')

# Home Work
# 1 ==========================================================================
'''Задача 1. Иконки
Андрей для себя хочет сделать экспериментальный сайт, где будет красиво отображаться
вся структура его диска: папки одними иконками, файлы — другими. Поэтому ему нужен код,
который поможет определить, какой тип иконки вставить.
Напишите программу, которая по заданному абсолютному пути определяет, на что указывает
этот путь (на директорию, файл, или же путь является ссылкой), и выведите соответствующее
сообщение. Если путь указывает на файл, то также выведите его размер (сколько он весит
в байтах). Обеспечьте контроль ввода: проверка пути на существование.
Подсказка: для вывода размера файла поищите соответствующий метод.

Пример 1:
Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
Это файл
Размер файла: 605 байт

Пример 2:
Путь: C:\Users\Roman\PycharmProjects\Skillbox\Module17\lesson2.py
Указанного пути не существует
'''

# import os
#
# abs_path = input('Путь: ')
# if os.path.exists(abs_path):
#     if os.path.isdir(abs_path):
#         print('Это директория')
#     elif os.path.isfile(abs_path):
#         print('Это файл')
#         print('Размер файла:', os.path.getsize(abs_path), 'байт')
#     else:
#         print('Это ссылка')
# else:
#     print('Указанного пути не существует')
# 2 ==========================================================================
'''Задача 2. Поиск файла
В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах 
указанной директории. Однако, как мы понимаем, файлов с таким названием может быть 
несколько.
Напишите функцию, которая принимает на вход абсолютный путь до директории и имя 
файла, рекурсивно проходит по всем вложенным файлам и папкам и выводит на экран 
все абсолютные пути с этим именем.

Пример:
Ищем в: C:/Users/Roman/PycharmProjects/Skillbox
Имя файла: lesson2

Найдены следующие пути:
C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module18\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module19\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module20\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module21\lesson2.py
C:/Users/Roman/PycharmProjects/Skillbox\Module22\lesson2.py

'''

import os

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


searched_file = input('Какой файл ищем? ')
abs_path = os.path.abspath(os.path.join('..', '..'))
if find_file(abs_path, searched_file):
    print('Найдены следующие пути:')
    for i_path in find_file(abs_path, searched_file):
        print('-'*60)
        print(i_path, '\n   | Размер файла:', os.path.getsize(i_path), 'байт |')
else:
    print('Файл {} в директории {} не найден!'.format(searched_file, abs_path))
print('-'*60)
