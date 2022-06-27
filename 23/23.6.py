# Home Work
# 1 ==========================================================================
"""Задача 1. Имена 2
Есть файл people.txt, в котором построчно хранится N имён пользователей.
Напишите программу, которая берёт количество символов в каждой строке файла и
в качестве ответа выводит общую сумму. Если в какой-либо строке меньше трёх
символов (не считая литерала \n), то вызывается ошибка и сообщение, в какой
именно строке ошибка возникла. Программа при этом не завершается и обрабатывает
все имена файла.
Также при желании можно вывести все ошибки в отдельный файл errors.log.
"""
# sum_sym = 0
# line_count = 0
#
# file = open('people.txt', 'r')
# for i_line in file:
#     line_count += 1
#     length = len(i_line)
#     if i_line.endswith('\n'):
#         length -= 1
#     sum_sym += length
#     try:
#         if length < 3:
#             raise BaseException
#     except BaseException:
#         print(f'В строке {line_count} меньше трёх символов!')
#
# print('Найденная сумма символов:', sum_sym)
# 2 ==========================================================================
'''Задача 2. Координаты
Есть файл coordinates.txt, в котором хранится N пар из чисел X и Y. Оба числа 
передаются в первую функцию, где к каждой координате прибавляется случайное 
число (от 0 до 5 и от 0 до 10) и возвращается результат деления X на Y. Затем 
эти же координаты передаются во вторую функцию, где уже отнимается случайное 
число и возвращается Y поделить на X.
После этого формируется случайное число от 0 до 100, и затем в файл result.txt 
в каждую строку записывается отсортированный список, состоящий из этого 
случайного числа и двух полученных результатов.
Один программист уже написал за нас программу для этой задачи, но «почему-то» 
его вариант решения отклонили. Вот его код:

import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y

def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x

try:
    file = open('coordinates.txt', 'r')
    for line in file:
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            try:
                number = random.randint(0, 100)
                file_2 = open('result_2.txt', 'w', encoding='utf-8')
                my_list = sorted([res1, res2, number])
                file_2.write(' '.join(my_list))
            except Exception:
                print("Что-то пошло не так!")
        except Exception:
            print("Что-то пошло не так со второй функцией.")
        finally:
            file.close()
            file_2.close()
except Exception:
    print("Что-то пошло не так с первой функцией.")

Отредактируйте и исправьте программу, убрав лишние вложенности try except.
'''
# Вариант 1 =======================================================================
# import random
#
#
# def f(x, y):
#     x += random.randint(0, 10)
#     y += random.randint(0, 5)
#     return x / y
#
#
# def f2(x, y):
#     x -= random.randint(0, 10)
#     y -= random.randint(0, 5)
#     return y / x
#
#
# try:
#     file = open('coordinates.txt', 'r')
#     file_2 = open('result_2.txt', 'a', encoding='utf-8')
#     for ind, line in enumerate(file):
#         nums_list = line.split()
#         res1 = f(int(nums_list[0]), int(nums_list[1]))
#         try:
#             res2 = f2(int(nums_list[0]), int(nums_list[1]))
#             try:
#                 number = random.randint(0, 100)
#                 my_list = sorted([res1, res2, number])
#                 string_my_list = ' '.join(map(str, my_list))
#                 file_2.write(f'{ind+1} запись: {string_my_list}\n')
#             except Exception:
#                 print("C функциями все в порядке, но что-то пошло не так при записи в файл!")
#         except Exception:
#             print(f"{ind+1} запись: Что-то пошло не так со второй функцией.")
#             print(f"{ind + 1} запись: Что-то пошло не так со второй функцией.", file=file_2)
#
# except Exception:
#     print(f"{ind+1} запись: Что-то пошло не так с первой функцией.")
#     print(f"{ind + 1} запись: Что-то пошло не так с первой функцией.", file=file_2)
#     file_2.write('\n')
# else:
#     file_2.write('\n')
#     file.close()
#     file_2.close()

