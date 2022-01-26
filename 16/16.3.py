# Task 1

# my_list = ['Игра', 'Изгой', 'Таксист']
# your_list = ['Начало', 'Отступники', 'Король Лев']
#
# my_list.append(your_list)
#
# print(my_list)

# Task 2

# my_list = ['Игра', 'Изгой', 'Таксист']
# your_list = ['Начало', 'Отступники', 'Король Лев']
#
# for i_elem in your_list:
#     my_list.append(i_elem)
#
# print(my_list)

# Task 3

# my_list = ['Игра', 'Изгой', 'Таксист']
# your_list = ['Начало', 'Отступники', 'Король Лев']
#
# my_list.extend(your_list)
#
# print(my_list)

# Task 4

# my_list = ['Игра', 'Изгой', 'Таксист']
# your_list = ['Начало', 'Отступники', 'Король Лев']
#
# my_list.extend(your_list)
#
# my_list.extend('Али')
#
# print(my_list)

# Task 5

# my_list = ['Игра', 'Изгой', 'Таксист']
# your_list = ['Начало', 'Отступники', 'Король Лев']
#
# my_list = my_list + your_list
#
# print(my_list)

# Task 6

# pack = []
# decode = []
# bad_packs = 0
#
# packs_amt = int(input('Кол-во пакетов: '))
#
# for i_pack_num in range(packs_amt):
#     print('\nПакет номер', i_pack_num + 1)
#     for i_bit in range(4):
#         print(i_bit + 1, 'бит:', end=' ')
#         num = int(input())
#         pack.append(num)
#     if pack.count(-1) <= 1:
#         decode.extend(pack)
#     else:
#         print('Много ошибок в пакете.')
#         bad_packs += 1
#     pack = []
#
# print('\nПолученное сообщение: ', decode)
# print('Кол-во ошибок в сообщении: ', decode.count(-1))
# print('Кол-во потераянных пакетов', bad_packs)

# Home Work
# 1 ==========================================================================
# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
# first_company = [0, 0, 0]
# second_company = [1, 0, 0, 1, 1]
# third_company = [1, 1, 1, 0, 1]
#
# main.extend(first_company)
# main.extend(second_company)
# main.extend(third_company)
#
# print('Общий список задач: ', main)
# print('Общее кол-во задач: ', main.count(0) + main.count(1))
# print('Кол-во невыполненных задач: ', main.count(0))
# 2 ==========================================================================
# message_1 = input('Первое сообщение: ')
# message_2 = input('Второе сообщение: ')
#
# if list(message_1).count('!') + list(message_1).count('?') > list(message_2).count('!') + list(message_2).count('?'):
#     print('Третье сообщение: ', message_1, message_2)
# elif list(message_1).count('!') + list(message_1).count('?') < list(message_2).count('!') + list(message_2).count('?'):
#     print('Третье сообщение: ', message_2, message_1)
# else:
#     print('Ой.')
# 3 ==========================================================================
pack = []
decode = []
bad_pack = 0

N = int(input('Кол-во пакетов: '))

for i_pack in range(N):
    print('\nПакет номер:', i_pack + 1)
    for i_bit in range(4):
        print(i_bit + 1, 'бит:', end=' ')
        bit = int(input())
        pack.append(bit)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('Много ошибок в пакете.')
        bad_pack += 1
    pack = []

print('Полученное сообщение: ', decode)
print('Кол-во ошибок в сообщении: ', decode.count(-1))
print('Кол-во потерянных пакетов: ', bad_pack)
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