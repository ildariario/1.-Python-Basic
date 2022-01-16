# Task 1

# def length(player_list):
#     players_count = 0
#     for _ in player_list:
#         players_count += 1
#     return players_count
#
# scores = [8, 5, 10, 7, 6]
# scores[1] += length(scores)
# scores.append(0)
# scores[2] += length(scores)
# print(scores)

# Task 2

# def length(player_list):
#     players_count = 0
#     for _ in player_list:
#         players_count += 1
#     return players_count
#
# scores = [8, 5, 10, 7, 6]
# scores[1] += length(scores)
# scores.append(0)
# scores[2] += length(scores)
# print(scores)

# Task 3

# scores = [8, 5, 10, 7, 6]
# scores[1] += len(scores)
# scores.append(0)
# scores[2] += len(scores)
# print(scores)

# Home Work
# 1 ==========================================================================

# 2 ==========================================================================

# 3 ==========================================================================

# 4 ==========================================================================

# 5 ==========================================================================
# films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
# favorites = []
# flag = False
#
# while True:
#     user_film = input('Введите фильм: ')
#     for film in films:
#         if user_film == film:
#             favorites.append(film)
#             flag = True
#
#     if flag == True:
#         print('Список любимых фильмов: ')
#         print(favorites)
#     else:
#         print('Ошибка! Такого фильма нет!')
#     flag = False
# 6 ==========================================================================
# word = input('Введите слово: ')
# word_list = list(word)
# num_unique_letters = len(word_list) # Кол-во уникальных букв
#
# print(word_list)
# for i in range(len(word)):
#     count = 0
#     for sym in word_list:
#         if word_list[i] == sym:
#             count += 1
#     if count == 2:
#         num_unique_letters -= 1
#
# print('Кол-во уникальных букв: ', num_unique_letters)
# 7 ==========================================================================
# N = int(input('Кол-во контейнеров: '))
# container_list = []
# index_new_container = 1
#
# for _ in range(N):
#     weight = int(input('Введите вес контейнера: '))
#     while weight > 200:
#         weight = int(input('Вес контейнера превышен! Введите вес контейнера еще раз: '))
#     container_list.append(weight)
#
# new_weight = int(input('\nВведите вес нового контейнера: '))
#
# for weight in container_list:
#     if new_weight <= weight:
#         index_new_container += 1
#
# print(container_list)
# print('\nНомер, куда встанет новый контейнер: ', index_new_container)
# 8 ==========================================================================
# Вариант 1

# K = int(input('Сдвиг: '))
# # initial_list = [1, 2, 3, 4, 5]
# initial_list = [1, 4, -3, 0, 10]
# shifted_list = []
# print('Изначальный список: ', initial_list)
#
# for _ in range(K):
#     shifted_list.append(initial_list[-1])
#     for j in range(len(initial_list) - 1):
#         shifted_list.append(initial_list[j])
#     initial_list = shifted_list
#     shifted_list = []
#
# print('Сдвинутый список: ', initial_list)

# Вариант 2

# K = int(input('Сдвиг: '))
# # initial_list = [1, 2, 3, 4, 5]
# initial_list = [1, 4, -3, 0, 10]
# print('Изначальный список: ', initial_list)
#
# for _ in range(K):
#     last_sym = initial_list[-1]
#     for i in range(-2, -len(initial_list) - 1, -1):
#         initial_list[i + 1] = initial_list[i]
#     initial_list[0] = last_sym
#
# print('Сдвинутый список: ', initial_list)
# 9 ==========================================================================
# word = input('Введите слово: ')
# sym_word = list(word)
# flag = True
#
# if len(sym_word) % 2 == 0:
#     for i in range(int(len(sym_word) / 2)):
#         if sym_word[i] != sym_word[-i - 1]:
#             flag = False
# else:
#     for i in range(int((len(sym_word) - 1) / 2)):
#         if sym_word[i] != sym_word[-i - 1]:
#             flag = False
#
# if flag == True:
#     print('Слово является палиндромом')
# else:
#     print('Слово НЕ является палиндромом')
# 10 ==========================================================================
def selection_sort(my_list):
    for i_mn in range(len(my_list)):
        for curr in range(i_mn, len(my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]


nums = [4, 9, 7, 6, 3, 2]

selection_sort(nums)

print(nums)
# 11 ==========================================================================

# 12 ==========================================================================

# 13 ==========================================================================

# 14 ==========================================================================

# 15 ==========================================================================