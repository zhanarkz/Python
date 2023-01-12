# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2  друга оказались не такими смышлеными. 
# Никто из ребят не смог до конца сделать это задание. 
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам.

# Ваня:                           Петя:
# n = int(input())                n = int(input())
# max_number = 1000               max_number = -1
# while n != 0:                   while n < 0:
#    n = int(input())             n = int(input())
#    if max_number > n:           if max_number < n:
#        max_number = n           n = max_number
# print(max_number)               print(n)


n = int(input('enter a number '))
if n !=0:
    max_number = n
    while n!= 0:
        if max_number < n:
            max_number = n
        n = int(input('enter next number '))
    print(max_number)
else:
    print('no number')




   
   
       
