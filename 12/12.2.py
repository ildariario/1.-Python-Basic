# Task 1

# for food in range(3):
#     print(food + 1,'- я клетка:')
#     fruits = int(input('Сколько фруктов? '))
#     vegrtables = int(input('Сколько обощей? '))
#     summ = fruits + vegrtables
#     print('В', food + 1,'- ю клетку нужно корма: ', summ)

# Task 2

# print('Обезьяны')
# fruits = int(input('Сколько фруктов? '))
# vegrtables = int(input('Сколько обощей? '))
# print('Всего: ', fruits + vegrtables)

# print('\nЖирафы')
# fruits = int(input('Сколько фруктов? '))
# vegrtables = int(input('Сколько обощей? '))
# print('Всего: ', fruits + vegrtables)

# print('\nСлоны')
# fruits = int(input('Сколько фруктов? '))
# vegrtables = int(input('Сколько обощей? '))
# print('Всего: ', fruits + vegrtables)

# Task 3

# def countFood():
#     fruits = int(input('Сколько фруктов? '))
#     vegrtables = int(input('Сколько обощей? '))
#     print('Всего: ', fruits + vegrtables)

# print('Обезьяны')
# countFood()
# print('\nЖирафы')
# countFood()
# print('\nСлоны')
# countFood()

# Task 4

# def triangle():   # triangle - треугольник
#     stars = 1
#     for line in range(5):
#         print(' ' * (5 - line - 1), end = '')
#         print('*' * stars)
#         stars += 2
    
# def rectangle():   # rectangle - прямоугольник
#     for line in range(5):
#         if line == 0 or line == 4:
#             print('*' * 5)
#         else:
#             print('*' + ' ' * 3 + '*')

# choice = int(input('Что рисуем? 1 - треугольник, 2 - прямоугольник: '))   # choiсe - выбор
# if choice == 1:
#     triangle()
# elif choice == 2:
#     rectangle()
# else:
#     print('Ошибка ввода.')

# Home Work
# 1 ==========================================================================
# def greeting():     # greeting - приветствие
#     print('Привет!')
#     print('Добро пожаловать!')

# while True:
#     a = input('Зайдёте? Да/Нет: ')
#     if a == 'Да':
#         greeting()
#     print('Следующий.\n')
# 2 ==========================================================================
# def count_food():
#     a = int(input())
#     b = int(input())
#     print("Всего", a+b, "шт.")

# print("Сколько мешков рыбы и мяса?")
# count_food()

# print("Сколько буханок белого и чёрного хлеба?")
# count_food()

# print("Сколько вёдер воды и молока?")
# count_food()
# 3 ==========================================================================
# def family_members():
#     print('Фамилия: Иванов')
#     print('Имя: Василий')
#     print('Улица: Пушкина')
#     print('Дом: 32')

# family_members()
# family_members()
# family_members()
# 4 ==========================================================================
def triangle():
    stars = 1
    for line in range(5):
        print(' ' * (5 - line - 1), end = '')
        print('*' * stars)
        stars += 2
def rectangle():
    for line in range(5):
        if line == 0 or line == 4:
            print('*' * 5)
        else:
            print('*' + ' ' * 3 + '*')

figure = int(input('Что нужно вывести на экран? 1 - треугольник, 2 - прямоугольник: '))
if figure == 1:
    triangle()
elif figure == 2:
    rectangle()
else:
    print('Ошибка ввода.')
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