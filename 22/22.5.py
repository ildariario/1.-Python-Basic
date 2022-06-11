'''Работа за преподавателем'''
# Task 1

# speakers_file = open('speakers.txt', 'r', encoding='utf-8')
# data = speakers_file.read(14)
# speakers_file.seek(1)
# data_2 = speakers_file.read(22)
# print(data)
# print(data_2)
# speakers_file.close()

# Task 2

# speakers_file = open('speakers.txt', 'r', encoding='utf-8')
# print(speakers_file.tell())
# data = speakers_file.readline()
# print(data)
# print(speakers_file.tell())
# speakers_file.close()

# Самостоятельная работа (Осваивал работу с модулями os, glob, pathlib, shutil, zipfile которые не рассмотрены в курсе)
'''Операции над файлами и директориями'''
# 1 ==========================================================================
'''Полезная информация, которую можно получить с помощью методов файлового объекта'''
# file = open('example_1.txt', 'w', encoding='utf=8')
#
# data = 'Привет Python!\nРад тебя видеть!\n'
# file_name = f'Имя файла: {file.name}'
# file_close = f'Статус закрытия файла (True - закрыт): {file.closed}'
# file_mode = f'Режим (mode) в котором был открыт файл: {file.mode}'
# file_encoding = f'Кодировка файла: {file.encoding}'
#
# data_list = [data, file_name, file_close, file_mode, file_encoding]
# file.write('\n'.join(data_list))
# file.close()
#
# print(f'Статус закрытия файла (True - закрыт): {file.closed}')
# 2 ==========================================================================
'''Модуль os. Справка'''
# import os
#
# print('Метод os.pardir (переход к родительскому каталогу (т.е. на уровень выше)):', os.pardir)
# print('Метод os.curdir (текущий каталог):', os.curdir)
# print('Метод os.extsep (разделитель отделяющий имя файла от расширения):', os.extsep)
# print('Метод os.sep (разделитель компонентов пути):', os.sep)
# 3 ==========================================================================
'''1. Модуль os. Удаление файла по определенному пути'''
# import os
#
# # Вар 1 =============
# file_name = 'For example_1.txt'
# rel_path_file = os.path.join('for test_1', file_name)
#
# if os.path.exists(rel_path_file):
#     os.remove(rel_path_file)
# else:
#     print('Такого файла нет в каталоге!')
#
# # Вар 2 =============
# # file_name = 'For example_2.txt'
# # abs_path_file = r'D:\Works of Skillbox\1. Python Basic\22\for test_1\Прочти перед изучением!.docx'
# # abs_path_file = os.path.abspath(os.path.join('for test_1', file_name))
# # os.remove(abs_path_file)
# 4 ==========================================================================
'''2(a). Модуль os. Переименование файлов'''
# import os
#
# rm_part = '[SW.BAND] '
# count = 0
# for index, i_file in enumerate(os.listdir('for test_2')):
#     cur_path = os.path.join('for test_2', i_file)
#     print(f'{index+1}-й файл:', i_file)
#     if rm_part in i_file:
#         new_name = i_file.replace(rm_part, '')  # replace - заменить
#         new_path = os.path.join('for test_2', new_name)
#         if not os.path.exists(new_path):
#             os.rename(cur_path, new_path)
#             print('\tПереименован на "{}"'.format(new_name))
#             count += 1
#         else:
#             print('\tПереименование невозможно, т.к. файл с таким именем уже существует!')
#     else:
#         print(f'\tНе нужно переименовывать.')
#
# print(f'\nВсего переименовано {count} файлов.')

'''2(b). Модуль os. Перемещение файлов из одной папки в другую'''
# import os
#
# count = 0
# for index, i_file in enumerate(os.listdir('for test_3')):
#     cur_path = os.path.join('for test_3', i_file)
#     print(f'{index+1}-й файл:', i_file)
#     new_path = os.path.join('empty for file', i_file)
#     if os.path.exists(new_path):
#         print('\tПеремещение невозможно, т.к. файл с таким именем уже существует!')
#     else:
#         os.rename(cur_path, new_path)
#         print('\t- перемещен в папку "empty for file"')
#         count += 1
#
# print(f'\nВсего перемещено файлов: {count}')

