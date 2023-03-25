values = [1, 23, 42, 'asdf']

transformation = lambda x: x
transformed_values = list(map(transformation, values))

if values == transformed_values: 
    print('ok')
else : 
    print('fail')


# Список относится к изменяемым типам данных. 
# Строки, кортежи - неизменяемые, и их можно присваивать. 