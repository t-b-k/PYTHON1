# Задача № 1. 
# Даны два массива чисел. 
# Требуется вывести те элементы первого массива, которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, 
# затем N чисел - элементов 1-го массива. 
# Затем число М  - количество элементов во втором массиве и элементы второго массива. 

count1 = int(input('Введите кол-во элементов в первом массиве => '))
list_1 = []
for _ in range(count1) : 
    list_1.append(int(input('\tЭлемент массива 1 => ')))

count1 = int(input('Введите кол-во элементов в первом массиве => '))
list_2 = []
for _ in range(count1) : 
    list_2.append(int(input('\tЭлемент массива 1 => ')))

print([x for x in list_1 if x not in set(list_2)])

