# Home Work
# 1 ==========================================================================
'''
counter = 10     # counter - счетчик, count - считать
while counter >= 0:
    print(counter)
    if counter == 0:
        print('Время вышло!')
    counter -= 1

# 2 ==========================================================================
while True:
    query = int(input('Продолжаем работать? (1-Да/0-Нет): '))     # query - запрос
    if query == 0:
        print('Приложение закрывается...')
        break
    else:
        print('Продолжаем работать...')
print('Работа завершена.')
'''
# 3 ==========================================================================
stop = True
while stop:
    password = input('Введите код: ')
    if password == '0550':
        print('Код верный, завершаю работу...')
        stop = False
    else:
        print('Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!')


# 4 ==========================================================================

# 5 ==========================================================================

# 6 ==========================================================================