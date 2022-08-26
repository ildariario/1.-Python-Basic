# Разбоор ДЗ
"""Задача 6. Магия (!)
Для одной игры необходимо реализовать механику магии, где при соединении двух
элементов получается новый. У нас есть четыре базовых элемента: «Вода», «Воздух»,
«Огонь», «Земля». Из них как раз и получаются новые: «Шторм», «Пар», «Грязь»,
«Молния», «Пыль», «Лава».

Вот таблица преобразований:
  Вода + Воздух = Шторм
  Вода + Огонь = Пар
  Вода + Земля = Грязь
  Воздух + Огонь = Молния
  Воздух + Земля = Пыль
  Огонь + Земля = Лава

Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо
организовать как отдельный класс. Если результат не определён, то возвращается None.

Примечание: сложение объектов можно реализовывать через магический метод __add__,
вот пример использования:

class Example_1:
    def __add__(self, other):
        return Example_2()

class Example_2:
    answer = 'сложили два класса и вывели'

a = Example_1()
b = Example_2()
c = a + b
print(c.answer)

Дополнительно: придумайте свой элемент (или элементы), а также реализуйте его
взаимодействие с остальными элементами.
"""


class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        else:
            return None


class Earth:
    def __str__(self):
        return 'Земля'


class Storm:
    def __str__(self):
        return 'Шторм'


class Vapor:
    def __str__(self):
        return 'Пар'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


water = Water()
air = Air()
fire = Fire()
earth = Earth()
print(water + air, water + fire, water + earth)
print(air + fire, air + earth)
print(fire + earth)
