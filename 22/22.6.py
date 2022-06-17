# Home Work
# 1 ==========================================================================
'''Задача 1. Сумма чисел 2
Во входном файле numbers2.txt записано N целых чисел, которые могут быть разделены пробелами
и концами строк. Напишите программу, которая выводит сумму чисел в выходной файл answer2.txt.
Пример:
Содержимое файла numbers1.txt
     2

2
  2
         2

Содержимое файла answer.txt
8
'''
# file_inp = open('numbers1.txt', 'r')
# file_out = open('answer1.txt', 'w')
#
# list_1 = [int(j_sym) for i_string in file_inp for j_sym in i_string if j_sym != ' ' and j_sym != '\n']
# # Развертка list comprehensions (привел для наглядности):
# # for i_string in file_inp:
# #     for j_sym in i_string:
# #         if j_sym != ' ' and j_sym != '\n':
# #             list_1.append(int(j_sym))
# file_out.write(str(sum(list_1)))
# file_inp.close()
# file_out.close()
# 2 ==========================================================================
'''Задача 2. Дзен Пайтона
В файле zen.txt хранится так называемый Дзен Пайтона — текст философии программирования на 
языке Python. Выглядит он так:
----------------------------------------------------------------------------
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

На русском:
Красивое лучше, чем уродливое.
Явное лучше, чем неявное.
Простое лучше, чем сложное.
Сложное лучше, чем запутанное.
Плоское лучше, чем вложенное.
Разреженное лучше, чем плотное.
Читаемость имеет значение.
Особые случаи не настолько особые, чтобы нарушать правила.
При этом практичность важнее безупречности.
Ошибки никогда не должны замалчиваться.
Если они не замалчиваются явно.
Встретив двусмысленность, отбрось искушение угадать.
Должен существовать один и, желательно, только один очевидный способ сделать это.
Хотя он поначалу может быть и не очевиден, если вы не голландец [^1].
Сейчас лучше, чем никогда.
Хотя никогда зачастую лучше, чем прямо сейчас.
Если реализацию сложно объяснить — идея плоха.
Если реализацию легко объяснить — идея, возможно, хороша.
Пространства имён — отличная штука! Будем делать их больше!
----------------------------------------------------------------------------
Напишите программу, которая выводит на экран все строки этого файла в обратном порядке.
Кстати, попробуйте открыть консоль Python и ввести команду “import this”.

Результат работы программы:
Namespaces are one honking great idea -- let's do more of those!
If the implementation is easy to explain, it may be a good idea.
If the implementation is hard to explain, it's a bad idea.
Although never is often better than *right* now.
'''
# Вар 1
# zen_file = open('Дзен Пайтона.txt', 'r', encoding='utf-8')
# zen_list = [i_string for i_string in zen_file]
# zen_file.close()
# zen_list[0] = zen_list[0].replace('\n', '')
# zen_list[-1] += '\n'
# zen_list.reverse()
# rev_text = ''.join(zen_list)
# print(rev_text)

