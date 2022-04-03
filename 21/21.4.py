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
def create_dict(old_list, new_list=None):
    for i_elem in old_list:
        if isinstance(i_elem, int) or isinstance(i_elem, float) or isinstance(i_elem, str):
            new_dict = dict()
            new_dict[i_elem] = i_elem
            new_list.append(new_dict)
        elif isinstance(i_elem, dict):
            new_list.append(i_elem)
    return new_list


data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
data = create_dict(data, [])
print(data)
# 4 ==========================================================================

# 5 ==========================================================================

# 6 ==========================================================================

# 7 ==========================================================================

# 8 ==========================================================================

# 9 ==========================================================================

# 10 ==========================================================================

# 11 ==========================================================================

# 12 ==========================================================================

# 13 ==========================================================================

# 14 ==========================================================================

# 15 ==========================================================================