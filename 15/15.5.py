'''Работа за преподавателем'''
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
'''Задача 1. Генерация списка
Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от 1 до N.
'''
# Пропустил
# 2 ==========================================================================
'''Задача 2. Турнир
Для турнира по волейболу необходимо сформировать турнирную сетку из восьми человек на два дня. 
На первый день из списка участников решили выбрать каждого второго.
Дан список из восьми имён: Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар. Напишите 
программу, которая выводит элементы списка только с чётными индексами.
'''
# Пропустил
# 3 ==========================================================================
'''Задача 3. Клетки
В научной лаборатории выводят и тестируют новые виды клеток. Есть список из N этих клеток, 
где элемент списка — это показатель эффективности, а индекс списка — это ранг клетки. Учёные 
отбирают клетки по следующему принципу: если эффективность клетки меньше её ранга, то эта 
клетка не подходит.
Напишите программу, которая выводит на экран те элементы списка, значения которых меньше 
их индекса.

Пример:
Кол-во клеток: 5
Эффективность 1 клетки: 3
Эффективность 2 клетки: 0
Эффективность 3 клетки: 6
Эффективность 4 клетки: 2
Эффективность 5 клетки: 10

Неподходящие значения: 0 2
'''
# Пропустил
# 4 ==========================================================================
'''Задача 4. Видеокарты
В базе одного магазина электроники есть список видеокарт компании NVIDIA разных поколений. 
Для удобства в списке вместо полных названий хранятся только числа, они обозначают модель 
и поколение видеокарты. Недавно компания выпустила новую линейку видеокарт, и в итоге самые 
старшие поколения разобрали за пару дней.
Напишите программу, которая удаляет из этого списка видеокарт наибольшие элементы.

Пример:
Кол-во видеокарт: 5
1 Видеокарта: 3070
2 Видеокарта: 2060
3 Видеокарта: 3090
4 Видеокарта: 3070
5 Видеокарта: 3090


Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
Новый список видеокарт: [ 3070 2060 3070 ]
'''
# Пропустил
# 5 ==========================================================================
'''Задача 5. Кино
Илья зашёл на один любительский киносайт, где пользователи пишут рецензии на фильмы. 
Вот, кстати, список этих фильмов: 
films = [‘Крепкий орешек’, ‘Назад в будущее’, ‘Таксист’, ‘Леон’, ‘Богемская рапсодия’, 
‘Город грехов’, ‘Мементо’, ‘Отступники’, ‘Деревня’]
Илья на сайте в первый раз, он хочет зарегистрироваться и сразу добавить некоторые 
фильмы в список своих любимых, чтобы потом почитать рецензии на них. Напишите программу, 
в которой пользователь вводит фильм, и если он есть в списке, то он добавляется в список 
любимых. Если его нет, то выводится ошибка. В конце выведите весь список любимых фильмов.
'''
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
'''Задача 6. Анализ слова
Мы пишем программу — анализатор слов, чтобы потом, возможно, использовать её для 
тренировки нейросети, которая будет генерировать нужный нам текст.
Пользователь вводит слово. Напишите программу, которая считает количество уникальных 
букв в слове. Уникальные буквы — это те, которые встречаются всего один раз.

Пример 1:
Введите слово: привет
Кол-во уникальных букв: 6

Пример 2:
Введите слово: лава
Кол-во уникальных букв: 2
'''
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
'''Задача 7. Контейнеры
Контейнеры на складе лежат в ряд в порядке невозрастания своей массы (в килограммах). 
На склад привезли ещё один контейнер, который также нужно положить на определённое место.
Напишите программу, которая получает на вход невозрастающую последовательность натуральных 
чисел, означающих массу каждого контейнера в ряду. После этого вводится число X — масса 
нового контейнера. Программа выводит номер, под которым будет лежать новый контейнер. 
Если в ряде есть контейнеры с одинаковой массой, такой же, как у нового, то его нужно 
положить после них.
Обеспечьте контроль ввода: все числа не превышают 200.
Пример:
Кол-во контейнеров: 8
Введите вес контейнера: 165 
Введите вес контейнера: 163 
Введите вес контейнера: 160 
Введите вес контейнера: 160 
Введите вес контейнера: 157 
Введите вес контейнера: 157 
Введите вес контейнера: 155 
Введите вес контейнера: 154 

Введите вес нового контейнера: 162

Номер, куда встанет новый контейнер: 3
'''
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
'''Задача 8. Бегущие цифры
Вы пишете программу для маленького табло, в котором циклически повторяется один и тот же 
текст или числа — прямо как в каком-нибудь метро, автобусах или трамваях.
Дан список из N элементов и целое число K. Напишите программу, которая циклически сдвигает 
элементы списка вправо на K позиций. Используйте минимально возможное количество операций 
присваивания.
Пример 1:
Сдвиг: 1
Изначальный список: [1, 2, 3, 4, 5]
Сдвинутый список: [5, 1, 2, 3, 4]

Пример 2:
Сдвиг: 3
Изначальный список: [1, 4, -3, 0, 10]
Сдвинутый список: [-3, 0, 10, 1, 4]
'''
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
'''Задача 9. Анализ слова 2
Мы продолжаем писать программы — анализаторы для текста, и теперь от нас требуется 
реализовать код, с помощью которого можно будет определять, является ли слово палиндромом 
— словом, которое одинаково читается слева направо и справа налево. 
Напишите такую программу.

Пример 1:
Введите слово: мадам
Слово является палиндромом

Пример 2:
Введите слово: abccba
Слово является палиндромом

Пример 3:
Введите слово: abbd
Слово не является палиндромом
'''
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
'''Задача 10. Сортировка (по желанию)
Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию 
и выводит его на экран. Дополнительный список не использовать.
Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.

Пример:
Изначальный список: [1, 4, -3, 0, 10]
Отсортированный список: [-3, 0, 1, 4, 10]
'''
def selection_sort(my_list):
    for i_mn in range(len(my_list)):
        for curr in range(i_mn, len(my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]


nums = [4, 9, 7, 6, 3, 2]

selection_sort(nums)

print(nums)
