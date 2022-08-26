"""Работа за преподавателем"""
# Task 1

# import garden
#
#
# my_garden = garden.PotatoGarden(5)
# my_garden.are_all_ripe()
# for _ in range(3):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()

# Task 2

# from garden import *
#
#
# my_garden = PotatoGarden(5)
# my_garden.are_all_ripe()
# for _ in range(3):
#     my_garden.grow_all()
#     my_garden.are_all_ripe()

# Task 3

from garden import PotatoGarden


my_garden = PotatoGarden(5)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()