'''2(c). Модуль os. Переименование каталога'''
# import os
#
# rm_part_list = ['[SW.BAND] ', '[SW.BAND]']
# count = 0
# os.chdir('for test_5')
# for i_elem in os.listdir():
#     if os.path.isdir(i_elem):
#         print(f'Каталог: «{i_elem}»')
#         for i_rm in rm_part_list:
#             if i_rm in i_elem:
#                 new_name = i_elem.replace(i_rm, '')  # replace - заменить
#                 if os.path.exists(new_name):
#                     print('\t- не удалось переименовть, т.к. файл с таким именем уже есть в папке.')
#                     break
#                 else:
#                     os.rename(i_elem, new_name)
#                     count += 1
#                     print(f'\t- переименован.')
#                     break   # Выход из цикла нужен для избежания двойной проверки удаляемой части из имени файла
#         else:
#             print(f'\t- не нужно переименовывать.')
#
# print(f'\nВсего переименовано папок: {count}')
# 5 ==========================================================================
'''2(d). Модуль os. Перемещение папки из одного каталога в другой'''
# import os
#
# count = 0
# os.chdir('for test_6')
# for i_file in os.listdir():
#     if os.path.isdir(i_file):
#         print(f'{count+1}-я папка:', i_file)
#         new_path = os.path.join(os.pardir, 'empty for dir', i_file)
#         if os.path.exists(new_path):
#             print('\tПеремещение невозможно, т.к. папка с таким названием уже существует!')
#         else:
#             os.rename(i_file, new_path)
#             print('\t- перемещена в папку "empty for dir"')
#             count += 1
#
# print(f'\nВсего перемещено папок: {count}')
# 6 ==========================================================================
'''2(e). Модуль os. Перемещение и переименование (с заменой) файла и папки из одного каталога в другой'''
# import os
#
# os.chdir('for test_7')
#
# new_path = os.path.join('empty for file', 'For example_1.txt')
# os.replace('For example_1.txt', new_path)
#
# new_path = os.path.join('empty for file', 'For example_1.txt')
# os.replace('[SW.BAND] For example_1.txt', new_path)
#
# new_path = os.path.join('empty for dir', 'For example 1')
# os.replace('For example 1', new_path)
#
# new_path = os.path.join('empty for dir', 'For example 1')
# os.replace('[SW.BAND] For example 1', new_path)

# 7 ==========================================================================
'''2(f) Модуль os. Переименование и перемещение файлов и папок с помощью функции renames()'''
# import os
#
# os.chdir('for test_8')
#
# # new_path = os.path.join('empty', '2', '3', '4', '2.txt')
# # os.renames('1.txt', new_path)
#
# # new_path = os.path.join('empty', '10', '11', '12')
# # os.renames('1', new_path)
#
# os.renames(os.path.join('1', '2', '3'), os.path.join('4', '5', '6'))
# 8 ==========================================================================
'''3(а). Модуль shutil, копирование файла в другой файл или другую папку'''
# import os
# import shutil
#
# os.chdir('for test_9')

# Функция
# def copy_files(src, dst, start, stop):
#     fnames = [f'{i}.jpg' for i in range(start, stop)]
#     for fname in fnames:
#         src_file = os.path.join(src, fname)
#         dst_file = os.path.join(dst, fname)
#         shutil.copy2(src_file, dst_file)
#
# copy_files('f_1', 'f_2', 1, 3)


# path_1 = shutil.copy('f_1\\1.jpg', 'f_2')
# print(path_1)

# path_1 = shutil.copy('1.txt', '2.txt')
# path_2 = shutil.copy('1.txt', 'f_1')

# path_1 = shutil.copy('f_1', 'f_2')  # Целиком папку (пустая она или нет) в другую папку так не скопируешь!
# print(path_1)

# path_1 = shutil.copy2('1.txt', '2.txt')
# path_2 = shutil.copy2('1.txt', 'f_1')

# path_1 = shutil.copyfile('1.txt', '2.txt')
# path_2 = shutil.copyfile('1.txt', 'f_1')
# path_3 = shutil.copyfile('f_1\\1.jpg', '3.jpg')

# print(path_1, path_2, sep='\n')
# 9 ==========================================================================
'''3(b). Модуль shutil, '''
# import os
# import shutil
#
# os.chdir('for test_10')
#
# shutil.move('1.txt', 'f_2')       # Перемещение файла в другую папку
#
# shutil.move('1.txt', '1.txt')       # Переименование файла в текущей рабочей директории на то же имя что и было
#
# path = os.path.join('f_1', '1.jpg') # Путь к другой папке
# shutil.move(path, '3.jpg')          # Перемещение c переименованием файла из другой папки в текущий рабочий каталог
#
# shutil.move('f_1', 'f_2')         # Перемещение непустой папки в другую папку
#
# shutil.move('f_3', 'f_1')         # Перемещение пустой папки в другую папку
#
# shutil.move('1.txt', '2.txt')     # Переименование файла в текущей рабочей директории
#
# shutil.move('1.txt', os.path.join('f_2', '2.txt'))   # Перемещение с переименованием файла в другую папку
#
# shutil.move('f_4', 'f_5')   # Переименование папки в текущей рабочей директории
#
# shutil.move(os.path.join('f_2', 'f_4'), os.path.join('f_2', 'f_5'))   # Переименование папки в другой директории
#
# shutil.move('1.txt', 'f_10')   # Перемещение файла в несуществующую папку
# 10 ==========================================================================
'''3(c). Модуль shutil, удаление непустой папки (всего дерева каталогов)'''
# import os
# import shutil
#
# os.chdir('for test_11')
#
# shutil.rmtree('f_1')
# shutil.rmtree(os.path.join('f_2', '1', '2'))
# shutil.rmtree('f_2')
# shutil.rmtree('1.txt')
# 11 ==========================================================================
'''3(d). Модуль shutil, копирование папок с помощью функции copytree()'''
# import os
# import shutil
#
# os.chdir('for test_12')
#
# path = shutil.copytree('f_2', 'f_1')   # Копирование содержимого непустой папки f_2 в пустую папку f_1
# print(path)
#
# shutil.copytree("f_2", "f_2/test1")   # Копирование содержимого папки f_2 внутрь неё самой же но в подпапку test1
#
# shutil.copytree("f_2", "f_1/f_2")   # Копирование содержимого папки f_2 внутрь папки f_1, но в подпапку f_2, равносильно копированию папки f_2 в папку f_1
# shutil.copytree("f_2", os.path.join('f_1', 'f_2'))   # Копирование содержимого папки f_2 внутрь папки f_1, но в подпапку f_2, равносильно копированию папки f_2 в папку f_1
#
# shutil.copytree("f_2", "f_1")   # Это выдаст ошибку
#
# shutil.copytree('1.txt', 'f_1')   # Это выдаст ошибку
#
# shutil.copytree('f_3', 'f_1')   # Копирование содержимого пустой папки f_3 в другую пустую папку f_1
# 12 ==========================================================================
'''3(d). Модуль os, создание папок с помощью функции mkdir() и makedirs()'''
# import os
#
# os.chdir('for test_13')
#
# os.mkdir('f_1')     # Создание папки f_1
# os.mkdir(os.path.join('f_2', 'f_3'))     # Выдаст ошибку FileExistsError
#
# os.makedirs(os.path.join('f_2', 'f_3', 'f_4'))     # Создание дерева каталогов