# Вар 2
# zen_file = open('Дзен Пайтона.txt', 'r', encoding='utf-8')
# zen_text = zen_file.read()
# zen_rev_list = zen_text.split('\n')[::-1]
# zen_rev = '\n'.join(zen_rev_list)
# print(zen_rev)
# 3 ==========================================================================
'''Задача 3. Дзен Пайтона 2
Напишите программу, которая определяет, сколько букв (латинского алфавита), слов и строк 
в файле zen.txt (который содержит всё тот же Дзен Пайтона). Выведите три найденных числа на экран.
Дополнительно: выведите на экран букву, которая встречается в тексте наименьшее количество раз.
'''
# letters_dict = {}
# symbols_exception = [',', ' ', '.', '\n', ':', '-', '*', "'", '!']
# words_count = 1     # Начинаем с единицы т.к. слов будет на единицу больше чем пробелов
# strings_count = 0
# zen_file = open('zen.txt', 'r')
# for i_string in zen_file:
#     strings_count += 1      # Счетчик строк
#     for i_sym in i_string.lower():
#         if i_sym not in letters_dict and i_sym not in symbols_exception:
#             letters_dict[i_sym] = 1
#         elif i_sym in letters_dict and i_sym not in symbols_exception:
#             letters_dict[i_sym] += 1
#         elif i_sym == ' ' or i_sym == '\n':     # Счетчик слов
#             words_count += 1
#
# zen_file.close()
# print(letters_dict)
# print('Количество букв:', sum(letters_dict.values()))
# print('Количество строк:', strings_count)
# print('Количество слов:', words_count)
#
# for i_letter, i_count in letters_dict.items():
#     if i_count == min(letters_dict.values()):
#         min_letter = i_letter
#         print(f'Буква "{min_letter}", встречается в тексте наименьшее количество раз: {i_count} раза')
# 4 ==========================================================================
'''Задача 4. Файлы и папки
Напишите программу, которая получает на вход путь до каталога (это может быть и просто корень 
диска) и выводит общее количество файлов и подкаталогов в нём. Также выведите на экран размер 
каталога в килобайтах (1 килобайт = 1024 байт).
Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех 
вложенных в него файлов. 

Результат работы программы на примере python_basic\Module14:
Размер каталога (в Кб): 8.373046875
Количество подкаталогов: 7
Количество файлов: 15
'''
# import os
#
#
# def get_size_dir(path, dir_size=0, f_count=0, d_count=0):
#     for i_elem in os.listdir(path):
#         i_path = os.path.join(path, i_elem)
#         if os.path.isfile(i_path):
#             dir_size += os.path.getsize(i_path)
#             f_count += 1
#         else:
#             d_count += 1
#             dir_size, f_count, d_count = get_size_dir(i_path, dir_size, f_count, d_count)
#     return dir_size, f_count, dir_count
#
#
# input_path = input('Введите путь до каталога: ')
# size, files_count, dir_count = get_size_dir(input_path)
#
# print(f'Размер каталога в Байтах: {size}, в КБ: {round(size / 1024, 2)}, в МБ: {round(size / 1024 / 1024, 2)}')
# print('Количество подкаталогов:', dir_count)
# print('Количество файлов:', files_count)
# 5 ==========================================================================
'''Задача 5. Сохранение
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
# import os
#
#
# def user_choice(text):
#     save_dir = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ')   # Папка для теста for_22.6_task_5/skillbox
#     folder_path = os.path.join(*save_dir.split(' '))      # Путь к папке куда нужно сохранить файл
#     if os.path.exists(folder_path):
#         file_name = '.'.join([input('Введите имя файла (без расширения .txt): '), 'txt'])    # Добавим к имени файла расширение
#         file_path = os.path.join(folder_path, file_name)
#         if os.path.exists(file_path):
#             flag = input('Файл с таким именем уже существует, хотите перезаписать файл (да/нет)? ')
#             if flag == 'да':
#                 file = open(file_path, 'w', encoding='utf-8')
#                 file.write(text)
#                 return 'Файл успешно перезаписан!'
#             else:
#                 return 'Файл с таким именем уже существует. Вы выбрали оставить старый вариант.'
#         else:
#             file = open(file_path, 'w', encoding='utf-8')
#             file.write(text)
#             return 'Файл успешно сохранён!'
#     else:
#         return 'Указанный из папок путь - не существует'
#
#
# text = input('Введите строку: ')
# action = user_choice(text)
# print(action)
# 6 ==========================================================================
'''Задача 6. Паранойя
Артуру постоянно кажется, что за ним следят и все хотят своровать «крайне важную информацию» 
с его компьютера, включая переписку с людьми. Поэтому он эти переписки шифрует. И делает это 
с помощью шифра Цезаря (чем веселит агента службы безопасности).
Напишите программу, которая шифрует содержимое текстового файла text.txt шифром Цезаря, при 
этом символы первой строки файла должны циклически сдвигаться на один, второй строки — на два, 
третьей строки — на три и так далее. Результат выведите в файл cipher_text.txt.
Пример:
Содержимое файла text.txt:
Hello
Hello
Hello
Hello

