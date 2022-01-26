# Task 1



# Task 2



# Task 3



# Home Work
# 1 ==========================================================================

# 2 ==========================================================================

# 3 ==========================================================================

# 4 ==========================================================================

# 5 ==========================================================================
# violator_songs = [
#     ['World in My Eyes', 4.86],
#     ['Sweetest Perfection', 4.43],
#     ['Personal Jesus', 4.56],
#     ['Halo', 4.9],
#     ['Waiting for the Night', 6.07],
#     ['Enjoy the Silence', 4.20],
#     ['Policy of Truth', 4.76],
#     ['Blue Dress', 4.29],
#     ['Clean', 5.83]
# ]
# total_time = 0
#
# num_select = int(input('Сколько песен выбрать? '))
#
# for i_sel in range(num_select):
#     print('Название', i_sel + 1, 'песни: ', end='')
#     song_name = input()
#     for i_song in range(len(violator_songs)):
#         if song_name == violator_songs[i_song][0]:
#             total_time += violator_songs[i_song][1]
#
# print('Общее время звучания песен: ', round(total_time, 2))
# 6 ==========================================================================
# first_list = []
# second_list = []
#
# for i_first in range(3):
#     num = int(input(f'Введите {i_first + 1}-е число для 1-го списка: '))
#     first_list.append(num)
# print()
# for i_sec in range(7):
#     num = int(input(f'Введите {i_sec + 1}-е число для 2-го списка: '))
#     second_list.append(num)
#
# print('Первый список: ', first_list, '\nВторой список:', second_list)
#
# first_list.extend(second_list)
#
# i_num = 0
#
# while i_num < len(first_list) - 1:
#     while first_list.count(first_list[i_num]) > 1:
#         first_list.remove(first_list[i_num])
#     i_num += 1
#
# print('Новый первый список с уникальными элементами: ', first_list)
# 7 ==========================================================================
# skate_sizes_list = []
# leg_sizes_list = []
# count = 0

# N = int(input('Кол-во коньков: '))
# for i_pair in range(N):
#     print('Размер', i_pair + 1, 'пары: ', end='')
#     pair = int(input())
#     skate_sizes_list.append(pair)

# K = int(input('\nКол-во людей: '))
# for i_leg in range(K):
#     print('Размер ноги', i_leg + 1, 'человека: ', end='')
#     leg = int(input())
#     leg_sizes_list.append(leg)

# print(skate_sizes_list)
# print(leg_sizes_list)
#
# for leg_size in leg_sizes_list:
#     for pair_size in skate_sizes_list:
#         if leg_size == pair_size:
#             skate_sizes_list.remove(pair_size)
#             count += 1
#             break
#         elif pair_size > leg_size:
#             skate_sizes_list.remove(pair_size)
#             count += 1
#             break
#
# print(skate_sizes_list)
# print(leg_sizes_list)

# print('Наибольшее кол-во людей, которые могут взять ролики: ', count)
# 8 ==========================================================================
# Вариант № 1 (Мой)

# N = int(input('Кол-во человек: '))
# K = int(input('Какое число в считалке? '))
# print(f'Значит, выбывает каждый {K} человек')
#
# people_list = list(range(1, N + 1))
#
# index = 0
# count = 1
# while len(people_list) > 1:
#     print('\nТекущий круг людей: ', people_list)
#     print('Начало счёта с номера', people_list[index])
#     while count < 7:
#         if index == len(people_list) - 1:
#             index = 0
#             count += 1
#         else:
#             index += 1
#             count += 1
#     else:
#         if index == len(people_list) - 1:
#             print('Выбывает человек под номером', people_list[index])
#             people_list.remove(people_list[index])
#             count = 1
#             index = 0
#         else:
#             print('Выбывает человек под номером', people_list[index])
#             people_list.remove(people_list[index])
#             count = 1
# print('\nОстался человек под номером ', people_list[0])

# Вариант № 2 (Нашел в инете, но не понял решения)

# N = int(input('Кол-во человек: '))
# K = int(input('Какое число в считалке?: '))
# print('Значит, выбывает каждый', K, 'человек')
#
# people_list = list(range(1, N + 1))
#
# count = 0
# while len(people_list) > 1:
#     print('Текущий круг людей: ', people_list)
#     print('Начало счёта с номера:', people_list[count])
#     count = (count + K - 1) % len(people_list)
#     if people_list[count] == people_list[-1]:
#         print('Выбывает человек под номером:', people_list.pop(count))
#         count = 0
#     else:
#         print('Выбывает человек под номером:', people_list.pop(count))
#
# print('Остался человек под номером:', people_list[0])
# 9 ==========================================================================
# debt = []
#
# N = int(input('Кол-во друзей: '))
# K = int(input('Долговых расписок: '))
#
# for _ in range(N):
#     debt.append(0)
#
# for i_voucher in range(K):
#     print()
#     print(i_voucher + 1, 'расписка')
#     whom = int(input('Кому: '))             # Кому
#     from_whom = int(input('От кого: '))     # От кого
#     how_much = int(input('Сколько: '))      # Сколько
#     debt[whom - 1] += how_much
#     debt[from_whom - 1] -= how_much
#
# print('Баланс друзей:')
# for i_friends in range(len(debt)):
#     print(i_friends + 1, ':', -debt[i_friends])
# 10 ==========================================================================
def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i_num])
    if num_list == reverse_list:
        return True
    else:
        return False


nums = [3, 4, 3]
new_nums = []
answer = []

for i_nums in range(0, len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    if is_palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []

print('Исходный список: ', nums)
print('Нужно приписать чисел: ', len(answer))
print('Сами числа: ', answer)
# 11 ==========================================================================

# 12 ==========================================================================

# 13 ==========================================================================

# 14 ==========================================================================

# 15 ==========================================================================