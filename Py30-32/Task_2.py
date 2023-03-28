# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

my_list = [random.randint(1, 101) for i in range(1, 20)]
print(my_list)

min_num = int(input("Enter the lower bond of the interval "))
max_num = int(input("Enter the higher bond of the interval "))


for i in range(0, len(my_list)):
    if my_list[i] <=max_num and my_list[i]>=min_num:
        print('i = ', i)