Содержимое файла cipher_text.txt:
Ifmmp
Jgnnq
Khoor
Lipps
'''
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# shift = 0
# file_input = open('text.txt', 'r', encoding='utf-8')
# file_output = open('cipher_text.txt', 'w', encoding='utf-8')
# for i_string in file_input:
#     shift += 1
#
#     # Вар 1 (но он не очень читабельный, зато покомпактнее)
#     # old_string = [(alphabet[(alphabet.index(i_sym.lower()) + shift) % len(alphabet)].upper() if i_sym.isupper() else
#     #                alphabet[(alphabet.index(i_sym.lower()) + shift) % len(alphabet)]) if i_sym.isalpha() else i_sym
#     #               for i_sym in i_string]
#     # new_string = ''.join(old_string)
#     # print(new_string, end='')
#
#     # Вар 2 (этот вариант более читабельный, он мне нравится больше)
#     new_string = ''
#     for i_sym in i_string:
#         if i_sym.isalpha():
#             if i_sym.isupper():
#                 new_string += alphabet[(alphabet.index(i_sym.lower()) + shift) % len(alphabet)].upper()
#             else:
#                 new_string += alphabet[(alphabet.index(i_sym.lower()) + shift) % len(alphabet)]
#         else:
#             new_string += i_sym
#
#     file_output.write(new_string)
# file_input.close()
# file_output.close()
# 7 ==========================================================================
'''Задача 7. Турнир
В файле first_tour.txt записано число K и данные об участниках турнира по настольной игре 
«Орлеан»: фамилии, имена и количество баллов, набранных в первом туре. Во второй тур проходят 
участники, которые набрали более K баллов в первом туре. 
Напишите программу, которая выводит в файл second_tour.txt данные всех участников, прошедших 
во второй тур, с нумерацией. 
В первой строке нужно вывести в файл second_tour.txt количество участников второго тура. 
Затем программа должна вывести фамилии, инициалы и количество баллов всех участников, 
прошедших во второй тур, с нумерацией. Имя нужно сократить до одной буквы. Список должен 
быть отсортирован по убыванию набранных баллов.
Пример:
Содержимое файла first_tour.txt:
80
Ivanov Serg 80
Segeev Petr 92
Petrov Vasiliy 98
Vasiliev Maxim 78

Содержимое файла second_tour.txt:
2
1) V. Petrov 98
2) P. Sergeev 92
'''

# Вариант 1 ----------------------------------------------------------------------------------------------------------
# file_input = open('first_tour.txt', 'r')
# file_output = open('second_tour.txt', 'w')
#
# strings_list = file_input.readlines()       # Создаем список элементы которого есть строки
# passing_score = int(strings_list.pop(0))    # Удаляем из этого списка проходной балл и присваиваем его переменной
# print(strings_list)

# for i_member in strings_list:               # Идем по списку с участниками
#     if int(i_member.split(' ')[2]) <= passing_score:   # Оставляем в списке только тех, чей балл > 80
#         strings_list.remove(i_member)
# print(strings_list)
#
# for i in range(len(strings_list)):          # Реализуем сортировку выбором участников по убыванию баллов
#     for j in range(i+1, len(strings_list)):
#         if int(strings_list[j].split(' ')[2]) > int(strings_list[i].split(' ')[2]):
#             strings_list[i], strings_list[j] = strings_list[j], strings_list[i]
# print(strings_list)
#
# for index, i_member in enumerate(strings_list):     # Меняем в каждом элементе списка имя с фамилией местами
#     strings_list[index] = i_member.split(' ')
#     strings_list[index][0], strings_list[index][1] = strings_list[index][1], strings_list[index][0]
#     strings_list[index][0] = strings_list[index][0][0] + '.'
#     strings_list[index].insert(0, f'{index+1})')    # Добавляем нумерацию участников
#     strings_list[index] = ' '.join(strings_list[index])
# print(strings_list)
#
# strings_list.insert(0, str(len(strings_list)) + '\n')   # Вставляем в список первым элементом кол-во участников 2 тура
# file_output.writelines(strings_list)    # Записываем каждый элемент готового списка в файл
# print(strings_list)
#
# file_input.close()
# file_output.close()
# Вариант 2 ----------------------------------------------------------------------------------------------------------
# file_input = open('first_tour.txt', 'r')
# file_output = open('second_tour.txt', 'w')
#
# strings_list = file_input.readlines()       # Создаем список элементы которого это строки файла first_tour.txt
# passing_score = int(strings_list.pop(0))    # Удаляем из этого списка проходной балл и присваиваем его переменной
# print(strings_list)
#
# strings_list_new = []
# for index, i_member in enumerate(strings_list):               # Идем по списку с участниками
#     if int(strings_list[index].split(' ')[2]) > passing_score:
#         surname, name, score = strings_list[index].split(' ')
#         strings_list_new.append(' '.join([name[0] + '.', surname, score]))      # Меняем местами имя с фамилией
# print(strings_list_new)   # => ['P. Segeev 92\n', 'V. Petrov 98\n']
#
# for i in range(len(strings_list_new)):          # Реализуем сортировку выбором участников по убыванию баллов
#     for j in range(i+1, len(strings_list_new)):
#         if int(strings_list_new[j].split(' ')[2]) > int(strings_list_new[i].split(' ')[2]):
#             strings_list_new[i], strings_list_new[j] = strings_list_new[j], strings_list_new[i]
# strings_list_new[-1] = strings_list_new[-1][:-len('\n')]    # Удаляем перенос строки в конце последнего элемента списка
# print(strings_list_new)  # => ['V. Petrov 98\n', 'P. Segeev 92']
#
# for index, i_member in enumerate(strings_list_new):
#     strings_list_new[index] = ' '.join([f'{index+1})', i_member])     # Добавляем нумерацию участников
# print(strings_list_new)  # => ['1) V. Petrov 98\n', '2) P. Segeev 92\n']
#
# strings_list_new.insert(0, str(len(strings_list_new)) + '\n')   # Вставляем в список первым элементом кол-во участников 2 тура
# file_output.writelines(strings_list_new)    # Записываем каждый элемент готового списка в файл
# print(strings_list_new)  # => ['2\n', '1) V. Petrov 98\n', '2) P. Segeev 92']
#
# file_input.close()
# file_output.close()
# Вариант 3 ----------------------------------------------------------------------------------------------------------
# def scoreSort(member):  # Функция для сортировки списка участников по баллам
#     return int(member.split()[2])  # Делим строку по пробелу и формируем список в котором 2-й элемент это баллы
#
#
# file_input = open('first_tour.txt', 'r')
# file_output = open('second_tour.txt', 'w')
#
# members_list = file_input.readlines()  # Создаем список элементы которого это строки файла first_tour.txt
# passing_score = int(members_list.pop(0))  # Удаляем из этого списка проходной балл и присваиваем его переменной
#
# new_members_list = [' '.join([members_list[index].split(' ')[1][0] + '.', members_list[index].split(' ')[0],
#                               members_list[index].split(' ')[2]]) for index, i_member in enumerate(members_list)
#                     if int(members_list[index].split(' ')[2]) > passing_score]  # Меняем имя и фамилию местами и сокращаем имя
#
# new_members_list.sort(key=scoreSort, reverse=True)  # reverse=True - сортировка по убыванию
#
# members_list = [' '.join([f'{index + 1})', i_member]) for index, i_member in enumerate(new_members_list)]   # Добавляем нумерацию участников
#
# members_list.insert(0, str(len(new_members_list)) + '\n')  # Вставляем в список 1-ым эл-том кол-во участников 2 тура
#
# file_output.writelines(members_list)  # Записываем каждый элемент готового списка в файл
#
# file_input.close()
# file_output.close()
# 8 ==========================================================================
'''Задача 8. Частотный анализ
Есть файл text2.txt, который содержит текст. Напишите программу, которая выполняет частотный 
анализ, определяя долю каждой буквы английского алфавита в общем количестве английских букв 
в тексте, и выводит результат в файл analysis.txt. Символы, не являющиеся буквами английского 
алфавита, учитывать не нужно. 
В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с тремя знаками в 
дробной части. Буквы должны быть отсортированы по убыванию их доли. Буквы с равной долей 
должны следовать в алфавитном порядке.
Пример:
Содержимое файла text.txt:
Mama myla ramu.

