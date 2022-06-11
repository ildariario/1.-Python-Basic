'''Работа за преподавателем'''
# Task 1
#
# def ask_user(questions, complaint, retries):
#     while True:
#         answer = input(questions).lower()
#         if answer == 'да':
#             return 1
#         if answer == 'нет':
#             return 0
#         retries -= 1
#         if retries == 0:
#             print('Количество попыток истекло.')
#             break
#         print(complaint)
#         print('Осталось попыток:', retries)
#
# ask_user('Вы действительно хотите выйти? ',
#          'Неверный ввод. Пожалуйста, введите да или нет',
#          4)
# ask_user('Удалить файл? ',
#          'Неверный ввод. Пожалуйста, введите да или нет',
#          4)
# ask_user('Записать файл? ',
#          'Неверный ввод. Пожалуйста, введите да или нет',
#          4)

# Task 2

# def ask_user(questions,
#              complaint='Неверный ввод. Пожалуйста, введите да или нет',
#              retries=4):
#     while True:
#         answer = input(questions).lower()
#         if answer == 'да':
#             return 1
#         if answer == 'нет':
#             return 0
#         retries -= 1
#         if retries == 0:
#             print('Количество попыток истекло.')
#             break
#         print(complaint)
#         print('Осталось попыток:', retries)
#
# ask_user('Вы действительно хотите выйти? ')
# ask_user('Удалить файл? ')
# ask_user('Записать файл? ')

# Task 3

# def ask_user(questions,
#              complaint='Неверный ввод. Пожалуйста, введите да или нет',
#              retries=4):
#     while True:
#         answer = input(questions).lower()
#         if answer == 'да':
#             return 1
#         if answer == 'нет':
#             return 0
#         retries -= 1
#         if retries == 0:
#             print('Количество попыток истекло.')
#             break
#         print(complaint)
#         print('Осталось попыток:', retries)
#
# ask_user('Вы действительно хотите выйти? ')
# ask_user('Удалить файл? ', 'Так удалить или нет?')
# ask_user('Записать файл? ', retries=2)

# Home Work
# 1 ==========================================================================
'''Задача 1. Работа с файлом
Вы пишете небольшое приложение для работы с файлами. Реализуйте функцию, которая может 
принимать на вход три аргумента: вопрос пользователю (на который нужно ответить да или нет), 
сообщение о неправильном вводе и количество попыток. Вопрос — обязательный позиционный 
аргумент, остальные — со значениями по умолчанию. При корректном ответе функция может 
возвращать что угодно — например, число 1 при ответе «да» или 0 при ответе «нет».
В основной программе вызовите функцию минимум три раза: только с вопросом, с вопросом и 
сообщением об ошибке, с вопросом и количеством попыток.

Пример работы программы:
Вы действительно хотите выйти? что
Неверный ввод. Пожалуйста, введите 'да' или 'нет'.
Осталось попыток: 3
Вы действительно хотите выйти? да
Удалить файл? не знаю
Так удалить или нет? 
Осталось попыток: 3
Удалить файл? нет
Записать файл? ага
Неверный ввод. Пожалуйста, введите 'да' или 'нет'.
Осталось попыток: 1
Записать файл? да
'''
# def ask_usr(question,
#             complaint="Неверный ввод. Пожалуйста, введите 'да' или 'нет'.",
#             retries=4):
#     while True:
#         answer = input(question)
#         if answer == 'да':
#             return 1
#         if answer == 'нет':
#             return 0
#         retries -= 1
#         if retries == 0:
#             print('Количество попыток истекло.')
#             break
#         print(complaint, f'Осталось попыток: {retries}', sep='\n')
#
# ask_usr('Вы действительно хотите выйти? ')
# ask_usr('Удалить файл? ', 'Так удалить или нет?')
# ask_usr('Записать файл? ', retries=2)
# 2 ==========================================================================
'''Задача 2. Накопление значений
При работе со значениями по умолчанию и изменяемыми типами данных нужно знать и остерегаться 
ещё одной интересной штуки.
Напишите функцию с двумя аргументами: первый — число num, позиционный аргумент; второй — 
список lst, по умолчанию он пустой. В теле функции в список добавляется число num и сам 
список выводится на экран.
В основной программе вызовите функции три раза только с одним аргументом (числом), например так:
add_num(5)
add_num(10)
add_num(15)
И посмотрите, что произойдёт.
После этого сделайте значение lst по умолчанию None и поправьте функцию, чтобы она работала 
правильно.
'''
# def add_num(num, lst=[]):
#     lst.append(num)
#     print(lst)
#
#
# add_num(5)
# add_num(10)
# add_num(15)
# # -------------------------------
# def add_num(num, lst=None):
#     lst.append(num)
#     print(lst)
#
#
# some_list = []
# add_num(5, some_list)
# add_num(10, some_list)
# add_num(15, some_list)
# 3 ==========================================================================
'''Задача 3. Помощь другу
Нашего друга попросили написать функцию, которая на вход принимает список всякого мусора. 
Ему нужно подготовить из этого списка список словарей, чтобы его коллеги смогли дальше 
продолжить обработку данных. Вот список правил, что нужно сделать с изначальным списком:
Если в списке встретился словарь, то оставляем его.
Если в списке встретилась строка, то из неё нужно сделать словарь и положить его в итоговый 
список, например  “abc” → {“abc”: “abc”}.
С числами нужно сделать то же самое, что и со строками.
Всё остальное выкидываем из нашего списка.
Друг написал программу, но в ней ошибка, так как она что-то не то выводит :( Нужна ваша 
помощь, вот сама программа:
def create_dict(data, template=dict()):
    if isinstance(data, dict):
        return data
    if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
        return template[data] = data

def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        new_list.append(create_dict(i_element))
    return new_list

data = [“sad”, {“sds”: 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data)
print(data)

Исправьте программу и убедитесь, что всё работает верно.
'''
# # Вариант 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def create_dict(new_elem):
#     if isinstance(new_elem, dict):
#         return new_elem
#     elif isinstance(new_elem, int) or isinstance(new_elem, float) or isinstance(new_elem, str):
#         new_dict = {}
#         new_dict[new_elem] = new_elem
#         return new_dict
#
#
# def data_preparation(old_list):
#     new_list = []
#     for i_element in old_list:
#         elem = create_dict(i_element)
#         if elem:
#             new_list.append(elem)
#     return new_list
#
#
# data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
# data = data_preparation(data)
# print(data)

# Вариант 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def create_dict(old_list, new_list=None):
#     for i_elem in old_list:
#         if isinstance(i_elem, int) or isinstance(i_elem, float) or isinstance(i_elem, str):
#             new_dict = dict()
#             new_dict[i_elem] = i_elem
#             new_list.append(new_dict)
#         elif isinstance(i_elem, dict):
#             new_list.append(i_elem)
#     return new_list
#
#
# data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
# data = create_dict(data, [])
# print(data)
