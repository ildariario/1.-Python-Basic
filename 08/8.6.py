# Home Work
# 1 ==========================================================================
'''Задача 1. Космическая еда
Ваш космический корабль потерпел крушение на пустынной планете. Еда здесь не растёт,
но вы спасли из обломков 100-килограммовый мешок гречки. Из прошлого опыта вы знаете,
что если будете экономно питаться, то у вас будет уходить по 4 килограмма гречки в месяц.
Чтобы прикинуть гречневый бюджет, вы решили написать программу, которая выведет информацию
о том сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее,
пока она не закончится. Используйте цикл for.
'''
# count = 0
# for buckwheat in range(100, -1, -4):           # buckwheat - гречка
#     count += 1
#     print('Прошел', count, 'месяц. Гречки осталось', buckwheat, 'кг.')
# 2 ==========================================================================
'''Задача 2. Сумма нечетных
Напишите программу, которая вычисляет сумму нечётных чисел, лежащих в диапазоне от единицы 
до указанного пользователем числа включительно.
'''
# n = int(input('Введите число: '))
# summ = 0
# for num in range(1, n+1, 2):
#     print(num)
#     summ += num
# print(summ)
# 3 ==========================================================================
'''Задача 3. Долги
МирПрогБанк наконец-то разделил законопослушных граждан и должников и поместил их в разные 
базы. Но банк не торопится как-то слишком сильно давить на возврат денег. Сейчас операторам 
банка дали задание позвонить каждому пятому должнику из списка (они нумеруются с нуля) и 
спросить, сколько примерно денег каждый из них задолжал банку.
Напишите программу, которая принимает на вход количество должников, затем спрашивает у 
каждого пятого (начиная с 0) его долг. В конце выводится общая сумма долгов.
Пример:
Введите количество должников: 13
Должник с номером 0
Сколько должны? 1000
Должник с номером 5
Сколько должны? 5000
Должник с номером 10
Сколько должны? 2000
Общая сумма долга: 8000
'''
# n = int(input('Введите число должников: '))
# summ = 0
# for debtor in range(0, n, 5):       # debtor - должник
#     print('Должник с номером:', debtor)
#     debt = int(input('Сколько должны? '))        # debt - долг
#     summ += debt
# print('Общая сумма долга: ', summ)
# 4 ==========================================================================
'''Задача 4. Это будет бомба
Мы разрабатываем пошаговую игру по мотивам боевика. Игрок - главный герой и должен 
обезвредить бомбу, которая взорвётся через N секунд. Программа спрашивает пользователя 
хочет ли он обезвредить бомбу сейчас. Если ответ “0” (то есть “нет”), то счетчик 
бомбы уменьшается. Если он достиг нуля, то программа выдаёт сообщение “Бомба взорвалась”, 
а если не достиг, то программа вновь переспрашивает, не хочет ли игрок обезвредить 
бомбу, и сообщает, сколько времени осталось до взрыва.. Если ответ “да”, то программа 
выводит на экран сообщение о том, что бомба обезврежена и сколько секунд оставалось 
до взрыва. Используйте цикл for.
'''
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
'''Задача 5. Антошка, пора копать картошку
Антона отвезли на дачу и опять заставили копать картошку. А он даже рад, ему она очень 
нравится. Правда, бабушка с дедушкой до его приезда уже вскопали N метров, поэтому он 
начнёт там, где закончили они. Вся грядка занимает 100 метров и на ней помимо картошки 
растут другие культуры. Но Антону нужна только картошка и больше ничего. Антон знает, 
что она посажена каждые K метров. То есть через каждые K метров он останавливается и 
выкапывает 3 клубня картошки Напишите программу, которая посчитает сколько клубней 
картошки соберёт Антон.
'''
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
'''Задача 6. Грустная история
Алёне было всего 6 лет, когда она узнала страшную новость - спилили её любимое дерево за 
домом. Этому дереву было N лет, Алёна очень часто сидела под ним и мечтала. Тогда она 
решила, что каждые K лет будет садить вокруг деревья до тех пор, пока ей самой не станет N лет.
Напишите программу, которая получает на вход возраст дерева N, а затем каждые K лет, начиная 
с 6 спрашивает у пользователя “Сколько посадить деревьев?”. В конце выведите сколько всего 
в сумме было посажено деревьев.
'''
# N = int(input('Сколько лет было дереву? '))
# K = int(input('Через сколько будем сажать? '))
# summ = 0
# for year in range(6, N, K):
#     num = int(input('Сколько посадить деревьев на ' + str(year)+'-й год? '))
#     summ += num
# print('В сумме за', N,'лет было посажено', summ, 'деревьев.')
# 7 ==========================================================================
'''Задача 7.
Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль 
среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу c.
'''
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
'''Задача 8. Функция 2
В прошлый раз мы написали Саше программу, которая считает функцию в каждой точке отрезка и выводит значение 
на экран. Но теперь ему нужно, чтобы значения считались в обратном порядке. Плюс к этому в программе ему 
нужно сделать так, чтобы можно было настраивать шаг, с которым он скачет по точкам отрезка.
Напишите программу, которая получает на вход начало и конец отрезка, а также шаг. Затем высчитывает функцию 
игрек в каждой точке отрезка и с нужным шагом, начиная с конца, и выводит ответ на экран.
Сама функция выглядит так: y = x^3 + 2*x^2 - 4*x + 1
 
Пример:
Введите начало отрезка: -2
Введите конец отрезка: 2
Введите шаг: -1
В точке 2 функция равна 9
В точке 1 функция равна 0
В точке 0 функция равна 1
В точке -1 функция равна 6
В точке -2 функция равна 9
'''
# start = int(input('Введите начало отрезка: '))
# stop = int(input('Введите конец отрезка: '))
# step = int(input('Введите шаг: '))
# for x in range(stop, start-1, step):
#     y = x**3 + 2*x**2 - 4*x + 1
#     print('В точке x =', x, 'функция y равна', y)
# 9 ==========================================================================
'''Задача 9. Письмо
У нас есть квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги, которое 
не помещается в конверт. Напишите программу, которая подскажет сколько раз нужно сложить письмо пополам, 
чтобы оно поместилось в конверт. Размеры письма вводятся с клавиатуры.
'''
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
'''Задача 10. Стипендия
Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают 
стипендию и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме 
первого месяца. Составьте программу расчета суммы денег, которую необходимо получить у родителей один 
раз в начале обучения, чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги 
и стипендию.
'''
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
'''Задача 11. Сумма ряда
Дано натуральное число N. Напишите программу для вычисления следующей суммы ряда (начиная с единицы)
S = 1 - 1/2 + 1/4 + ... + (-1)^N * 1/2^N
'''
# N = int(input('Введите натуральное число: '))
# s = 1
# for num in range(1, N+1):
#     s += (-1)**num * 1/2**num
#     print(s)
# print('Сумма =', s)
# 12 ==========================================================================
'''Дано число x. Напишите программу для вычисления следующего выражения
((x-1)*(x-3)*(x-7)*...*(x-63))/((x-2)*(x-4)*(x-8)*...*(x-64))
'''
# x = int(input('Введите число x: '))
# j = 1
# s_1 = 1
# s_2 = 1
# for num in range(1, 100, 1):
#     j *= 2
#     i = j - 1
#     s_1 *= x - i
#     s_2 *= x - j
#     print('num =', num, '=>> i =', i, '; j =', j, '; s_1 =', s_1, '; s_2 =', s_2)
#     if j >= 64:
#         break
# total = s_1 / s_2
# print("-------------------------------------------------------")
# print('s_1 =', s_1, '; s_2 =', s_2)
# print('total = s_1 / s_2 =', s_1, '/', s_2, '=', total)
# print("-------------------------------------------------------")
# 13 ==========================================================================
'''Задача 13. Остатки
Даны целые неотрицательные числа a b c d, при этом 0≤c≤d. Выведите в порядке возрастания 
все числа от a до b, которые дают остаток c при делении на d.
'''
# print("===================================   0 ≤ c ≤ d   ===================================")
# a = 1    # int(input('Введите число a: '))
# b = 200  # int(input('Введите число b: '))
# c = 50   # int(input('Введите число c: '))
# d = 100  # int(input('Введите число d: '))
# print("--------------------------")
# for num in range(a, b+1):
#     # print(num, '/', d,'=', num / d,'   |   num // d =', num // d,'   |   num % d =', num % d)
#     if num % d == c:
#         print(num)
# 14 ==========================================================================
'''Задача 14. Кинотеатр (необязательно)
X мальчиков и Y девочек пошли в кинотеатр и купили билеты на подряд идущие места в одном 
ряду. Напишите программу, которая выдаст, как нужно сесть мальчикам и девочкам, чтобы рядом 
с каждым мальчиком сидела хотя бы одна девочка, а рядом с каждой девочкой — хотя бы один 
мальчик.
На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y. В ответе выведите 
какую-нибудь строку, в которой будет ровно X символов “B” (обозначающих мальчиков) и Y 
символов “G” (обозначающих девочек), удовлетворяющую условию задачи. Пробелы между 
символами выводить не нужно. Если рассадить мальчиков и девочек согласно условию задачи 
невозможно, выведите строку “Нет решения”.
Пример 1:
Введите кол-во мальчиков: 5
Введите кол-во девочек: 5
Ответ: BGBGBGBGBG
Пример 2:
Введите кол-во мальчиков: 5
Введите кол-во девочек: 3
Ответ: BGBGBBGB
Пример 3:
Введите кол-во мальчиков: 100
Введите кол-во девочек: 1
Ответ: Нет решения
'''
# Сам не смог решить
# M = int(input('Сколько мальчиков? '))
# D = int(input('Сколько девочек? '))
# answer = ''
# if (M > 2 * D) or (D > 2 * M):
#     print('Рассадить по условию не получится!\nРешений нет!')
# elif M >= D:
#     MDM = M - D
#     for mdm in range(1, MDM + 1):
#         answer += 'MDM '
#     MD = D - MDM
#     for md in range(1, MD + 1):
#         answer += 'MD '
# else:
#     DMD = D - M
#     for dmd in range(1, DMD + 1):
#         answer += 'DMD '
#     DM = M - DMD
#     for dm in range(1, DM + 1):
#         answer += 'DM '
# print(answer)
