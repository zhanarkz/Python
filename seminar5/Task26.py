# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

one = int(input('введите первое число '))
two = int(input('введите второе число '))

def degree (a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * degree(a, b -1))

print(degree(one, two))