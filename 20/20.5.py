# Task 1

# phonebook_dict = {
#     ('Петров', 'Ваня'): 88006663636,
#     ('Егоров', 'Ваня'): 88003333333,
#     ('Ульянов', 'Петя'): 88005553535,
#     ('Сидорова', 'Лена'): 88007773737
# }
#
# phonebook_dict[('Сидорова', 'Алена')] = 109090
# print(phonebook_dict)
# for i_person in phonebook_dict:
#     if 'Сидорова' in i_person:
#         print(i_person[1], phonebook_dict[i_person])

# Task 2


# Task 3


# Home Work
# 1 ==========================================================================
# def get_name(series_number):
#     series_number = tuple(series_number)
#     if series_number in data:
#         print(f'Имя и фамилия человека: {data[series_number][1]} {data[series_number][0]}')
#     else:
#         print('Такого человека нет в базе!')
#
#
# data = {
#     (5000, 123456): ('Иванов', 'Василий'),
#     (6000, 111111): ('Иванов', 'Петр'),
#     (7000, 222222): ('Медведев', 'Алексей'),
#     (8000, 333333): ('Алексеев', 'Георгий'),
#     (9000, 444444): ('Георгиева', 'Мария')
# }
#
# ser_num = input('Введите серию и номер паспорта ч/з пробел: ').split()
# get_name([int(ser_num[0]), int(ser_num[1])])
# 2 ==========================================================================
contacts_dict = dict()

while True:
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    number = int(input('Введите номер телефона: '))
    if (name, surname) not in contacts_dict:
        contacts_dict[(name, surname)] = number
    else:
        print('\nТакой контакт уже есть в телефонной книге!')

    request = input('Желаете продолжить? Да/Нет: ')
    if request == 'Нет':
        break

print('\nТелефонная книга:')
for name_surname, number in contacts_dict.items():
    print('\t', name_surname[0], name_surname[1], ':', number)
# 3 ==========================================================================

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
