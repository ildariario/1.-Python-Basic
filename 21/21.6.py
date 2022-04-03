# Task 1


# Task 2


# Task 3


# Home Work
# 1 ==========================================================================
# Вариант 1
# def seq(n, i=1):
#     if i <= n:
#         print(i, end=' ')
#         seq(n, i+1)
#
#
# num = int(input('До какого значения нужно вывести числа? '))
# seq(num)

# Вариант 2
# def seq(n, i=1, lst=None):
#     if lst is None:
#         lst = []
#     if i <= n:
#         lst.append(i)
#         # print(i, end=' ')
#         seq(n, i+1, lst)
#     return lst
#
#
# num = int(input('До какого значения нужно вывести числа? '))
# print(seq(num))
# 2 ==========================================================================
# Вариант 1 (без использования циклов (с помощью рекурсии) так и не смог сделать)
# def zipp(seq_1, seq_2):
#     seq_1 = list(seq_1)
#     seq_2 = list(seq_2)
#     pairs = ((seq_1[i_elem], seq_2[i_elem]) for i_elem in range(min(len(seq_1), len(seq_2))))
#     return pairs
#
#
# sequence_1 = 'abcd'
# sequence_2 = (10, 20, 30)
# print(zipp(sequence_1, sequence_2))
# for i_value in zipp(sequence_1, sequence_2):
#     print(i_value)
#
# sequence_3 = [2, 3, 4, 5]
# sequence_4 = {20, 30, 40, 50, 60}
# print(zipp(sequence_3, sequence_4))
# for i_value in zipp(sequence_3, sequence_4):
#     print(i_value)
#
# sequence_5 = 'abcd'
# sequence_6 = {'aa': 50, 'bb': 60, 'cc': 70}
# print(zipp(sequence_5, sequence_6))
# for i_value in zipp(sequence_5, sequence_6):
#     print(i_value)


# Вариант 2
# def zipp(*args):
#     for index in range(min(len(args[0]), len(args[1]))):
#         yield args[0][index], args[1][index]
#
#
# s_1 = 'abcd'
# s_2 = (10, 20, 30)
#
# print(zipp(s_1, s_2))
# print(list(zipp(s_1, s_2)))
# for i_value in zipp(s_1, s_2):
#     print(i_value)
# 3 ==========================================================================
# Вариант 1 (без рекурсии)
# def fibo(num, lst=None):
#     if lst is None:
#         lst = [1, 1]
#     if num < 2:
#         print('Число:', 1)
#     else:
#         for i in range(2, num):
#             lst.append(sum(lst))
#             lst.pop(0)
#         print('Число:', lst[1])
#
#
# num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
# fibo(num_pos)

