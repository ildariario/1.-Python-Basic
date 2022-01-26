# Task 1

# langs = ['Python', 'Java', 'JS', 'SQL']
# new_langs = []
#
# for i_lang in range(2):
#     new_langs.append(langs[i_lang])
# new_langs.append('C++')
# for i_lang in range(2, len(langs)):
#     new_langs.append(langs[i_lang])
#
# print(new_langs)

# Task 2

# langs = ['Python', 'Java', 'JS', 'SQL']
#
# langs.insert(2, 'C++')
#
# print(langs)

# Task 3

# langs = ['Python', 'Java', 'JS', 'SQL']
# user_lang = input('После чего вставить: ')
# i_lang = langs.index(user_lang)
#
# langs.insert(i_lang, 'C++')
#
# print(langs)

# Task 4

# def is_film_exist(movie, films_list):   # movie - кино, фильм
#     for i_movie in films_list:
#         if i_movie == movie:
#             return True
#     return False
#
#
# films = [
#     'Крепкий орешек', 'Назад в будущее', 'Таксист',
#     'Леон', 'Богемская рапсодия', 'Город грехов',
#     'Мементо', 'Отступники', 'Деревня',
#     'Проклятый остров', 'Начало', 'Матрица'
# ]
#
# my_list = []
#
# while True:
#     print('\nВаш текущий топ фильмов:', my_list)
#     new_movie = input('Название фильма: ')
#     if is_film_exist(new_movie, films):
#         print('Команды: добавить, удалить, вставить')
#         command = input('Введите команду: ')
#         if command == 'добавить':
#             my_list.append(new_movie)
#         if command == 'удалить':
#             if is_film_exist(new_movie, my_list):
#                 my_list.remove(new_movie)
#             else:
#                 print('Такого фильма нет в нашем рейтинге!')
#         if command == 'вставить':
#             index = int(input('На какое место?  '))
#             my_list.insert(index - 1, new_movie)
#     else:
#         print('Такого фильма нет на сайте!')

# Home Work
# 1 ==========================================================================
# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# zoo.insert(1, 'bear')
# print(zoo)
# zoo.remove('elephant')
# print(zoo)
# print('Лев сидит в клетке номер ', zoo.index('lion') + 1)
# print('Обезьяна сидит в клетке номер ', zoo.index('monkey') + 1)
# 2 ==========================================================================
# N = int(input('Кол-во сотрудников: '))
# salary_list = []
#
# for i in range(N):
#     print('Зарплата', i + 1, '-го сотрудника: ', end='')
#     employee = int(input())
#     salary_list.append(employee)
#
# # print(salary_list)
# for i_salary in salary_list:
#     if i_salary == 0:
#         salary_list.remove(i_salary)
# print('\nОсталось сотрудников: ', len(salary_list))
# print('Зарплаты: ', salary_list)
# print('Максимальная зп: ', max(salary_list))
# print('Минимальная зп: ', min(salary_list))
# 3 ==========================================================================
def existing_movie(movie, movie_list):
    for i_movie in movie_list:
        if i_movie == movie:
            return True
    return False


films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

my_list = []


print('Список фильмов на сайте:')
print('~' * 180)
print('|| ', films, '  ||')
print('~' * 180)

while True:
    print('Ваш текущий топ фильмов:', my_list)
    film = input('\nВведите название фильма: ')
    print('Доступны следующие действия: (добавить, вставить, удалить, выйти)')
    command = input('Что сделать с фильмом? ')
    if existing_movie(film, films) == True:
        if command == 'добавить':
            if existing_movie(film, my_list) == True:
                print('Фильм ***', film, '*** уже есть в избранном!')
            else:
                my_list.append(film)
                print('Фильм ***', film, '*** успешно добавлен в избранное!')
        elif command == 'вставить':
            index = int(input('На какое место Вы хотите вставить этот фильм? '))
            if existing_movie(film, my_list) == True:
                my_list.remove(film)
                my_list.insert(index - 1, film)
            else:
                my_list.insert(index - 1, film)
            print('Фильм ***', film, '*** успешно передислоцирован!')
        elif command == 'удалить':
            if existing_movie(film, my_list) == True:
                my_list.remove(film)
                print('Фильм ***', film, '*** успешно удален из избранных!')
            else:
                print('Фильма ***', film, '*** в избранных нет! Так что удалять нечего.')
        elif command == 'выйти':
            print('=== Досвидания! Хорошего дня! ===')
            break
        else:
            print('########################### Нет такой команды! ###########################')
    else:
        print('########################### Этого фильма нет на сайте! ###########################')
        flag = input('Хотите выйти? (Да/любая клавиша): ')
        if flag == 'Да':
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