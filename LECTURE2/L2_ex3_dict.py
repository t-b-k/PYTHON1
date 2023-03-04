# Словари - это неупорядоченные коллекции произвольных объектов с доступом по ключу
# В списках в качестве ключа используется индекс элемента. 
# В словаре для определения элемента используется значение ключа (строка, число)

dictionary = {}

dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}

# Типы ключей могут различаться

print(dictionary)
print(dictionary['left'])
print(dictionary['right'])

dictionary['left'] = '⇐'
print(dictionary['left'])

# удаление элемента

del dictionary['left']
print(dictionary)

d = {}
d = dict()

# Добавление элементов в словарь

d['q'] = 'qwerty'
print(d)

d['w'] = 'werty'
print(d)

print(d['w'])
print(d['q'])

dictionary[895] = 98998

print(dictionary[895])

for item in dictionary: 
    print(item) # выведутся значения ключей

for item in dictionary: 
    print('{}: {}'.format(item, dictionary[item]))

print(dictionary.items())

for (k, v) in dictionary.items(): 
    print(k, v)


