# Разбоор ДЗ
"""Задача 9. Война и мир (необязательная)
Мало кто не знает про знаменитый роман Л. Н. Толстого «Война и мир». Это довольно объёмное
произведение лежит в архиве voina-i-mir.zip. Напишите программу, которая подсчитает статистику
по буквам (не только русского алфавита) в этом романе и выведет результат на экран (или в файл).
Результат должен быть отсортирован по частоте встречаемости букв (по возрастанию или убыванию).
Регистр символов имеет значение.
Постарайтесь написать программу так, чтобы для её работы не требовалась распаковка архива
«вручную».
"""


# Вар 1 (с помощью обычного словаря)-----------------------------------------------------------------------------
import zipfile


def unzip(archive):  # Распаковка zip архива
    zfile = zipfile.ZipFile(archive, 'r')
    for i_file_name in zfile.namelist():  # метод namelist - возвращает список имен файлов которые находятся в архиве
        zfile.extract(i_file_name)
    zfile.close()


def collect_stats(f_name):  # Формирование словаря содержащего буквы с их частотой в файле
    result = {}
    if f_name.endswith('.zip'):
        unzip(f_name)  # Распаковка zip архива
        f_name = ''.join((f_name[:-3], 'txt'))  # Изменим расширение с zip на txt, чтоб дальше в теле функции
    text_file = open(f_name, 'r', encoding='utf-8')  # работать с правильным именем файла
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
    text_file.close()

    return result


def print_stats(dictionary):  # Красивый вывод словаря
    print("+{:-^19}+".format('+'))
    print("|{: ^9}|{: ^9}|".format('буква', 'частота'))
    print("+{:-^19}+".format('+'))
    for char, count in dictionary.items():
        print("|{: ^9}|{: ^9}|".format(char, count))
    print("+{:-^19}+".format('+'))


def write_stats(dictionary):  # Красивый вывод словаря в файл statistics.txt
    file_output = open('statistics.txt', 'w', encoding='utf-8')
    file_output.write("+{:-^19}+\n|{: ^9}|{: ^9}|\n".format('+', 'буква', 'частота', '+'))
    for char, count in dictionary.items():
        file_output.write("|{: ^9}|{: ^9}|\n".format(char, count))
    file_output.write("+{:-^19}+".format('+'))
    file_output.close()


def sort_by_frequency(stats_dict):  # Функция сортирующая ключи словаря по убыванию значений
    sorted_values = sorted(set(stats_dict.values()), reverse=True)  # Формируем множество отсортированных уникальных
    sorted_dict = {}  # значений, чтоб не добавлять в словарь одни и те же значения по нескольку раз
    for i_value in sorted_values:
        for j_key in stats_dict.keys():
            if stats_dict[j_key] == i_value:
                sorted_dict[j_key] = i_value

    return sorted_dict


file_name = 'voina-i-mir.zip'
stats = collect_stats(file_name)  # Формирование словаря содержащего буквы с их частотой в файле
stats = sort_by_frequency(stats)  # Функция сортирующая ключи словаря по убыванию значений
print_stats(stats)  # Красивый вывод словаря на экран
write_stats(stats)  # Красивый вывод словаря в файл statistics.txt

# Вар 2 (с помощью модуля collection) ---------------------------------------------------------------------
# import collections
# import zipfile
#
#
# def unzip(archive):  # Распаковка zip архива
#     zfile = zipfile.ZipFile(archive, 'r')
#     for i_file_name in zfile.namelist():  # метод namelist - возвращает список имен файлов которые находятся в архиве
#         zfile.extract(i_file_name)
#     zfile.close()
#
#
# def collect_stats(f_name):  # Формирование словаря содержащего буквы с их частотой в файле
#     result = {}
#     if f_name.endswith('.zip'):
#         unzip(f_name)  # Распаковка zip архива
#         f_name = ''.join((f_name[:-3], 'txt'))  # Изменим расширение с zip на txt, чтоб дальше в теле функции
#     text_file = open(f_name, 'r', encoding='utf-8')  # работать с правильным именем файла
#     for i_line in text_file:
#         for j_char in i_line:
#             if j_char.isalpha():
#                 if j_char not in result:
#                     result[j_char] = 0
#                 result[j_char] += 1
#     text_file.close()
#
#     return result
#
#
# def print_stats(dictionary):  # Красивый вывод словаря на экран
#     print("+{:-^19}+".format('+'))
#     print("|{: ^9}|{: ^9}|".format('буква', 'частота'))
#     print("+{:-^19}+".format('+'))
#     for char, count in dictionary.items():
#         print("|{: ^9}|{: ^9}|".format(char, count))
#     print("+{:-^19}+".format('+'))
#
#
# def write_stats(dictionary):  # Красивый вывод словаря в файл statistics.txt
#     file_output = open('statistics.txt', 'w', encoding='utf-8')
#     file_output.write("+{:-^19}+\n|{: ^9}|{: ^9}|\n".format('+', 'буква', 'частота', '+'))
#     for char, count in dictionary.items():
#         file_output.write("|{: ^9}|{: ^9}|\n".format(char, count))
#     file_output.write("+{:-^19}+".format('+'))
#     file_output.close()
#
#
# def sort_by_frequency(stats_dict):  # Функция сортирующая ключи словаря по убыванию значений
#     sorted_values = sorted(set(stats_dict.values()), reverse=True)  # Создаем список отсортированных уникальных значений
#     sorted_dict = collections.OrderedDict()  # OrderedDict - это обычный, но упорядоченный словарь,
#     # т.е. он запоминает (хранит) позиции и поэтому позволяет правильно работать с сортировкой
#     for i_value in sorted_values:
#         for j_key in stats_dict.keys():
#             if stats_dict[j_key] == i_value:
#                 sorted_dict[j_key] = i_value
#
#     return sorted_dict
#
#
# file_name = 'voina-i-mir.zip'
# stats = collect_stats(file_name)  # Формирование словаря содержащего буквы с их частотой в файле
# stats = sort_by_frequency(stats)  # Функция сортирующая ключи словаря по убыванию значений
# print_stats(stats)  # Красивый вывод словаря на экран
# write_stats(stats)  # Красивый вывод словаря в файл statistics.txt