'''3(e). Cоздание пустого файла'''
# import os
#
# os.chdir('for test_13')

# file = open('empty.txt', 'x')
# file.write('Hello World!')
# file.close()
# 13 ==========================================================================
'''3(f). Модуль os, Рекурсивный обход папок с помощью функции walk()'''
# import os
#
# os.chdir('for test_14')

# Вар 1
# for current_dir, dirs, files in os.walk("."):   # Передаем в качестве аргумента текущую директорию ("." - означает именно ее)
#     print(current_dir, dirs, files)             # Выведем, что получается
# print()

# for tup in os.walk(".", topdown=False):
#     print(tup)

# Вар 2
# path = os.path.abspath(os.path.curdir)
# for dirpath, dirnames, filenames in os.walk(path):
    # Вар 1
    # print('Выбранный каталог:', dirpath)
    # print('\tВложенные папки:', dirnames)
    # print('\tФайлы в папке:', filenames)
    # Вар 2
    # print('Текущая директория: ' + dirpath)
    # # цикл по поддиректориям текущей директории
    # for subdir in dirnames:
    #     print('\tДочерняя директория: ' + subdir)
    # # цикл по файлам текущей директории
    # for file in filenames:
    #     print('\tФайл в директории: ' + file)

# Вар 3
# path = os.path.abspath(os.path.curdir)
# for root, dirs, files in os.walk(path):
#     print(f'Директория: <<{root}>>', "занимает", end=" ")
#     print(sum([os.path.getsize(os.path.join(root, name)) for name in files]), end=" ")
#     print("байт. Содержит", len(files), "файла")
#     if 'CVS' in dirs:
#         # не просматриваем каталог `CVS`
#         dirs.remove('CVS')
# 14 ==========================================================================
'''4(a). Модуль glob '''

# import glob
# import os
#
# p = 'c:/windows'
# # Вар 1
# e = [x for x in os.listdir(p) if os.path.isfile(os.path.join(p, x)) and os.path.splitext(x)[-1] == '.exe']
# print(e)
# # Вар 2
# # Используя модуль glob это можно сделать красивее и проще т.к. он предназначен для
# # поиска файлов по патернам (шаблонам)
# print(glob.glob1(p, '*.exe'))       # Список экзешников
# print(glob.glob1(p, '*[0-9].exe'))  # Список экзешников имя кот. заканчивается на цифры

# Вар 3
# import glob
# import os
#
# os.chdir('for test_15')
#
# print(glob.glob(r'D:\Works of Skillbox\1. Python Basic\22\for test_15\*.txt'))
# print()
# path_1 = os.path.join('2', '3', '4', '*.txt')
# path_2 = os.path.join('2', '3', '4', '*[0-9].txt')
# path_3 = os.path.join('2', '3', '4', '[0-9]*.txt')
# path_4 = os.path.join('2', '3', '4', '[a-z].txt')
#
# for i_path in glob.iglob(path_1):
#     print(os.path.abspath(i_path))
# print()
# for i_path in glob.iglob(path_2):
#     print(os.path.abspath(i_path))
# print()
# for i_path in glob.iglob(path_3):
#     print(os.path.abspath(i_path))
# print()
# for i_path in glob.iglob(path_4):
#     print(os.path.abspath(i_path))
# 15 ==========================================================================
'''4(b). Модуль glob '''
# import glob
# import os
#
# os.chdir('for test_16/test')
#
# print(glob.glob('*.txt'))
# print(glob.glob('*/'))
# print(glob.glob('*/*.txt'))
# print(glob.glob('*/*/'))
# print(glob.glob('*/*/*.txt'))
# print(glob.glob('*/*/*/*.txt'))
# print(glob.glob('*/*/*/*.txt', recursive=True))
# 16 ==========================================================================
'''4(c). Модуль glob '''
# import glob
# import os
#
# os.chdir('for test_16/test')

