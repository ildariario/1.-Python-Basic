'''Работа за преподавателем'''
# Task 1
# Вариант 1
# attemptCount = 3
# for attempt in range(1, 4):                     # attempt - попытка
#     pincode = int(input('Введите пин-код: '))
#     if pincode == 1234:
#         print('Пин-код верный. Держите вашу зарпалату!')
#         break
#     attemptCount -= 1
#     print('Неверный пин-код. Осталось попыток: ', 3 - attempt)
# if attemptCount == 0:
#     print('Ваша карта заблокирована. Досвидос!')

# Вариант 2
# for attempt in range(1, 4):                     # attempt - попытка
#     pincode = int(input('Введите пин-код: '))
#     if pincode == 1234:
#         print('Пин-код верный. Держите вашу зарпалату!')
#         break
#     print('Неверный пин-код. Осталось попыток: ', 3 - attempt)
# else:
#     print('Ваша карта заблокирована. Досвидос!')

# Вариант 3
# while True:
#     for attempt in range(1, 4):                     # attempt - попытка
#         pincode = int(input('Введите пин-код: '))
#         if pincode == 1234:
#             print('\nПин-код верный. Держите вашу зарпалату!')
#             break
#         print('Неверный пин-код. Осталось попыток: ', 3 - attempt)
#     else:
#         print('\nВаша карта заблокирована. Досвидос!')
#     print('Следующий клиент, добро пожаловать!')

# Вариант 4
while True:
    attempt = 1
    while attempt < 4:                     # attempt - попытка
        pincode = int(input('Введите пин-код: '))
        if pincode == 1234:
            print('\nПин-код верный. Держите вашу зарпалату!')
            break
        print('Неверный пин-код. Осталось попыток: ', 3 - attempt)
        attempt += 1
    else:
        print('\nВаша карта заблокирована. Досвидос!')
    print('Следующий клиент, добро пожаловать!')
