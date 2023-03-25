# Напишите функцию same_by(characteristics, objects), 
# которая проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращает True, если это так. 
# Для пустого набора объектов функция должна возвращать True. 
# Аргумент haracteristic - это функция, которая принимает объект 
# и вычисляет его характеристику

# values = [0, 2, 10, 6]
# def same_by (lambda x: x % 2, values) : 
#   print('same')
# else: 
#   print('different')

values = [0, 2, 10, 6]

def same_by (characterictics, objects) : 
    if not objects : 
        return len(set(map(characterictics, objects))) == 1

if same_by (lambda x: x % 2, values) : 
    print('same')
else: 
    print('different')