# print(glob.glob('*.gif'))
# print(glob.glob('.c*'))

# print(glob.glob('./[0-9].*'))
# print(glob.glob('*.gif'))
# print(glob.glob('?.gif'))

# Поиск файлов по шаблону *.txt во всех каталогах и подкаталогах (т.е. рекурсивный
# поиск файлов), начиная с текущего каталога, т.к. в pathname указан отн-ный путь
# print(glob.glob('**/*.txt', recursive=True))

# Рекурсивный поиск (т.е. во всех каталогах и подкаталогах) файлов и папок
# print(glob.glob('**', recursive=True))

# Рекурсивный поиск всех папок, начиная с текущего рабочего каталога
# print(glob.glob('**/', recursive=True))

# Рекурсивный поиск всех папок, начиная с текущего рабочего каталога, но с
# предварительной прибавкой компонента пути ./
# print(glob.glob('./**/', recursive=True))
# 17 ==========================================================================
'''4(d). Модуль glob '''
# import glob
# import os
#
# os.chdir('for test_16')
#
# print(glob.glob('*/*'))
#
# for name in glob.glob("some folder/*"):
#     print(name)
# print()
# print(glob.glob('some folder/subdir/*'))
# print(sorted(glob.glob('some folder/*/*')))
# 18 ==========================================================================
'''4(e). Модуль glob '''
# import os
# from glob import glob
#
# os.chdir('for test_16')
#
# for i_path in glob(os.getcwd() + "/*/"):
#     print(i_path)

# import time
# print(time.ctime(os.path.getmtime('2.txt')))
# print(time.ctime(os.path.getmtime('../for test_16')))
# 19 ==========================================================================
'''5(a). Модуль pathlib '''
# import os
# from pathlib import *
#
# os.chdir('PATHLIB/test_1')
#
# current_dir = Path.cwd()
# home_dir = Path.home()
#
# print(current_dir)
# print(home_dir)
# ==========================================================================
# import pathlib
#
# current_dir = pathlib.Path.cwd()
# home_dir = pathlib.Path.home()
#
# print(current_dir)
# print(home_dir)
# 20 ==========================================================================
'''5(b). Модуль pathlib '''
# import os
#
# os.chdir('PATHLIB/test_1')
#
# outpath = os.path.join(os.getcwd(), 'output')
# os.mkdir(outpath)
# outpath_file = os.path.join(outpath, 'sample.txt')
#
# file = open(outpath_file, 'x')
# file.write('Hello World!')
# file.close()
# 21 ==========================================================================
'''5(c). Модуль pathlib '''
# import os
#
# os.chdir('PATHLIB/test_1')
#
# if not os.path.exists(os.path.join(os.getcwd(), 'output')):
#     os.mkdir(os.path.join(os.getcwd(), 'output'))
#
# file = open(os.path.join(os.path.join(os.getcwd(), 'output'), 'sample.txt'), 'w')
# file.write('Hello World!')
# file.close()
# 22 ==========================================================================
'''5(d). Модуль pathlib '''
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_2')

# if not os.path.exists(Path.cwd() / 'output'):
#     os.mkdir(Path.cwd() / 'output')
# with open(Path.cwd() / 'output' / 'sample.txt', 'w') as file:
#     file.write('Hello World!')
# 23 ==========================================================================
'''5(e). Модуль pathlib '''
# import os
#
# os.chdir('PATHLIB/test_3')
# path = os.path.join(os.getcwd(), 'f_1')
# if os.path.isdir(path):
#     os.rmdir(path)
# ==========================================================================
# import os
# import pathlib
#
# os.chdir('PATHLIB/test_3')
# path = pathlib.Path.cwd() / 'f_1'
# if path.is_dir():
#     path.rmdir()
# 24 ==========================================================================
'''5(f). Модуль pathlib '''
# import os
#
# os.chdir('PATHLIB/test_4')
#
# outpath = os.path.join(os.getcwd(), 'output')           # Создадим путь к папке output
# outpath_tmp = os.path.join(os.getcwd(), 'output.tmp')   # Создадим путь к файлу output.tmp
# print(outpath_tmp)
#
# if os.path.getsize(outpath_tmp):     # Если размер файла output.tmp не ноль (ноль-False, любое число-True):
#     os.rename(outpath_tmp, outpath)  # то переименовываем его с output.tmp в output (т.е. удаляем расширение)
# else:
#     os.remove(outpath_tmp)           # иначе удаляем файл output.tmp
# ==========================================================================
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_4')
#
# outpath = Path.cwd() / 'output'           # Создадим путь к папке output
# outpath_tmp = Path.cwd() / 'output.tmp'   # Создадим путь к файлу output.tmp
#
# if outpath_tmp.stat().st_size:    # Если размер файла output.tmp не ноль (ноль-False, любое число-True):
#     outpath_tmp.rename(outpath)   # то переименовываем его с output.tmp в output (т.е. удаляем расширение)
# else:
#     outpath_tmp.unlink()             # иначе удаляем файл output.tmp
# 25 ==========================================================================
'''5(g). Модуль os (протестил передачу списка в функцию os.path.join()) '''
# import os
#
# path_list_1 = ['PATHLIB', 'test_3']           # Список компонентов 1-го пути
# path_chg_1 = os.path.join(*path_list_1, '')   # Объединим компоненты списка path_list_1 в один путь с разделителем os.sep между компонентами
# print(path_chg_1)

