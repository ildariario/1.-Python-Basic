'''Работа за преподавателем'''
# Task 1
'''Задача №1 (Путь к файлу)
Нужно сформировать относительный путь к файлу, для использования в других скриптах
проекта. Сам путь из последовательности двух папок и имени файла нам известен
(т.е. дано docs/{folder}/{file}). Одну из папок и имя файла вводит юзер. Нужно
написать код, который выведет этот относительный путь на экран.
'''

# folder_name = 'project'
# file_name = 'my_file.txt'
#
# path = 'docs/{folder}/{file}'.format(
#     folder=folder_name,
#     file=file_name,
# )
#
# print(path)

# Task 2

# import os
#
# folder_name = 'project'
# file_name = 'my_file.txt'
#
# rel_path = os.path.join('docs', folder_name, file_name)
# print(rel_path)
#
# abs_path = os.path.abspath(file_name)
# print(abs_path)

# Task 3
'''Работа за преподавателем'''
# import os
#
# abs_path = os.path.abspath('new_folder')
# print('1:', abs_path)
#
# abs_path = os.path.abspath('../new_folder')
# print('2:', abs_path)
#
# abs_path = os.path.abspath(os.path.join('..', 'new_folder'))
# print('3:', abs_path)
#
# abs_path = os.path.abspath('/new_folder')
# print('4:', abs_path)
#
# abs_path = os.path.abspath(os.path.join(os.path.sep, 'new_folder'))
# print('5:', abs_path)

# Task 4
'''Задача №2 (Проекты)
Есть список из двух проектов «Git start» и «Hh», которые хранятся в папке 
«1. Python Basic». Написать прогу, которая выведет на экран содержимое каждого 
проекта, т.е. абсолютные пути до файлов и папок внутри них. 
'''
# import os
#
# def print_dirs(project):
#     print('\nСодержимое директории', project)
#     for i_elem in os.listdir(project):
#         path = os.path.join(project, i_elem)
#         print('    ', path)
#
# projects_list = ['1. Python Basic', 'Hh']
# for i_project in projects_list:
#     path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
#     print_dirs(path_to_project)

# Home Work
# 1 ==========================================================================
'''Напишите программу, которая выводит на экран относительный и абсолютный пути 
до файла admin.bat. 

Пример результата:
Абсолютный путь до файла: C:\Users\Roman\PycharmProjects\Skillbox\access\admin.bat
Относительный путь до файла: Skillbox\access\admin.bat
'''
# import os
#
# file_name = 'admin.bat'
# folder_name = 'access'
#
# abs_path = os.path.abspath(file_name)
# print('Абсолютный путь до файла:', abs_path)
# rel_path = os.path.join('Skillbox', folder_name, file_name)
# print('Относительный путь до файла:', rel_path)
# 2 ==========================================================================
'''Выберите любую директорию на своём диске и затем напишите программу, выводящую 
на экран абсолютные пути к файлам и папкам, которые находятся внутри этой директории. 
Результат программы на примере директории проекта python_basic:
Содержимое каталога G:\PycharmProjects\python_basic
    G:\PycharmProjects\python_basic\.git
    G:\PycharmProjects\python_basic\.idea
    G:\PycharmProjects\python_basic\Module14
    G:\PycharmProjects\python_basic\Module15
    G:\PycharmProjects\python_basic\Module16
    G:\PycharmProjects\python_basic\Module17
    G:\PycharmProjects\python_basic\Module18
    G:\PycharmProjects\python_basic\Module19
    G:\PycharmProjects\python_basic\Module20
    G:\PycharmProjects\python_basic\Module21
    G:\PycharmProjects\python_basic\Module22
'''
# import os
#
# def print_dirs(path):
#     print('Содержимое каталога:', path)
#     for i_path in os.listdir(path):
#         print('   ', os.path.join(path, i_path))
#
#
# project_folder = 'Git start'
#
# abs_path = os.path.abspath(os.path.join('..', '..', project_folder))
# print(abs_path)
# print_dirs(abs_path)
# 3 ==========================================================================
'''Напишите программу, которая выводит на экран только корень диска, на котором 
запущен скрипт. Учтите, что скрипт может быть запущен где угодно и при любой 
вложенности папок.

Результат программы на примере диска G:
Корень диска: G:\\
'''
import os

root_folder = os.path.abspath(os.path.sep)
print('Корень диска:', root_folder)