# Вариант 2 (с использованием рекурсии)
# def fibonacci(n):
#     if n in (1, 2):    # или if n == 1 or n == 2:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
# print('Число:', fibonacci(num_pos))
# 4 ==========================================================================
# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
# def search_of_key(struct, *args, curr_lvl=0):
#     if curr_lvl < args[1]:
#         curr_lvl += 1
#         if args[0] in struct:
#             return struct[args[0]]
#         for i_value in struct.values():
#             if isinstance(i_value, dict):
#                 result = search_of_key(i_value, args[0], args[1], curr_lvl=curr_lvl)
#                 if result:
#                     break
#         else:
#             result = None   # Если ключ в структуре сайта так и не был найден, то вернуть в основную прогу None
#         return result
#
#
# key = input('Введите искомый ключ: ')
# choice = input('Хотите ввести уровень, до которого будет просматриваться структура? (Y/N) ')
# if choice.lower() == 'y':
#     depth = int(input('Введите глубину поиска в структуре сайта: '))
# else:
#     depth = 1000
#
# finded_key = search_of_key(site, key, depth)
# if finded_key:
#     print(finded_key)
# else:
#     if depth < 1000:
#         print('Ключа {} в структуре сайта на глубине вложенности {} нет!'.format(key, depth))
#     else:
#         print('Ключа {} в структуре сайта нет!'.format(key))
# 5 ==========================================================================
# Вариант 1
# def calculating_math_func(data, fact_list={}):
#     if data not in fact_list:
#         result = 1
#         for index in range(1, data + 1):
#             result *= index
#         fact_list[data] = result
#     else:
#         result = fact_list[data]
#     result /= data ** 3
#     result = result ** 10
#     return result
#
# print(calculating_math_func(3))
# print(calculating_math_func(4))
# print(calculating_math_func(5))
# print(calculating_math_func(4))
# print(calculating_math_func(3))
#
# Вариант 2 (Это если нужно сохранять факториалы во внешнем, конкретном словаре)
# def calculating_math_func(data):
#     if data in factorials:  # если факториал в словаре присваеваем переменной result его значение
#         result = factorials[data]
#     else:
#         result = 1
#         for index in range(1, data + 1):
#             result *= index
#         factorials[data] = result  # иначе находим факториал и добавляем его значение в словарь
#     result /= data ** 3
#     result = result ** 10
#     return result
#
#
# factorials = {}  # создаем словарь всех найденных факториалов
# print(calculating_math_func(3))
# print(calculating_math_func(4))
# print(calculating_math_func(4))
# print(calculating_math_func(3))
# print(factorials)
# 6 ==========================================================================
# Вариант 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import copy
#
# site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам телефон недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на телефон',
#             'div': 'Купить',
#             'p': 'Продать'
#         }
#     }
# }
#
# def new_site(struct, name, bol=True):
#     if bol:
#         struct = copy.deepcopy(struct)
#     if not isinstance(struct, dict):
#         if 'телефон' in struct:
#             tmp_lst = struct.split()
#             index = tmp_lst.index('телефон')
#             tmp_lst.insert(index, name)
#             tmp_lst.remove('телефон')
#             return ' '.join(tmp_lst)
#     else:
#         for i_key, i_value in struct.items():
#             struct[i_key] = new_site(i_value, name, False)
#     return struct
#
#
# n = int(input('Сколько сайтов: '))
#
# for _ in range(n):
#     product_name = input('Введите название продукта для нового сайта: ')
#     print('\nСайт для {}:\n{}\n'.format(product_name, new_site(site, product_name)))
# print('Исходная структура сайта была такой:\n{}'.format(site))
#
# Вариант 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# site = {
#     'html': {
#         'head': {
#             'title': 'Куплю/продам телефон недорого'
#         },
#         'body': {
#             'h2': 'У нас самая низкая цена на телефон',
#             'div': 'Купить',
#             'p': 'Продать'
#         }
#     }
# }
#
# def new_site(struct, name):
#     new_struct = {}
#     if not isinstance(struct, dict):
#         if 'телефон' in struct:
#             tmp_lst = struct.split()
#             index = tmp_lst.index('телефон')
#             tmp_lst.insert(index, name)
#             tmp_lst.remove('телефон')
#             return ' '.join(tmp_lst)
#         else:
#             return struct
#     else:
#         for i_key, i_value in struct.items():
#             new_struct[i_key] = new_site(i_value, name)
#     return new_struct
#
#
# n = int(input('Сколько сайтов: '))
#
# for _ in range(n):
#     product_name = input('Введите название продукта для нового сайта: ')
#     print('\nСайт для {}:\n{}\n'.format(product_name, new_site(site, product_name)))
# print('А исходная структура сайта была такой:\n{}'.format(site))
# 7 ==========================================================================
# def sum(*args, result=0):
#     if isinstance(args[0], list):
#         iter_list = args[0]
#     else:
#         iter_list = args
#     for i_elem in iter_list:
#         if not isinstance(i_elem, list):
#             result += i_elem
#         else:
#             result += sum(i_elem)
#     return result
#
#
# print(sum([[1, 2, [3]], [1], 3]))
# print(sum(1, 2, 3, 4, 5))
# 8 ==========================================================================
# Вариант 1 мой вариант ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def other_list(lst):
#     for i_elem in lst:
#         if not isinstance(i_elem, list):
#             sec_list.append(i_elem)
#         else:
#             other_list(i_elem)
#
#
# sec_list = []
# nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
#
# other_list(nice_list)
# print(sec_list)
#
# Вариант 2 мой вариант ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def other_list(lst, sec_list=None):
#     if sec_list == None:
#         sec_list = []
#     for i_elem in lst:
#         if not isinstance(i_elem, list):
#             sec_list.append(i_elem)
#         else:
#             other_list(i_elem, sec_list)
#     return sec_list
#
#
# nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
#
# result = other_list(nice_list)
# print(result)

