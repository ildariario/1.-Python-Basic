# Task 1

# phonebook_list = [
#     ['Ваня', 88006663636],
#     ['Петя', 88005553535],
#     ['Лена', 88007773737],
# ]
#
# name = input('Введите имя: ')
#
# is_exist = False
# for i_person in phonebook_list:
#     if i_person[0] == name:
#         is_exist = True
#         print(i_person[1])
#         break
# if not is_exist:
#     print('Ошибка: человек с именем {0} не найден.'.format(name))

# Task 2

# phonebook_dict = {
#     'Ваня': 88006663636,
#     'Петя': 88005553535,
#     'Лена': 88007773737,
# }
# name = input('Введите имя: ')
# if name in phonebook_dict:
#     print(phonebook_dict[name])
# else:
#     print('Ошибка: человек с именем {0} не найден'.format(name))

# Task 3

# example = {}
# example = dict()
#
# example['Ваня'] = 10000
# print(example)
# example['Петя'] = 10000
# print(example)
# example['Ваня'] = 50000
# print(example)

# Task 3

# student_str = input('Введите информацию о студенте через пробел\n'
#                     '(имя, фамилия, город, место учебы, оценки):\n'
#                     )
#
# student_info = student_str.split()
# student = dict()
# student['Имя'] = student_info[0]
# student['Фамилия'] = student_info[1]
# student['Город'] = student_info[2]
# student['Место учебы'] = student_info[3]
# student['Оценки'] = []
#
# for i_grade in student_info[4:]:
#     student['Оценки'].append(int(i_grade))
# print(student)
# for i_info in student:
#     print(i_info, '-', student[i_info])

# Home Work
# 1 ==========================================================================
# num = int(input('Введите целое число: '))
# result = {}
#
# for i_elem in range(1, num + 1):
#     result[i_elem] = i_elem ** 2
#
# print(result)
# 2 ==========================================================================
# student_info = input('Введите Фамилию, Имя, Город, ВУЗ, Оценки '
#                      '(Всё вводится в одну строку через пробел):\n').split()
#
# student_dict = {}
#
# student_dict['Фамилия'] = student_info[0]
# student_dict['Имя'] = student_info[1]
# student_dict['Город'] = student_info[2]
# student_dict['ВУЗ'] = student_info[3]
# student_dict['Оценки'] = []
#
# for i_grade in student_info[4:]:
#     student_dict['Оценки'].append(i_grade)
# for i_info in student_dict:
#     print(i_info, '-', student_dict[i_info])
# 3 ==========================================================================
phonebook = {}

while True:
    print('Текущие контакты на телефоне:')
    for i_contact in phonebook:
        print(i_contact, phonebook[i_contact])

    name = input('\nВведите имя: ')
    phone_number = int(input('Введите номер телефона: '))
    phonebook[name] = phone_number

    status = input('\nВыберете действие (exit - завершить, enter -продолжить): ')
    print()
    if status == 'exit':
        break
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