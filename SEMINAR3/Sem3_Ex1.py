# Задача 1. 
# Дан список чисел. 
# Определить, сколько в нем встречается различных чисел. 
# Пользователь может сам вводить список, или он может быть задан программно

# РЕШЕНИЕ: 

qty = int(input("Сколько значений Вы планируете ввести? => "))

numbers = []  # сформировали пустой список
for i in range (qty) : 
    numbers.append(int(input("Введите число : ")))

print(numbers)
num_values = len(set(numbers))  # Преобразовали список в массив и посчитали в нем количество элементов
print(num_values)

