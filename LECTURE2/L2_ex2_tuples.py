t = ()
print(type(t))  # результат - class 'tuple'>

t = (1)
print(type(t))  # результат - class 'int'

t = (1, 5, 3)
print(t)
print(type(t))

v = [1, 8, 9]
print(v)
print(type(v))

v = tuple(v) # Преобразовали спиок в кортеж

print(v)
print(type(v))

# Множественное присваивание: распаковка кортежа в отдельные переменные

a, b, c = v

print(a, b, c)

# Посмотрим, чем кортеж отличается от списка. 
# Создадим еще раз кортеж

t = (1, 2, 3, 4, 5)

print(t)

for i in t: 
    print(i)

for i in range(len(t)): 
    print(t[i])

# Попробуем изменить 1-й элемент

# t[0] = 2
# Ничего не получится, будет выдана ошибка

# А со списком такой номер пройдет

v = [1, 2, 3, 4, 5]
print(v)
v[0] = 2
print(v)