# Вариант 2 =======================================================================
# import random
#
#
# def f(x, y):
#     x += random.randint(0, 10)
#     y += random.randint(0, 5)
#     if y == 0:
#         print(f' - ОШИБКА! В первой функции: X/Y={x}/{y}', end=' - ')
#         print(f'ОШИБКА! В первой функции: X/Y={x}/{y} ', end='', file=file_2)
#     return x / y
#
#
# def f2(x, y):
#     x -= random.randint(0, 10)
#     y -= random.randint(0, 5)
#     if x == 0:
#         print(f' - ОШИБКА! Во второй функции: Y/X={y}/{x}', end=' - ')
#         print(f'ОШИБКА! Во второй функции: X/Y={y}/{x} ', end='', file=file_2)
#     return y / x
#
#
# file = open('coordinates.txt', 'r')
# file_2 = open('result_2.txt', 'a', encoding='utf-8')
# print('=====================НОВЫЙ ЗАПУСК=====================', file=file_2)
# for ind, line in enumerate(file):
#     print(f'{ind + 1}-я запись', end='')
#     print(f'{ind + 1}-я запись:', end=' ', file=file_2)
#     nums_list = line.split()
#     try:
#         res1 = f(int(nums_list[0]), int(nums_list[1]))
#         res2 = f2(int(nums_list[0]), int(nums_list[1]))
#     except ZeroDivisionError:
#         file_2.write('- деление на ноль!\n')
#         print(f"деление на ноль!")
#     else:
#         number = random.randint(0, 100)
#         my_list = sorted([res1, res2, number])
#         try:
#             file_2.write(f"({' '.join(list(map(str, my_list)))})" + '\n')
#         except TypeError:
#             print(f" - ОШИБКА! Что-то пошло не так при {ind+1}-й записи!")
#         else:
#             print(' - прошла успешно.')
# file_2.close()
# file.close()
# 3 ==========================================================================
'''Задача 3. Счастливое число
Напишите программу, которая запрашивает у пользователя число до тех пор, пока 
сумма этих чисел не станет больше либо равна 777. Каждое введённое число при 
этом дозаписывается в файл. Сделайте так, чтобы перед дозаписью программа с 
вероятностью 1 к 13 выбрасывала пользователю случайное исключение и завершалась.
'''
# import random
#
# random_errors = [ArithmeticError, AssertionError, AttributeError]  # список случайных ошибок
# sum_num = 0
#
# with open('nums.txt', 'w') as file:
#     while sum_num <= 777:
#         num = int(input('Введите число: '))
#         sum_num += num
#         if random.choices([0, 1], [1 - 1 / 13, 1 / 13])[0]:
#             raise random.choice(random_errors)
#         print(num, file=file)  # Перенаправим вывод n в файл с помощью параметра file функции print
# 4 ==========================================================================
'''Задача 4. Регистрация
У вас есть файл с протоколом регистраций пользователей на сайте — registrations.txt
Каждая строка содержит: ИМЯ ИМЕЙЛ ВОЗРАСТ, разделённые пробелами.
Например:
Василий test@test.ru 27

Напишите программу, которая проверяет данные из файла для каждой строки:
•	Присутствуют все три поля.
•	Поле имени содержит только буквы.
•	Поле «Имейл» содержит @ и . (точку).
•	Поле «Возраст» является числом от 10 до 99.
В результате проверки сформируйте два файла:
•	registrations_good.log — для правильных данных, записывать строки как есть,
•	registrations_bad.log — для ошибочных, записывать строку и вид ошибки.
Для валидации строки данных напишите функцию, которая может выдавать исключения:
•	НЕ присутствуют все три поля: ValueError.
•	Поле имени содержит НЕ только буквы: NameError.
•	Поле «Имейл» НЕ содержит @ или (точку): SyntaxError.
•	Поле «Возраст» НЕ является числом от 10 до 99: RuntimeError.
'''