# path_list_2 = ('f_2', 'f_3')                   # Кортеж компонентов 2-го пути
# path_list_2 = ('f_2', os.path.abspath('f_3'))  # Кортеж компонентов 2-го пути
# path_chg_2 = os.path.join(path_chg_1, *path_list_2, 'f_5')  # Объединим путь и компоненты списка path_list_2 в единый путь. М/у путем path_chg_1 и компонетами path_chg_2 ставится разделитель os.sep
# path_chg_2 = os.path.join('f_1', 'E:', os.sep, 'f_5')
# print(path_chg_2)
# os.makedirs(path_chg_2)  # Создадим дерево каталогов согласно сформированному пути path_chg_2
# 26 ==========================================================================
'''5(h). Модуль pathlib '''
# from pathlib import Path

# root = Path('/')
# subdirs = ['usr', 'local']
# usr_local = root.joinpath(*subdirs)
# print(usr_local)  #=>  \usr\local

# root_1 = Path('ocean')
# root_2 = Path('sea')
# usr_local = root_1.joinpath(root_2)
# print(usr_local)  #=>  ocean\sea

# root = Path('')
# subdirs = ['usr', 'local']
# usr_local = root.joinpath(*subdirs)
# print(usr_local)  #=>  usr\local

# subdirs_1 = ['ocean', 'sea', 'shark']
# root = Path(*subdirs_1)
# print(root)  #=>  ocean\sea\shark
# subdirs_2 = ('usr', 'local')
# usr_local = root.joinpath(*subdirs_2)
# print(usr_local)  #=>  ocean\sea\shark\usr\local

# p_1 = Path('/ocean')
# print(p_1)
# p_2 = p_1 / 'shark'
# print(p_2)

# print(Path())

# p = Path('ocean')
# usr_local = p.joinpath('usr', 'local')
# print(usr_local)  #=>  ocean\usr\local
# 27 ==========================================================================
'''5(i). Модуль pathlib '''
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_5/')

# p = Path("ocean").glob('*.txt')
# print(next(p))

# for txt_path in Path("ocean").glob('*.txt'):
#     print(txt_path)

# for txt_path in Path("ocean").glob('**/*.txt'):
#     print(txt_path)
#
# for txt_path in Path("ocean").rglob('*.txt'):
#     print(txt_path)

# top_xlsx_files = Path.cwd().glob('*.txt')
# all_xlsx_files = Path.cwd().rglob('*.txt')
# print(top_xlsx_files)
# print(all_xlsx_files)
# 28 ==========================================================================
'''5(j). Модуль pathlib '''
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_5/ocean')

# path = Path('.')
#
# subdirs = []
# files = []
#
# for x in path.iterdir():        # перебираем файлы и папки по пути path
#
#     if x.is_dir():              # условие проверки является ли объект каталогом
#         subdirs.append(str(x))  # используем ф-цию str для перобразования объекта в строку и уже ее добавим в список
#     else:
#         files.append(str(x))
#
# print(subdirs)
# print(files)
# ==========================================================================
# p = Path('.', 'tides.txt')
# for child in p.iterdir():
#     print(child)
# 29 ==========================================================================
'''5(k). Модуль pathlib '''
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_5')
#
# # path_1 = os.path.join('ocean', 'wive.txt')
# # path_2 = os.path.abspath(path_1)
# # print(path_1)   # => ocean\wive.txt
# # print(path_2)   # => D:\Works of Skillbox\1. Python Basic\22\PATHLIB\test_5\ocean\wive.txt
#
# p_1 = Path('ocean') / 'wive.txt'    # А можно и так: p_1 = Path('ocean', 'wive.txt')
# p_2 = p_1.resolve()     # Это аналог path_2 = os.path.abspath(path_1)
# print(p_1)   # => ocean\wive.txt
# print(p_2)   # => D:\Works of Skillbox\1. Python Basic\22\PATHLIB\test_5\ocean\wive.txt
# 29 ==========================================================================
'''5(l). Модуль pathlib '''
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_5')
#
# path = Path("ocean/animals")
# print(path.exists())  # True
# path = Path("ocean/tides.txt")
# print(path.exists())  # True
# path = Path("sea")
# print(path.exists())  # False
# path = Path("tides.txt")
# print(path.exists())  # False
# 30 ==========================================================================
'''5(m). Модуль pathlib '''
# from pathlib import Path
#
# wave = Path("ocean", "wave.txt")
# print('Полный путь:', wave)              #=> ocean/wave.txt
# print('Полное имя файла:', wave.name)    #=> wave.txt
# print('Расширение файла:', wave.suffix)  #=> .txt
# print('Только имя файла:', wave.stem)    #=> wave
# path = Path("ocean", "animals")
# print('Имя папки:', path.name)           #=> animals
# 31 ==========================================================================
'''5(n). Модуль pathlib '''
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_5')

