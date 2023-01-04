# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
import random

n = int(input('введите количество монет  '))
coins = []
for num in range(n):
    coins.append(random.randint(0,1))
print(f'you have coins {coins} ')

heads = sum(coins)
tails = n - heads #reshka

if heads == 0 and heads == n:
    print('все идеально')
elif heads == tails:
    print('без разницы какую часть переворачивать')
elif heads < tails:
    print('решок больше, переверни орлов')
elif heads > tails:
    print('орлов больше, переверни решки')



