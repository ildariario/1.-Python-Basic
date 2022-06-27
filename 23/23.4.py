"""Работа за преподавателем"""
# Task 1

# # Вар 1
# sym_sum = 0
# try:
#     people_file = open('people.txt', 'r')
#     for line_count, i_line in enumerate(people_file):
#         length = len(i_line)
#         if i_line.endswith('\n'):
#             length -= 1
#         if length < 3:
#             raise BaseException('Длина {} строки меньше 3 символов'.format(line_count+1))
#         sym_sum += length
#     people_file.close()
#
# except FileNotFoundError:
#     print('Файл не найден.')
# finally:
#     print('Найденная сумма символов:', sym_sum)
#
# # Вар 2
# sym_sum = 0
# line_count = 0
# try:
#     people_file = open('people.txt', 'r')
#     for i_line in people_file:
#         length = len(i_line)
#         line_count += 1
#         if i_line.endswith('\n'):
#             length -= 1
#         if length < 3:
#             raise BaseException
#         sym_sum += length
#     people_file.close()
#
# except FileNotFoundError:
#     print('Файл не найден.')
# except BaseException:
#     print('Длина {} строки меньше 3 символов'.format(line_count+1))
# finally:
#     print('Найденная сумма символов:', sym_sum)

# Task 2

# names_list = []
#
# while True:
#     try:
#         name = input('Введите имя: ')
#         if not name.isalpha():
#             raise TypeError
#         names_list.append(name)
#         if len(names_list) == 5:
#             print('Место закончилось!')
#             break
#     except TypeError:
#         print('Ты чего ввёл?')
#
# names_file = open('names.txt', 'w', encoding='utf-8')
# names_file.write('\n'.join(names_list))
# names_file.close()
# print('Программа закончена, запись завершена.')

# Task 3

# Вариант 1
# names_list = []
#
# while True:
#     try:
#         name = input('Введите имя: ')
#         if name.lower() == 'error':
#             names_list = []
#             raise BaseException('Ты сломал программу!')
#         if not name.isalpha():
#             raise TypeError
#         names_list.append(name)
#         if len(names_list) == 5:
#             print('Место закончилось!')
#             break
#     except TypeError:
#         print('Ты чего ввёл?')
#
# names_file = open('names.txt', 'w', encoding='utf-8')
# names_file.write('\n'.join(names_list))
# names_file.close()
# print('Программа закончена, запись завершена.')

# Вариант 2
# names_list = []
#
# while True:
#     try:
#         name = input('Введите имя: ')
#         if name.lower() == 'error':
#             raise BaseException('Ты сломал программу!')
#         if not name.isalpha():
#             raise TypeError
#         names_list.append(name)
#         if len(names_list) == 5:
#             print('Место закончилось!')
#             break
#     except TypeError:
#         print('Ты чего ввёл?')
#     except BaseException:
#         names_list = []
#         print('Введено стоп-слово.')
#         raise  # raise ValueError('Пожалуйста, не вводите стоп-слово...')
#
#
# names_file = open('names.txt', 'w', encoding='utf-8')
# names_file.write('\n'.join(names_list))
# names_file.close()
# print('Программа закончена, запись завершена.')

# Home Work
# 1 ==========================================================================
'''Задача 1. Имена
В базе данных одной компании есть баг (или, может быть, фича): если ввести туда 
имя сотрудника меньше чем из трёх букв, то база сломается и упадёт. Как компания 
принимает на работу людей, например, с китайскими именами, непонятно.
Дан файл people.txt, в котором построчно хранится N имён пользователей. 
Напишите программу, которая берёт количество символов в каждой строке файла и в 
качестве ответа выводит общую сумму. Если в какой-либо строке меньше трёх символов 
(не считая литерала \n), то вызывается ошибка, и программа завершается.
'''
# sum_sym = 0
# line_count = 0
# try:
#     file = open('people.txt', 'r')
#     for i_line in file:
#         line_count += 1
#         length = len(i_line)
#         if i_line.endswith('\n'):
#             length -= 1
#         sum_sym += length
#         if length < 3:
#             raise BaseException
# except BaseException:
#     print(f'В строке {line_count} меньше трёх символов!')
# else:
#     print('Найденная сумма символов:', sum_sym)
# 2 ==========================================================================
'''Задача 2. Логирование
Возможно, вы замечали, что некоторые программы не просто выдают ошибку и 
закрываются, но и записывают эту ошибку в файл. Таким образом проще сформировать 
отчёт об ошибках, а значит, программисту будет проще их исправить. Это называется 
логированием ошибок.
Дан файл words.txt, в котором построчно записаны слова. Необходимо определить 
количество слов, из которых можно получить палиндром (привет предыдущим модулям). 
Если в строке встречается число, то программа выдаёт ошибку ValueError и записывает 
эту ошибку в файл errors.log
'''


def is_poly(string, index):
    char_dict = {}
    for i_sym in string:  # Заполнение словаря char_dict в формате (символ: количество таких символов в строке)
        try:
            if i_sym.isdigit():
                raise ValueError
            char_dict[i_sym] = char_dict.get(i_sym, 0) + 1  # Прием добавления 1 к значениям уже имеющихся в словаре ключей
        except ValueError:
            print(f'В строке {index+1} присутствует число {i_sym}!')
            file_out.write(f'\t-в строке {index+1} присутствует число {i_sym}!' + '\n')
            return False

    odd_count = 0  # Подсчет количества нечетных значений символов в строке/словаре
    for i_value in char_dict.values():
        if i_value % 2 != 0:
            odd_count += 1

    return odd_count <= 1


poly_count = 0
file_inp = open('words.txt', 'r')
file_out = open('errors.log', 'a', encoding='utf-8')
file_out.write(f'Очередной запуск программы:\n')
for i_ind, i_word in enumerate(file_inp):
    if is_poly(i_word.removesuffix('\n'), i_ind):  # .removesuffix - удаляет \n, если он есть в конце строки
        poly_count += 1
print('Количество слов, из которых можно получить палиндром:', poly_count)
file_inp.close()
file_out.close()
