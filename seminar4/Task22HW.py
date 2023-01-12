# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12
# множества
# пересечение
# рандом
import random
n = int(input('кол-во элементов первого набора '))
m = int(input('кол-во элементов второго набора '))
list1 = [random.randint(1, 10) for i in range(n)]
list2 = [random.randint(1, 10) for i in range(m)]
print('first list ', list1)
print('second list ', list2)

a = set(list1)
b = set(list2)
print('first list uniques number ', a)
print('second list unique numbers ', b)
i = a.intersection(b)
print('repeated numbers are ', sorted(i))