# file_path = Path("text.txt")
# if file_path.exists() and file_path.is_file():
#     with file_path.open(encoding='utf-8') as f:
#         print(f.readlines())
# ==========================================================================
# p = Path('my_text_file.txt')
# data = 'Тут можно написать любые текстовые данные'
# print(p.write_text(data))   # => 41
# print(len(data))            # => 41
# print(p.read_text())        # => Тут можно написать любые текстовые данные
# ==========================================================================
# path = Path.cwd() / 'text.txt'
# print(path.read_text(encoding='utf-8'))
# # => Тут какой то текст...
# # => И привет Всем!
# ==========================================================================
# p = Path('text_2.txt')
# p.write_text('Образец данных для записи в файл')
# 32 ==========================================================================
'''5(o). Архивирование и разархивирование файлов'''
# import os, zipfile
#
# os.chdir('PATHLIB/test_6/extract from archive')
#
# # zip_file = zipfile.ZipFile('files.zip', 'r')
# # zip_file.extractall()
# # zip_file.close()
#
# # Эквивалентно
#
# with zipfile.ZipFile('files.zip') as zip_file:
#     zip_file.extractall()
# ==========================================================================
# import os, zipfile, glob
#
# os.chdir('PATHLIB/test_6/extract from archive')
#
# extract_dir = 'extract_dir'
# zf = zipfile.ZipFile('files.zip')
# zf.extractall(extract_dir)
# zf.close()
# for file in glob.glob(extract_dir + '/**', recursive=True):
#     print(file)
# ==========================================================================
# import os, zipfile
#
# os.chdir('PATHLIB/test_6/extract from archive')
#
# with zipfile.ZipFile('files.zip') as zf:
#     print(zf.namelist())
#     for name in zf.namelist():
#         print(name)
# ==========================================================================
# import os, zipfile
#
# os.chdir('PATHLIB/test_6/extract from archive')
#
# with zipfile.ZipFile('files.zip') as zip_file:
#     zip_file.extract('1/2/4.txt', 'extract_dir_2')
#     zip_file.extract('1.txt', 'extract_dir_2')
# ==========================================================================
# import os, zipfile
#
# os.chdir('PATHLIB/test_6/extract from archive')
#
# with zipfile.ZipFile('files.zip') as zf:
#     zf.printdir()
# ==========================================================================
# import os, zipfile
#
# os.chdir('PATHLIB/test_6/extract from archive')
#
# with zipfile.ZipFile('files.zip') as zf:
#     byte_text = zf.read('1.txt')
#     text = zf.read('2.txt')
#     print(byte_text.decode('utf-8'))
#     print(byte_text)
#     print(text)
#     print(text.decode('utf-8'))
# ==========================================================================
# import os
# import zipfile
#
# os.chdir('PATHLIB/test_6/add in archive')
#
# with zipfile.ZipFile('files_w.zip', mode='w') as zf:
#     zf.write('1.txt', arcname='1_1.txt',
#              compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
# ==========================================================================
# import zipfile, os, glob
#
# file_dir = glob.glob('PATHLIB/test_6/add in archive/**', recursive=True)
#
# with zipfile.ZipFile('PATHLIB/test_6/add in archive/files_w.zip', mode='w',
#                      compression=zipfile.ZIP_DEFLATED) as zf:
#     for file in file_dir:
#         if os.path.basename(file) != 'files_w.zip':   # Если наш архив есть среди файлов, то не включать его в новый архив
#             zf.write(file)
# ---------------
# import zipfile, os, glob
#
# os.chdir('PATHLIB/test_6/add in archive')
#
# file_dir = glob.glob('**', recursive=True)
#
# with zipfile.ZipFile('files_w.zip', mode='w',
#                      compression=zipfile.ZIP_DEFLATED) as zf:
#     for file in file_dir:
#         if os.path.basename(file) != 'files_w.zip':
#             zf.write(file)
# ==========================================================================
# import os
# from pathlib import Path
# from zipfile import ZipFile
#
# os.chdir('PATHLIB/test_6/add in archive')

# # Создадим zip-архива, содержащий все текстовые файлы содержащиеся во всех папках и подпапках
# with ZipFile('text_files.zip', 'w') as file:
#     for txt_file in Path().rglob('*.txt'):
#         print(f"* Файл: {txt_file.name} добавлен в zip-архив")
#         file.write(txt_file)

# * Файл: 1.txt добавлен в zip-архив
# * Файл: 2.txt добавлен в zip-архив
# * Файл: 3.txt добавлен в zip-архив

