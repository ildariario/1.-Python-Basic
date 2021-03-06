'''Работа за преподавателем'''
# Task 1

# n = int(input('Введите число: '))
# for num in range(n + 1):
#     if num % 2 == 0:
#         print(num,'** 3 = ',num ** 3)

# Task 2

# n = int(input('Введите число: '))
# for num in range(1, n//2 + 1):
#     num = num * 2             # Четное число
#     print(num,'** 3 = ',num ** 3)

# Task 3

# total_hours = int(input('Введите кол-во часов: '))
# sells = 1
# for hour in range(1, total_hours // 3 + 1):
#     sells *= 2
#     print('Прошло часов: ', hour*3)
#     print('Кол-во клеток: ', sells)
#     print('Осталось часов: ', total_hours - hour*3)
#     print()
# print('Наблюдение завершено!')

# Home Work
# 1 ==========================================================================
'''Задача 1. Таблица кубов
Паше для проекта по математике нужна таблица кубов (третья степень числа) только 
чётных чисел от 1 до N. Напишите программу, которая выведет ему эту таблицу на экран. 
Не используйте условные операторы, выведите формулу, как мы сделали это в уроке.
'''
# n = int(input('Введите число: '))
# for num in range(1, n // 2 + 1):
#     num *= 2
#     print(num,'^ 3 = ', num**3)
# 2 ==========================================================================
'''Задача 2. Деление клетки
Реализуйте программу, разобранную в уроке.
В одной лаборатории наблюдают за одноклеточной амёбой. Мы знаем, что каждые три часа 
она делится на 2 клетки. Нам нужно для этой лаборатории написать программу, которая 
будет выводить сколько прошло часов и сколько получилось клеток. Также нас попросили 
писать на каждом этапе деления сколько осталось часов до завершения наблюдения, чтобы 
ученым было проще формулировать выводы на определённом этапе наблюдения.
Пример сообщений:
Прошло часов: 3.
Клеток: 2.
Часов до конца эксперимента: 12
Прошло часов: 6...
'''
# hours = int(input('Введите общее кол-во часов наблюдения: '))
# sells = 1
# for hour in range(1, hours // 3 + 1):
#     hour *= 3
#     sells *= 2
#     print('Прошло', hour, 'часов.')
#     print('Кол-во клеток:', sells)
#     print('До завершения наблюдения', hours - hour, 'часов.')
#     print()
# print('Наблюдение завершено!')
# 3 ==========================================================================
'''Задача 3. Марсоход
Робот Валли помогает человечеству и исследует поверхность Марса. С Земли ему говорят, 
сколько примерно метров ему нужно будет проехать. Валли останавливается каждые 4 метра 
и сообщает землянам сколько метров он прошёл, сколько ещё ехать и какой у него остался 
коэффициент прочности (изначально он равен 100, каждые 4 метра уменьшается на 5/2). 
Реализуйте программу для Валли, чтобы он мог держать землян в курсе событи
'''
# distance = int(input('Cколько метров нужно проехать? '))
# strength_factor  = 100
# for hour in range(1, distance // 4 + 1):
#     hour *= 4
#     strength_factor -= 5/2
#     print('Валли-Рус прошел', hour,'метров.')
#     print('Ехать еще', distance - hour,'метров.')
#     print('Коэффициент прочности', strength_factor)
#     print()
# 4 ==========================================================================
'''Задача 4. Квадраты нечётных чисел
Вводится число N. Напишите программу, которая выводит квадраты нечетных чисел от 1 до N. 
Нельзя использовать условные операторы. Можно использовать цикл while, но постарайтесь 
всё-таки решить с помощью конструкции for in range. Не нужно искать решение в интернете, 
попробуйте подумать сами, в следующем уроке мы обязательно разберём эту задачу.
'''
n = int(input('Введите число: '))
for num in range(1, n // 2 + 1):
    num = num * 2 - 1        # Нечетное число
    print(num, '^ 2 =', num ** 2)
