# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input("Enter the first element of the progression: "))
difference = int(input("Enter the difference of the progression: "))
amount = int(input("Enter the total amount of the elements in the the progression: "))

progression = [(first_element + (i - 1)*difference) for i in range(1, amount + 1 )]

print(progression)