# Вариант 3 мой вариант ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def other_list(lst, sec_list=[], bool_4_last_return=True):
#     copy_lst = lst.copy()   # или copy_lst = lst[:]
#     while copy_lst:
#         if not isinstance(copy_lst[0], list):
#             tmp_elem = copy_lst.pop(0)
#             sec_list.append(tmp_elem)
#         else:
#             other_list(copy_lst[0], sec_list, False)
#             del copy_lst[0]  # или copy_lst.remove([]) или copy_lst[:1] = []
#     if bool_4_last_return:
#         return sec_list
#
#
# nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
#
# result = other_list(nice_list)
# print('Исходный список:', nice_list)
# print('Выпрямленный список:', result)
#
# # Вариант 4 c ресурса https://pythonist.ru/vypryamlenie-spiskov-pri-pomoshhi-rekursii/
# def flatten(nice_list):  # flatten - выпрямлять
#     if nice_list == []:
#         return nice_list
#     if isinstance(nice_list[0], list):
#         return flatten(nice_list[0]) + flatten(nice_list[1:])
#     return nice_list[:1] + flatten(nice_list[1:])
#
#
# nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
# print("Выпрямленный список: ", flatten(nice_list))
'''
Объяснение работы программы
1. Инициализируем переменную s списком, в котором содержатся вложенные списки.
2. Передаем этот список в рекурсивную функцию flatten() для преобразования в обычный список.
3. Базовым условием рекурсии будет равенство входящего списка пустому списку. В этом случае 
возвращается пустой список и дальнейшие вызовы рекурсивной функции не осуществляются.
4. В противном случае проверяется, является ли первый элемент списка вложенным списком или 
обычным элементом списка. Проверка осуществляется при помощи функции isinstance(s[0], list).
5. Если элемент списка тоже список, то он целиком передается нашей рекурсивной функции в 
качестве аргумента и к этому прибавляется остальная часть основного списка, которую мы 
также передаем в функцию в качестве аргумента. А именно: flatten(s[0]) + flatten(s[1:].
6. Если же элемент списка обычное число, то он выводится в результат в виде списка из одного 
элемента и к нему прибавляется рекурсивная функция, в которой в качестве аргумента остальная 
часть списка. А именно: s[:1] + flatten(s[1:]. Таким образом мы можем «распрямить» списки 
со сколь угодно глубокими вложениями.
7. После окончания работы функции выпрямленный список выводится на печать.
8. Конец.
'''
# 9 ==========================================================================
# # Решение Т.Ф. Хирьянова ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def hanoi(n, i, k):     # i - стержень с которого ; k - на который надо перекладывать
#     if n == 1:
#         print(f'Переложить ДИСК №1: с {i}-го на {k}-й стержень')
#     else:
#         tmp = 6 - i - k
#         hanoi(n - 1, i, tmp)
#         print(f'Переложить ДИСК №{n}: с {i}-го на {k}-й стержень')
#         hanoi(n - 1, tmp, k)
#
# hanoi(3, 1, 2)

# # Решение Горской Елены Сергеевны ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def move(n, start, finish):     # start - стержень с которого ; finish - на который надо перекладывать
#     if n == 1:
#         print(f'Переложить ДИСК №1: с {start}-го на {finish}-й стержень')
#     else:
#         tmp = 6 - start - finish
#         move(n - 1, start, tmp)
#         print(f'Переложить ДИСК №{n}: с {start}-го на {finish}-й стержень')
#         move(n - 1, tmp, finish)
#
# move(3, 1, 3)

# # Решение в терминах самой задачи SkillBox на основе вышеприведенных решений ~~~~~~~~~~~~~~
def move(n, x, y):     # x - стержень с которого ; y - на который надо перекладывать
    if n == 1:
        print(f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
    else:
        tmp = 6 - x - y
        move(n - 1, x, tmp)
        print(f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
        move(n - 1, tmp, y)

n = int(input('Введите количество дисков: '))
x = int(input('На каком из трех стержней будет находится пирамидка? '))
while True:
    y = int(input(f'На какой стержень (кроме {x}-го) хотите переложить пирамидку? '))
    if y == x:
        print('На этот стержень нельзя перемещать пирамидку т.к. она на нем уже стоит!')
    else:
        break

move(n, x, y)