# Создание zip-архива, содержащего все файлы в директории
# with ZipFile('text_files.zip', 'w') as file:
#     for i_elem in Path().rglob('*'):
#         if i_elem.name != 'text_files.zip':
#             print(f"* Элемент: «{i_elem.name}» добавлен в zip-архив")
#             file.write(i_elem)
# ==========================================================================
# import os, zipfile
#
# os.chdir('PATHLIB/test_6/add in archive')
#
# with zipfile.ZipFile('text_files.zip', 'w',
#                      compression=zipfile.ZIP_DEFLATED) as zf:
#     for root, dirs, files in os.walk('.'):
#         print(root, dirs, files)
#         for file in files:
#             print('--------')
#             print(os.path.join(root, file))
#             if os.path.basename(file) != 'text_files.zip':
#                 zf.write(os.path.join(root, file))
#         print('=======================')
# ==========================================================================
# import os, zipfile
#
# os.chdir('PATHLIB/test_6/add in archive')
#
# with zipfile.ZipFile('text_files.zip', 'w') as zf:
#     for folder, dirs, files in os.walk('.'):
#         for file in files:
#             if file.endswith('.txt'):
#                 zf.write(os.path.join(folder, file), compress_type=zipfile.ZIP_DEFLATED)
# ==========================================================================
'''Лирическое отступление'''
# import os
#
# p_1 = 'archive/test/a.txt'
# p_2 = 'archive/test/../test/a.txt'    # ".." - на 1 уровень выше
# print(p_1)
# print(p_2)
# path_1 = os.path.realpath(p_1)
# path_2 = os.path.realpath(p_2)
# print(path_1)
# print(path_2)
# ==========================================================================
# import os, zipfile
#
# os.chdir('PATHLIB/test_6/add in archive')
#
# text = 'Это новый текстовый файл в архиве.'
# filename = 'ReadMe.txt'
#
# # добавляем текстовый файл в архив
# with zipfile.ZipFile('test.zip', mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
#     zf.writestr(filename, text)
#
# # прочитаем добавленный текстовый файл в архив
# with zipfile.ZipFile('test.zip') as zf:
#     byte_text = zf.read(filename)
#     print(byte_text.decode('utf-8'))
# ==========================================================================
# import os, zipfile
#
# os.chdir('PATHLIB/test_6/add in archive')
#
# file_list = os.listdir('.')     # Список файлов формируется до создания архивного файла
#                                 # поэтому дальше обход файла T.zip при добавлении всех
#                                 # файлов в архив не нужен
#
# with zipfile.ZipFile('T.zip', mode='x', compression=zipfile.ZIP_DEFLATED) as zf:
#     for file in file_list:
#         zf.write(file)
# 33 ==========================================================================
'''5(p). Модуль pathlib '''
# from pathlib import Path
#
# p_1 = Path('/usr/bin/python3/')
# path_components_1 = p_1.parts
# print(path_components_1)      #=> ('\\', 'usr', 'bin', 'python3')
#
# p_2 = Path('C:/Program Files/PSF')
# path_components_2 = p_2.parts
# print(path_components_2)      #=> ('C:\\', 'Program Files', 'PSF')
#  ==========================================================================
# from pathlib import Path
#
# path_components = ('usr', 'bin', 'python3')
# path = Path(*path_components)
# print(path)      #=> usr\bin\python3
#  ==========================================================================
# from pathlib import Path
#
# print(Path('C:/Program Files/').drive)  # 'C:'
# print(Path('/Program Files/').drive)    # ''
# print(Path('/etc').drive)               # ''
#  ==========================================================================
# from pathlib import Path
#
# print(Path('C:/Program Files/').anchor)   # 'C:\'
# print(Path('C:Program Files/').anchor)    # 'C:'
# print(Path('/Program Files/').anchor)     # '\'
# print(Path('Program Files/').anchor)      # ''
#  ==========================================================================
# from pathlib import Path
# print(Path('a/b.py').match('*.py'))         # True
# print(Path('/a/b/c.py').match('b/*.py'))    # True
# print(Path('/a/b/c.py').match('a/*.py'))    # False
# print(Path('/a/b/c.py').match('a/*/*.py'))  # True

