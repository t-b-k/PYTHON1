# Задача 2. 
# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних, и при этом оба соседних элемента меньше данного. 
# Сначала вводится число N - количество элементов в массиве. 
# Далее записаны N чисел - элементы массива. 

count = int(input('Введите кол-во элементов в первом массиве => '))
list = []
for _ in range(count) : 
    list.append(int(input('Введите элемент массива => ')))

print(len([1 for i in range(1,count-1) if list[i] > list[i-1] and list[i] > list[i+1] ]))

# for i in range(1, len(list_1)-1) : 
#     if list_1[i] == max(list_1[i-1:i+2]) : 
#         count_1 += 1
# print(count_1)

# print([len([i for i in range(1, len(list_1)-1) if list_1[i-1] < list_1[i] > list_1[i+2]])])