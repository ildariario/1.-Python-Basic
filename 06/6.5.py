# Home Work
# 1 ==========================================================================
'''
counter = 1
quality = int(input('Сколько раз вывести фразу "Я - программист!"? '))
while counter <= quality:
    print('Я - программист!')
    counter += 1

# 2 ==========================================================================
counter = 1
task = input('Введите задание о котором нужно напомнить: ')
quality = int(input('Сколько раз напомнить о нем? '))
while counter <= quality:
    print(f'Напоминаю Вам: {task}')
    counter += 1

# 3 ==========================================================================
counter = 1
total_weight = 0
num = int(input('Сколько мешков перенести? '))
while counter <= num:
    weight = int(input(f'Какова масса (в кг) {counter}-го мешка? '))
    total_weight += weight
    print(f'Перенесено {counter} из {num} мешков.')
    counter += 1
print(f'Масса всех мешков = {total_weight} кг.')
'''
# 4 ==========================================================================
counter = 0
degree = int(input('Введите степень до которой нужно возводить число 2: '))
while counter <= degree:
    print(2**counter)
    counter += 1


