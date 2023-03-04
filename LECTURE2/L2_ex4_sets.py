# Множество - это неупорядоченный набор уникальных значений
# Значение множества задается при помощи фигурных скобок, внутри которых 
# перечисляются все значения через запятую. 

colors = {'red', 'green', 'blue'}
print(colors)

colors.add('red')
print(colors) # Ничего не изменится, поскольку значение 'red' уже было в данном множестве

colors.add('gray')
print(colors) # Добавится значение 'gray'

# Функция remove() удаляет из множества существующее значение. 
# Если такого значения нет, она возвращает ошибку

colors.remove('red')
print(colors)

# Функция discard() удаляет значение, если оно есть во множестве. 
# Если такого значения во множестве нет, она просто ничего не делает. 

colors.discard('red')  # ok
print(colors)

# Очистка множества - удаление из него всех элементов

colors.clear()
print(colors)

# Операции над множествами

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

c = a.copy(); 
print(c)

u = a.union(b)
print(u)

i = a.intersection(b)
print(i)

dl = a.difference(b)
dr = b.difference(a)
print(dl, dr)

q = a.union(b).difference(a.intersection(b))
print(q)

# ЗАМОРОЖЕННЫЕ МНОЖЕСТВА

s = {1, 8, 6}
z = frozenset(s)

# Замороженное множество нельзя изменить

print(z)