# def err_fun(data_list, num_string):
#     message = ''
#     try:
#         if len(data_list) < 3:          # Присутствуют все три поля
#             message = 'ОШИБКА: НЕ присутствуют все три поля!'
#             raise ValueError(message)
#         elif not data_list[0].isalpha():  # Поле имени содержит только буквы
#             message = 'ОШИБКА: Поле имени содержит НЕ только буквы!'
#             raise NameError(message)
#         elif '@' not in data_list[1] or '.' not in data_list[1]:  # Поле «Имейл» содержит @ и . (точку)
#             message = 'ОШИБКА: Поле «Имейл» НЕ содержит @ или (точку)!'
#             raise SyntaxError(message)
#         elif not (10 <= int(data_list[2]) <= 99):                 # Поле «Возраст» является числом от 10 до 99
#             message = 'ОШИБКА: Поле «Возраст» НЕ является числом от 10 до 99!'
#             raise RuntimeError(message)
#     except (ValueError, NameError, SyntaxError, RuntimeError):
#         print(f'В {num_string}-ом поле допущена', message)
#         return False, message
#     else:
#         print(f'{num_string}-е поле заполнено без ошибок :)')
#         return True, message
#
#
# def log_fun(file_name, string='', mode='a'):
#     with open(file_name, mode, encoding='utf-8') as file_out:
#         print(string, end='', file=file_out)
#
#
# log_fun('registrations_good.log', mode='w')  # Очистка содержимого файла
# log_fun('registrations_bad.log', mode='w')   # Очистка содержимого файла
#
# with open('registrations.txt', 'r', encoding='utf-8') as file_inp:
#     for i_ind, i_string in enumerate(file_inp):
#         str_list = i_string.split()
#
#         flag, err_message = err_fun(str_list, i_ind+1)
#
#         if flag:
#             log_fun('registrations_good.log', i_string)
#         else:
#             log_fun('registrations_bad.log', ' '.join([' '.join(str_list), f'({err_message})', '\n']))
# 5 ==========================================================================
'''Задача 5. Текстовый калькулятор
Иван стоит на пороге величайшего открытия (не будем его расстраивать), которое 
перевернёт представление о всей математике и программировании. Имя этому открытию
— текстовый калькулятор. Правда, код для своего открытия ему сложно написать самому,
 и поэтому он попросил вас помочь ему. Так что уже можно бежать в патентное бюро.
Есть файл calc.txt, в котором хранятся записи вида:
100 + 34
23 / 4
то есть ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2, разделённые пробелами.
Операнды — целые числа. Операции — арифметические (включая деление нацело и 
нахождение остатка).
Напишите программу, которая вычисляет все эти операции и находит сумму их 
результатов. Пропишите обработку возможных ошибок. Программа не должна завершаться 
при первой же ошибке, она учитывает все верные строки и выводит найденный ответ.
'''


# def calc(operand_1, operation, operand_2):
#     if operation == '*':
#         return operand_1 * operand_2
#     elif operation == '/':
#         return operand_1 / operand_2
#     elif operation == '%':
#         return operand_1 % operand_2
#     elif operation == '//':
#         return operand_1 // operand_2
#     elif operation == '+':
#         return operand_1 + operand_2
#     elif operation == '-':
#         return operand_1 - operand_2
#     else:
#         raise TypeError
#
#
# sum_result = 0
# sum_list = []
# with open('calc.txt', 'r') as file:
#     for num_str, i_string in enumerate(file):
#         num_1, action, num_2 = i_string.split()
#         try:
#             num = calc(int(num_1), action, int(num_2))
#         except ZeroDivisionError:
#             print(f'{num_str+1}) Деление на ноль в {num_str+1}-й строчке файла.')
#         except TypeError:
#             print(f'{num_str+1}) Некорректный оператор в {num_str+1}-й строчке файла.')
#         except ValueError:
#             print(f'{num_str+1}) Один из операндов не является целым числом в {num_str+1}-й строчке файла.')
#         except Exception:
#             print(f'{num_str+1}) Неизвестная ошибка при вычислении результата в {num_str+1}-й строчке файла.')
#         else:
#             sum_list.append(str(num))
#             print(f'{num_str+1})', num_1, action, num_2, f'= {num}')
#             sum_result += num
# print(f"Сумма всех результатов: {' + '.join(sum_list)} =", sum_result)
# 6 ==========================================================================
'''Задача 6. Чат
Реализуйте программу — чат, в котором могут участвовать сразу несколько человек, 
то есть программа может работать одновременно для нескольких пользователей. 
При запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
1.	Посмотреть текущий текст чата.
2.	Отправить сообщение (затем вводит сообщение).
Действия запрашиваются бесконечно. 

Примечание: для решения задачи вам будет достаточно текущих знаний, нужно лишь 
проявить немного фантазии и хитрости. Не нужно лезть в дебри работы с сетями, 
создания GUI-приложений и прочих штук. (Но если очень хочется, то останавливать 
вас никто не будет!)
'''
# Вариант 1 (Мой вариант)
def action_in_chat(act):
    if act == '1':
        with open('chat.txt', 'r', encoding='utf-8') as chat_file:
            print(chat_file.read())
    elif act == '2':
        with open('chat.txt', 'a', encoding='utf-8') as chat_file:
            message = input('Введите сообщение: ')
            chat_file.write(f'{name}: {message}\n')
    elif act == '3':
        return True
    else:
        print('Неверное действие!')
        act_next = input('Выберете действие (1. Посмотреть текущий текст чата, 2. Отправить сообщение, '
                         '3. Закрыть программу): ')
        action_in_chat(act_next)