Содержимое файла analysis.txt:
a 0.333
m 0.333
l 0.083
r 0.083
u 0.083
y 0.083
'''
# Вариант 1 ---------------------------------------------------------------------------------
# import string
#
# file_input = open('text2.txt', 'r')
# file_output = open('analysis.txt', 'w')
#
# text = file_input.read()
#
# all_letters = [i_sym.lower() for i_sym in text if i_sym.lower() in string.ascii_lowercase]   # Список всех букв в тексте
# print(all_letters, '- cписок всех букв в тексте')
#
# sorted_unique_letters = sorted(set(all_letters))    # Сортируем уникальные буквы текста в алфавитном порядке
# print(sorted_unique_letters, '- cписок уникальных букв в тексте отсортированных в алфавитном порядке')
#
# frequency = [round(all_letters.count(i_letter)/len(all_letters), 3)
#              for i_letter in sorted_unique_letters]     # Создаем список содержащий доли уникальных букв в тексте
# print(frequency, '- доли букв в тексте')
#
# hist_letters_dict = dict(zip(sorted_unique_letters, frequency))  # Сшиваем в dict уникальные буквы и соотв-щие им доли
# print(hist_letters_dict, '- буквы и их доля в тексте отсортированные пока только в алфавитном порядке')
#
# sorted_hist_letters_dict = {i_key: str(hist_letters_dict[i_key])
#                             for i_key in sorted(hist_letters_dict, key=hist_letters_dict.get, reverse=True)}
# print(sorted_hist_letters_dict, '- буквы и их доля в тексте отсортированные по убыванию долей')
#
# file_output.writelines([' '.join(i_elem) + '\n'
#                         if list(sorted_hist_letters_dict.keys()).index(i_elem[0]) != len(sorted_hist_letters_dict.keys())-1
#                         else ' '.join(i_elem) for i_elem in sorted_hist_letters_dict.items()])
# file_input.close()
# file_output.close()
# Вариант 2 ---------------------------------------------------------------------------------
# import string
# def funcSort(list_elem):
#     return float(list_elem[1])
#
#
# file_input = open('text2.txt', 'r')
# file_output = open('analysis.txt', 'w')
#
# text = file_input.read()
#
# all_letters_list = [i_sym.lower() for i_sym in text if i_sym.lower() in string.ascii_lowercase]   # Список всех букв в тексте
# print(all_letters_list, '- cписок всех букв в тексте')
#
# sorted_unique_letters_list = sorted(set(all_letters_list))    # Отсортированный по алфавиту список уникальных букв
# print(sorted_unique_letters_list, '- отсортированный по алфавиту cписок уникальных букв в тексте')
#
# quantity_letters = [round(all_letters_list.count(i_letter)/len(all_letters_list), 3)
#                     for i_letter in sorted_unique_letters_list]     # Cписок долей
# print(quantity_letters, '- список долей соответствующих отсортированному по алфавиту cписку уникальных букв')
#
# hist_of_letters_list = list(zip(sorted_unique_letters_list, map(str, quantity_letters)))  # Список букв с долями
# print(hist_of_letters_list, '- список букв с долями отсортированный пока что только по алфавиту')
#
# hist_of_letters_list.sort(key=funcSort, reverse=True)   # Сортировка списка по частоте букв
# print(hist_of_letters_list, '- список букв с долями отсортированный по убыванию долей')
#
# file_output.writelines([' '.join(i_elem) + '\n'  # если элемент не последний, добавим перенос строки, иначе не добавим
#                         if hist_of_letters_list.index(i_elem) != len(hist_of_letters_list)-1 else ' '.join(i_elem)
#                         for i_elem in hist_of_letters_list])
# file_input.close()
# file_output.close()
# 9 ==========================================================================
'''Задача 9. Война и мир (необязательная)
Мало кто не знает про знаменитый роман Л. Н. Толстого «Война и мир». Это довольно объёмное 
произведение лежит в архиве voina-i-mir.zip. Напишите программу, которая подсчитает статистику 
по буквам (не только русского алфавита) в этом романе и выведет результат на экран (или в файл).
Результат должен быть отсортирован по частоте встречаемости букв (по возрастанию или убыванию).
Регистр символов имеет значение.
Постарайтесь написать программу так, чтобы для её работы не требовалась распаковка архива 
«вручную».
'''
import zipfile
import os

if os.path.exists('voina-i-mir.txt'):    # Если файл существует, удаляем его
    os.remove('voina-i-mir.txt')

zf = zipfile.ZipFile('voina-i-mir.zip', 'r')    # Распаковываем файл
zf.extractall()
zf.close()

extracted_file = open('voina-i-mir.txt', 'r')   # Т.к. файл имеет кодировку отличную от UTF-8 (а именно ANSI),
text = extracted_file.read()                    # мы его считываем
decoded_file = open('voina-i-mir.txt', 'w', encoding='utf-8')
decoded_file.write(text)                        # и перезаписываем этот файл с кодировкой UTF-8
extracted_file.close()
decoded_file.close()

alphabet = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

file_input = open('voina-i-mir.txt', 'r', encoding='utf-8')
file_output = open('statistics.txt', 'w', encoding='utf-8')

text = file_input.read()

letters_dict = {}
for i_letter in text:   # Заполняем новый словарь буквами и их частотой в тексте
    if i_letter in alphabet or i_letter in alphabet.upper():    # а можно просто: if i_letter.isalpha():
        if i_letter not in letters_dict:
            letters_dict[i_letter] = 0
        letters_dict[i_letter] += 1

sorted_letters_dict = {i_letter: str(letters_dict[i_letter])     # Формируем новый отсортированный по убыванию значений словарь
                       for i_letter in sorted(letters_dict, key=letters_dict.get, reverse=True)}     # Идем по списку ключей отсортированных по значениям по убыванию

print(f"Буква\t|\tЧастота")
file_output.write(f"Буква\t|\tЧастота\n")
for i_letter, i_frequency in sorted_letters_dict.items():
    print(f'  {i_letter}\t\t|\t {i_frequency}')
    file_output.write(f'  {i_letter}\t\t|\t {i_frequency}\t\n')

file_input.close()
file_output.close()
