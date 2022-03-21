# Task 1

# scores = [54, 67, 48, 99, 27]
# for i_player in range(len(scores)):
#     print(i_player, scores[i_player])

# Task 2

# scores = [54, 67, 48, 99, 27]
# for i_player in enumerate(scores):
#     print(i_player)

# Task 3

# scores = [54, 67, 48, 99, 27]
# for i_player, i_score in enumerate(scores):
#     print(i_player, i_score)

# Home Work
# 1 ==========================================================================
# # string = input('Строка: ')
# string = 'so~mec~od~e'
# indices = ''    # indices - индексы
#
# for i_index, i_sym in enumerate(string):
#     if i_sym == '~':
#         indices += str(i_index)
# print('Ответ:', ' '.join(indices))
# -------------------------------------------------
# string = 'so~mec~od~e'
# indices = []  # indices - индексы
#
# for i_index, i_sym in enumerate(string):
#     if '~' in i_sym:
#         indices.append(str(i_index))
# print('Ответ:', ' '. join(indices))
# 2 ==========================================================================
# from random import choice
#
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#
# first_list = [choice(alphabet) for _ in range(10)]
# second_list = [choice(alphabet) for _ in range(10)]
#
# first_dict = {i_ind: i_letter for i_ind, i_letter in enumerate(first_list)}
# second_dict = {i_ind: i_letter for i_ind, i_letter in enumerate(second_list)}
#
# print('Первый список:', first_list)
# print('Второй список:', second_list)
# print('Первый словарь:', first_dict)
# print('Второй словарь:', second_dict)
# 3 ==========================================================================
def odd_list(seq):
    new_list = []
    if isinstance(seq, tuple) or isinstance(seq, str) or isinstance(seq, list):
        seq = list(seq)
        for i_index, i_elem in enumerate(seq):
            if i_index % 2 == 0:
                new_list.append(i_elem)
        return new_list
    elif isinstance(seq, dict):
        message = 'Словарь не имеет индексов!'
        return message


some_tuple = (1, 3, 5, 7, 9)
some_string = 'О Дивный Новый мир!'
some_list = [100, 200, 300, 'буква', 0, 2, 'а']
some_dict = {1: 'a', 2: 'b', 3: 'c'}

print('Результат:', odd_list(some_tuple))
print('Результат:', odd_list(some_list))
print('Результат:', odd_list(some_string))
print('Результат:', odd_list(some_dict))
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
