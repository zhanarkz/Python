# Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), 
# не превосходящие числа N.
# 5
# 1 2 4
# 17
# 1 2 4 8 16

# def degree(N):
#     numbers=[]
#     for x in range(N):
#         if x < N and x > 1:
#             if x % 2 == 0:
#                 numbers.append(x)
#     return(numbers)

# n = int(input('Введите число '))
# print(degree(n))

n = int(input('Введите число '))
i = 1
while i <= n:
    i *= 2
    if i % 2 == 0:
        print(i)
    else:
        print('wrong')
