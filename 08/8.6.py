# Home Work
# 1 ==========================================================================
# count = 0
# for buckwheat in range(100, -1, -4):           # buckwheat - гречка
#     count += 1
#     print('Прошел', count, 'месяц. Гречки осталось', buckwheat, 'кг.')
# 2 ==========================================================================
# n = int(input('Введите число: '))
# summ = 0
# for num in range(1, n+1, 2):
#     print(num)
#     summ += num
# print(summ)
# 3 ==========================================================================
# n = int(input('Введите число должников: '))
# summ = 0
# for debtor in range(0, n, 5):       # debtor - должник
#     print('Должник с номером:', debtor)
#     debt = int(input('Сколько должны? '))        # debt - долг
#     summ += debt
# print('Общая сумма долга: ', summ)
# 4 ==========================================================================
# N = int(input('Через сколько секунд взорвётся бомба? '))
# for sec in range(1, N + 1):
#     question = int(input('Хотите обезвредить бомбу? (0/1 - Нет/Да): '))
#     print('До всзрыва', N - sec, 'секунд.')
#     if question == 1:
#         print('Бомба обезврежена!')
#         break
#     if sec == N:
#         print('Бомба взорвалась!')
# 5 ==========================================================================
# print('=' * 50)
# N = int(input('Сколько уже вскопали бабушка с дедушкой? '))
# K = int(input('Через сколько метров друг от друга посажена картошка? '))
# met = ''
# summ = 0
# for meter in range(N, 100, K):
#     met = met +' '+ str(meter)
#     # print('Вскапывается', meter,'- я грядка')
#     summ += 3
# print("Вскопанные грядки:", met)
# print('Антон соберет', summ, 'клубней картошки.')
# print('=' * 50)
# 6 ==========================================================================
# N = int(input('Сколько лет было дереву? '))
# K = int(input('Через сколько будем сажать? '))
# summ = 0
# for year in range(6, N, K):
#     num = int(input('Сколько посадить деревьев на ' + str(year)+'-й год? '))
#     summ += num
# print('В сумме за', N,'лет было посажено', summ, 'деревьев.')
# 7 ==========================================================================
# a = int(input('Введите границу а: '))
# b = int(input('Введите границу b: '))
# c = int(input('Введите делитель с: '))
# tot = 0
# count = 0
# for num in range(a, b+1):
#     if num % c == 0:
#         tot += num
#         count += 1
#         print(count,'-е число кратное', c,'на отрезке [a; b] равно:', num)
# print('Среднее арифметическое чисел =', tot/count)
# 8 ==========================================================================
# start = int(input('Введите начало отрезка: '))
# stop = int(input('Введите конец отрезка: '))
# step = int(input('Введите шаг: '))
# for x in range(stop, start-1, step):
#     y = x**3 + 2*x**2 - 4*x + 1
#     print('В точке x =', x, 'функция y равна', y)
# 9 ==========================================================================

# print("=====================================================================================")
# print("=====================================================================================")
# letter = int(input('Введите длину стороны квадратного письма: '))
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# count = 0
# for side in range(letter, 12-1, -12):      # side - сторона
#     print("Размер стороны письма:", side-12)
#     if side > 12:
#         count += 1
#     elif side <= 12:
#         break
#     print("Письмо было сложено: ", count, "раз.")
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("В итоге:\nЧтоб письмо поместить в конверт,\nего нужно сложить: ", 2*count, "раз.")
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 10 ==========================================================================
# print("=====================================================================================")
# print("=====================================================================================")
# educational_grant = int(input('Введите ежемесячную стипендию студента: '))      # educational grant - Ежемесячная стипендия
# expenses = int(input('Введите расходы в месяц: '))              # expenses - расходы
# debt = expenses - educational_grant                             # debt - долг
# print("-----------------------------------------")
# print('Расходы в 1-й месяц:', expenses)
# print('Долг в 1-й месяц:', debt)
# print("-----------------------------------------")
# summ = debt
# if expenses > educational_grant:
#     for month in range(2, 11):
#         expenses = expenses + expenses * 0.03
#         debt_month = expenses - educational_grant
#         debt += expenses - educational_grant
#         # summ = summ + debt
#         print(month, '- й месяц:')
#         print('Расходы: ', expenses)
#         print('Долг в текущем месяце: ', debt_month)
#         print('Суммарный долг: ', debt)
#         print("-----------------------------------------")
#     print('Чтоб жить без долгов, родители должны дать в начале года', debt, 'рублей!\n``````````````````````````````````````````````````````````````````````````````````````')
# else:
#     print('Неверный ввод!\nРасходы на проживание должны превышать ежемесячную стипендию студента!')
# 11 ==========================================================================
# print("=====================================================================================")
# print("=====================================================================================")
# N = int(input('Введите натуральное число: '))
# s = 1
# for num in range(1, N+1):
#     s += (-1)**num * 1/2**num
#     print(s)
# print('Сумма =', s)
# 12 ==========================================================================
# print("=====================================================================================")
# print("=====================================================================================")
# x = int(input('Введите число x: '))
# j = 1
# s_2 = 0
# s_1 = 0
# for num in range(1, 100, 1):
#     j *= 2
#     i = j - 1
#     s_1 += x - i
#     s_2 += x - j    
#     print('num =', num, '=>> i =', i, '; j =', j)
#     total = s_1 / s_2
#     if j >= 64:
#         break
# print("-------------------------------------------------------")
# print('s_1 =', s_1, '; s_2 =', s_2)
# print('total = s_1 / s_2 =',s_1,'/',s_2,'=', total)
# print("-------------------------------------------------------")
# 13 ==========================================================================
# print("=====================================================================================")
# print("===================================   0 ≤ c ≤ d   ===================================")
# a = 1 # int(input('Введите число a: '))
# b = 200 # int(input('Введите число b: '))
# c = 50 # int(input('Введите число c: '))
# d = 100 # int(input('Введите число d: '))
# print("--------------------------")
# for num in range(a, b+1):
#     # print(num, '/', d,'=', num / d,'   |   num // d =', num // d,'   |   num % d =', num % d)
#     if num % d == c:
#         print(num)
# 14 ==========================================================================
# Сам не решил
M = int(input('Сколько мальчиков? '))
D = int(input('Сколько девочек? '))
answer = ''
if (M > 2 * D) or (D > 2 * M):
    print('Рассадить по условию не получится!\nРешений нет!')
elif M >= D:
    MDM = M - D
    for mdm in range(1, MDM + 1):
        answer += 'MDM '
    MD = D - MDM
    for md in range(1, MD + 1):
        answer += 'MD '
else:
    DMD = D - M
    for dmd in range(1, DMD + 1):
        answer += 'DMD '
    DM = M - DMD
    for dm in range(1, DM + 1):
        answer += 'DM '
print(answer)
