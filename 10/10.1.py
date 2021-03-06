'''Работа за преподавателем'''
# Task 1

# for a in range(1, 10):
#     for b in range(1, 10):
#         print(a, '*', b, '=', a * b)
#     print()

# Task 2

# for row in range(6):    # row - строка
#     for col in range(6):    # column - столбец
#         print(row + col, end = ' ')
#     print()

# Task 3

# for row in range(0, 6, 2):    # row - строка
#     for col in range(0, 6, 3):    # column - столбец
#         print(row + col, end = ' ')
#     print()

# Home Work
# 1 ==========================================================================
'''Задача 1. Таблица умножения
Математик Паша недавно заметил, что у него уже есть куча разных таблиц степеней, но нет 
самого основного - таблицы умножения. Пора бы это исправить.
Напишите программу, которая выводит таблицу умножения для чисел от 1 до 9. Для этого 
используйте конструкцию вложенного цикла: внешний отвечает за первый множитель, а внутренний 
- за второй.
Дополнение: выведите настоящую таблицу умножения, без всяких знаков, только числа. 
Чтобы она получилась красивой и ровной, используйте литерал ‘\t’ внутри оператора end. 
\t - это литерал табуляции, благодаря ему все числа выстраиваются в виде таблицы. 
Результат должен получиться таким:
1	2	3	4	5	6	7	8	9	
2	4	6	8	10	12	14	16	18	
3	6	9	12	15	18	21	24	27	
4	8	12	16	20	24	28	32	36	
5	10	15	20	25	30	35	40	45	
6	12	18	24	30	36	42	48	54	
7	14	21	28	35	42	49	56	63	
8	16	24	32	40	48	56	64	72	
9	18	27	36	45	54	63	72	81
'''
# Вар 1
# for row in range(1, 10):
#     for col in range(1, 10):
#         print(row, '*', col, '=', row * col)
#     print()

# Вар 2
# for row in range(1, 10):
#     for col in range(1, 10):
#         print(row, '*', col, '=', row * col, end = '\t')
#     print()

# Вар 3
# for row in range(1, 10):
#     for col in range(1, 10):
#         print(row * col, end = '\t')
#     print()
# 2 ==========================================================================
'''Задача 2. Таблица суммы
Напишите программу, которая запрашивает у пользователя число N и выводит таблицу суммы для чисел от 1 до N.
Пример:
0 1 2 3 4 5 
1 2 3 4 5 6 
2 3 4 5 6 7 
3 4 5 6 7 8 
4 5 6 7 8 9 
5 6 7 8 9 10
'''
# N = int(input('Введите число N: '))
# for row in range(N+1):
#     for col in range(N+1):
#         print(row + col, end = ' ')
#     print()
# 3 ==========================================================================
'''Задача 3. Анализ данных
Отдел анализа данных сегодня получил вот такую интересную штуку:
0	-1	-2	-3	-4	-5	-6	-7	-8	-9	
1	0	-1	-2	-3	-4	-5	-6	-7	-8	
2	1	0	-1	-2	-3	-4	-5	-6	-7	
3	2	1	0	-1	-2	-3	-4	-5	-6	
4	3	2	1	0	-1	-2	-3	-4	-5	
5	4	3	2	1	0	-1	-2	-3	-4	
6	5	4	3	2	1	0	-1	-2	-3	
7	6	5	4	3	2	1	0	-1	-2	
8	7	6	5	4	3	2	1	0	-1	
9	8	7	6	5	4	3	2	1	0
Нам, как работнику этого отдела, дали задание понять, как и почему такое произошло. 
Напишите программу, которая выводит на экран такую таблицу. 
Замечание: не забудьте про литерал табуляции \t
'''
# for row in range(10):
#     for col in range(0, -10, -1):
#         print(row + col, end = '\t')
#     print()
# 4 ==========================================================================
'''Задача 4. Урезанная таблица умножения(необязательная)
Математик (и теперь уже программист) Паша подумал и понял, что в таблице умножения есть 
много повторяющихся чисел. “Зачем мне тогда хранить лишнюю информацию в памяти?”, - спросил 
он себя и убрал верхнюю половину таблицы.
Напишите программу, которая выводит только нижнюю половину таблицы умножения, вот так
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
9 18 27 36 45 54 63 72 81
'''
# i = 0
# for row in range(0, 10):
#     i += 1
#     for col in range(1, i):
#         print(row * col, end = ' ')
#     print()