Exit = False
with open('chat.txt', 'a', encoding='utf-8') as chat_file:
    chat_file.write('=========Новый сеанс=========\n')
while not Exit:
    name = input('Ваше имя: ')
    action = input('Выберете действие (1. Посмотреть текущий текст чата, 2. Отправить сообщение, '
                   '3. Закрыть программу): ')
    Exit = action_in_chat(action)
    print()
# 7 ==========================================================================
'''Задача 7. Текстовый калькулятор 2 (выполните по желанию)
Модифицируйте задачу про калькулятор: условие задачи остается тем же, но теперь 
пользователю должно выводиться сообщение с ошибочной строкой на экран с 
предложением её исправить. 

Пример 1:
Содержимое файла calc.txt
100 + 34
10 +* 3
23 / 4

Содержимое консоли:
Обнаружена ошибка в строке: 10 +* 3 Хотите исправить? да
Введите исправленную строку: 10 + 3

Сумма результатов: 152.75

Пример 2:
Содержимое файла calc.txt
100 + 34
10 +* 3
20 -* 2
23 / 4

Содержимое консоли:
Обнаружена ошибка в строке: 10 +* 3 Хотите исправить? нет
Обнаружена ошибка в строке: 20 -* 2 Хотите исправить? да
Введите исправленную строку: 20 - 2

Сумма результатов: 157.75
'''


# def calc(operand_1, operation, operand_2):
#     if operation == '*':
#         return operand_1 * operand_2
#     elif operation == '/':
#         return operand_1 / operand_2
#     elif operation == '%':
#         return operand_1 % operand_2
#     elif operation == '//':
#         return operand_1 // operand_2
#     elif operation == '+':
#         return operand_1 + operand_2
#     elif operation == '-':
#         return operand_1 - operand_2
#     else:
#         raise TypeError
#
#
# def correct_fun(choice, num_line):
#     if choice == '1' or choice == '0':
#         if int(choice):
#             corrected_line = input('Введите исправленную строку: ')
#             num1, act, num2 = corrected_line.split()
#             res_num = calc(int(num1), act, int(num2))
#             sum_list.append(str(res_num))
#             print(f'{num_line+1})', num1, act, num2, f'= {res_num}')
#             return res_num
#     else:
#         correct_fun(input('Вводить можно только Да-1 или Нет-0: '), num_line)
#     return 0
#
#
# sum_result = 0
# sum_list = []
# with open('calc.txt', 'r') as file:
#     for num_str, i_string in enumerate(file):
#         num_1, action, num_2 = i_string.split()
#         try:
#             num = calc(int(num_1), action, int(num_2))
#         except Exception:
#             print(f'{num_str+1}) Обнаружена ошибка в {num_str+1}-й строке: ({i_string[:-1]}).', end=' | ')
#             sum_result += correct_fun(input('Хотите исправить ошибку? (Да-1, Нет-0): '), num_str)
#         else:
#             sum_list.append(str(num))
#             print(f'{num_str+1})', num_1, action, num_2, f'= {num}')
#             sum_result += num
# print(f"Сумма всех результатов: {' + '.join(sum_list)} =", sum_result)
