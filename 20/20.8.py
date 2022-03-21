# Task 1

# Task 2

# Task 3

# Home Work
# 1 ==========================================================================
# def f(dict):
#     lst = [j_list for _, i_dict in dict.items() for j_keys, j_list in i_dict.items() if j_keys == 'interests']
#     lst = [j_elem for i_list in lst for j_elem in i_list]
#     length = [len(j_surname) for _, i_dict in dict.items() for j_keys, j_surname in i_dict.items() if j_keys == 'surname']
#     return lst, sum(length)
#
#
# students = {
#     1: {
#         'name': 'Bob',
#         'surname': 'Vazovski',
#         'age': 23,
#         'interests': ['biology, swimming']
#     },
#     2: {
#         'name': 'Rob',
#         'surname': 'Stepanov',
#         'age': 24,
#         'interests': ['math', 'computer games', 'running']
#     },
#     3: {
#         'name': 'Alexander',
#         'surname': 'Krug',
#         'age': 22,
#         'interests': ['languages', 'health food']
#     }
# }
#
# pairs = []
# for i_ID, i_dict in students.items():
#     pairs += [i_ID, i_dict['age']]    # pairs.extend([i, students['age']])
# print('Cписок пар:', pairs)
#
# print(f(students))
# 2 ==========================================================================

# 3 ==========================================================================

# 4 ==========================================================================

# 5 ==========================================================================
# data_family = {
#     ('Сидоров', 'Никита'): 35,
#     ('Сидорова', 'Алина'): 34,
#     ('Сидоров', 'Павел'): 10,
#     ('Валитов', 'Эль'): 34,
#     ('Валитова', 'Гуля'): 25,
#     ('Валитова', 'Сылу'): 2,
#     ('Ибрагимов', 'Виталий'): 50,
#     ('Ибрагимова', 'Лена'): 45,
#     ('Ибрагимова', 'Вика'): 22
# }
#
# surname = input('Введите фамилию: ').lower()
#
# for (i_surname, i_name), i_age in data_family.items():
#     if surname[:-1] in i_surname.lower():
#         print(i_surname, i_name, i_age)
# 6 ==========================================================================
# from random import randint
#
# random_lst = [randint(0, 10) for _ in range(10)]
# print('Оригинальный список: ', random_lst)
#
# # Вар 1
# new_lst = []
# while random_lst:
#     temp_lst = [i_elem for i_elem in random_lst[:2]]
#     new_lst.append(tuple(temp_lst))
#     random_lst[:2] = []
# print(new_lst)
#
# # Вар 2
# for _ in random_lst:
#     temp_lst = [i_elem for i_elem in random_lst[:2]]
#     random_lst[:2] = []
#     random_lst.append(tuple(temp_lst))
# print(random_lst)
#
# # Вар 3
# random_lst = list(zip(random_lst[0::2], random_lst[1::2]))
# print('Новый список: ', random_lst)
# 7 ==========================================================================

# 8 ==========================================================================
# contacts_dict = dict()
#
# while True:
#     flag = False
#     action = input('Выберите действие: \nadd - добавить контакт;\nsearch - найти человека в телефонной книге по фамилии; \nq - выйти: ')
#     if action == 'add':
#         name_surname = tuple(input('Введите имя и фамилию ч/з пробел: ').lower().split())
#         number = int(input('Введите номер телефона: '))
#         if name_surname not in contacts_dict:
#             contacts_dict[name_surname] = number
#             print('\nТелефонная книга:')
#             for (i_name, i_surname), i_number in contacts_dict.items():
#                 print('\t', i_name, i_surname, ':', i_number, end='\n\n')
#         else:
#             print('\nТакой контакт уже есть в телефонной книге!')
#     elif action == 'search':
#         if contacts_dict:
#             surname_cont = input('Введите фамилию контакта который хотите найти: ').lower()
#             for (i_name, i_surname), i_number in contacts_dict.items():
#                 if i_surname == surname_cont:
#                     print('Такой контакт есть:', i_name, i_surname, ':', i_number, end='\n\n')
#                     flag = True
#             if not flag:
#                 print('Такого контакта нет!', end='\n\n')
#         else:
#             print('Телефонная книга пока пуста!')
#     elif action == 'quit' or action == 'q':
#         break
#     else:
#         print('Несуществующая команда! Начните заново.', end='\n\n')
#
# if contacts_dict:
#     print('\nТелефонная книга:')
#     for name_surname, number in contacts_dict.items():
#         print('\t', name_surname[0], name_surname[1], ':', number)
# else:
#     print('Телефонная книга пока пуста!')
# 9 ==========================================================================
# results = {}
#
# # заполняем словарь только лучшими результатами игроков
# N = int(input('Сколько записей вносится в протокол? '))
# print('Записи (результат и имя):')
# for i_log in range(N):
#     log = input(f'{i_log+1} запись: ').split()
#     if log[1] not in results:
#         results[log[1]] = [int(log[0]), i_log+1]
#     else:
#         if int(log[0]) > results[log[1]][0]:    # Если рез-ат лучше, то заменяем его в словаре
#             results[log[1]] = [int(log[0]), i_log+1]
#
# # На основе полученного выше словаря results формируем список из вложенных списков,
# # каждый из кот. содержит лучший результат каждого игрока
# result_list = [[i_name, i_score, i_log] for i_name, [i_score, i_log] in results.items()]
#
# # Сортировка списка result_list по правилу 3-4 соревнований.
# for i_index in range(len(result_list) - 1):
#     if result_list[i_index][1] < result_list[i_index + 1][1]:
#         result_list.insert(i_index, result_list.pop(i_index + 1))
#     else:
#         if result_list[i_index][1] == result_list[i_index + 1][1]:
#             if result_list[i_index][2] > result_list[i_index + 1][2]:
#                 result_list.insert(i_index, result_list.pop(i_index + 1))
#
# # Вывод результатов трёх лучших игроков
# print('\nИтоги соревнований:')
# for i_place in range(3):
#     print(f'{i_place+1} место: {result_list[i_place][0]} ({result_list[i_place][1]})')
# 10 ==========================================================================

# 11 ==========================================================================

# 12 ==========================================================================


# 13 ==========================================================================

# 14 ==========================================================================

# 15 ==========================================================================