# print(Path('/a.py').match('/*.py'))      # True
# print(Path('/a/b.py').match('/*.py'))    # False
# print(Path('a/b.py').match('/*.py'))     # False
# print(Path('/a/b.py').match('/*/*.py'))  # True
#  ==========================================================================
# from pathlib import Path
#
# print(Path('/a/b').is_absolute())           # False
# print(Path('a/b').is_absolute())            # False
#
# print(Path('c:/a/b').is_absolute())         # True
# print(Path('/a/b').is_absolute())           # False
# print(Path('c:').is_absolute())             # False
# print(Path('//some/share').is_absolute())   # True
#  ==========================================================================
# from pathlib import Path
#
# p = Path('c:\\windows')
# print(type(p))             # <class 'pathlib.WindowsPath'>
# print(str(p))              # 'c:\windows'
# print(p.as_posix())        # 'c:/windows'
#  ==========================================================================
# from pathlib import Path
#
# p = Path('c:/foo/bar/setup.py')
# print(p.parents)        # <WindowsPath.parents>
# print(p.parents[0])     # PureWindowsPath('c:/foo/bar')
# print(p.parents[1])     # PureWindowsPath('c:/foo')
# print(p.parents[2])     # PureWindowsPath('c:/')
#
# # Двигаемся вверх по директории
# for up in p.parents:
#     print(up)
#
# # c:\foo\bar
# # c:\foo
# # c:\
#  ==========================================================================
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_5')
#
# print(Path('ocean').is_dir())              # True
# print(Path('my_text_file.txt').is_dir())   # False
#  ==========================================================================
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_5')
#
# print(Path('ocean').is_file())              # False
# print(Path('my_text_file.txt').is_file())   # True
# 34 ==========================================================================
'''5(q). Модуль pathlib '''
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_7')
#
# p = Path('some/mydir')
# p.mkdir(parents=True, exist_ok=True)  # Создаст все папки в пути даже если они уже существуют
# 35 ==========================================================================
'''5(r). Модуль pathlib '''
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_7')
#
# Path('some/mydir').mkdir(parents=True, exist_ok=True)
# Path('some/mydir/example.txt').touch()
# 36 ==========================================================================
'''5(s). Модуль pathlib '''
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_7')
#
# Path('some/mydir_1').mkdir(parents=True, exist_ok=True)
# print(Path('some/mydir_1').exists())    # True
# Path('some/mydir_1').rmdir()
# print(Path('some/mydir_1').exists())    # False
# 36 ==========================================================================
'''5(t). Модуль pathlib '''
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_7')
#
# Path('some/mydir_2').mkdir(parents=True, exist_ok=True)
# Path('some/mydir_2/example.txt').touch()          # Создаем пустой файл
# print(Path('some/mydir_2/example.txt').exists())  #=> True. Проверяем существует ли он
# Path('some/mydir_2/example.txt').unlink()         # Удаляем файл
# print(Path('some/mydir_2/example.txt').exists())  #=> False. Проверяем существует ли он
# 36 ==========================================================================
'''5(u). Модуль pathlib '''
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_8')
#
# p = Path('foo.txt')
# p.open('w').write('some text')
# target = Path('bar.txt')  # Переименование файла
# p.rename(target)    # Переименует файл, если файла bar.txt еще не существует
# # ==========================================================================
# p = Path('foo_1')
# p.mkdir(parents=True, exist_ok=True)  # Создаст все папки в пути даже если они уже существуют
# target = Path('bar_1')  # Переименование директории
# p.rename(target)    # Переименует папку, если папки bar_1 еще не существует
# # ==========================================================================
# p = Path('foo.txt')
# p.open('w').write('some text')
# target = Path('other catalog/bar.txt')
# p.rename(target)    # Т.к. каталог p и target отличаются, по произойдет перемещение с переименованием
# # ==========================================================================
# p = Path('foo_1')
# p.mkdir(parents=True, exist_ok=True)  # Создаст все папки в пути даже если они уже существуют
# target = Path('other catalog/bar_1')  # Переименование директории
# p.rename(target)    # Переименует папку, если папки bar_1 еще не существует
# 36 ==========================================================================
'''5(v). Модуль pathlib '''
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_8')

# Path('file_0.txt').open('w')   # Создадим пустой файл
#
# with Path('file_1.txt').open('w') as file_1:  # Создадим пустой файл
#     file_1.write('')    # Или можно просто указать ...
#
# with Path('file_2.txt').open('w') as file_2:  # Создадим непустой файл
#     file_2.write('some text')

# Path('file_3.txt').write_text('some text')   # Создадим непустой файл
# 36 ==========================================================================
'''5(w). Модуль pathlib '''
# import os
# from pathlib import Path
#
# os.chdir('PATHLIB/test_9')
#
# p = Path('foo.txt')
# p.write_text('Тут какой то текст')
# print(p.is_file())          # True
# target = Path('bar.txt')
# p.replace(target)           # Переименует файл с заменой даже если он уже существует
# print(p.is_file())          # False
# print(p)                    # 'foo.txt'
# # ==========================================================================
# p = Path('foo_1')
# p.mkdir(parents=True, exist_ok=True)  # Создаст все папки в пути даже если они уже существуют
# print(p.is_dir())          # True
# p.replace('bar_1')         # Переименует папку с заменой даже если она существует
# print(p.is_dir())          # False
# print(p)                   # 'foo_1'
# # ==========================================================================
# p = Path('foo.txt')
# p.write_text('Тут какой то текст')
# p.replace('other catalog/bar.txt')   # Т.к. каталоги отличаются, по произойдет перемещение с переименованием и заменой даже если файл уже существует
# # ==========================================================================
# p = Path('foo_1')
# p.mkdir(parents=True, exist_ok=True)  # Создаст все папки в пути даже если они уже существуют
# p.replace('other catalog/bar_1')   # Т.к. каталоги отличаются, по произойдет перемещение с переименованием и заменой даже если папка уже существует
