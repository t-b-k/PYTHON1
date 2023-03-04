# Задача 4: 
# Требуется определить, можно ли от шоколадки размером n x m долек 
# отломить k долек, если разрешается сделать ровно один разлом 
# по прямой между дольками (то есть, разломить шоколадку на два прямоугольника)

# В шоколадке n x m п "строк" по m клеточек и m "столбцов" по n клеточке. 
# Следовательно, какое бы количество клеточек мы не отломили от нее одним разломом, 
# полученное число отломленных долек будет обязательно кратно или m, или n
# Все остальные варианты невозможны. 

rows_in_chocolate = int(input("Введите размеры шоколадки: \n\nn = "))
columns_in_chocolate = int(input("m = "))

qty_of_pieces = rows_in_chocolate * columns_in_chocolate

pieces_to_break_off = int(input("Сколько долек Вы хотели бы отломить? => "))

result = False

if pieces_to_break_off > 0 and pieces_to_break_off < qty_of_pieces : 
    result = not pieces_to_break_off % rows_in_chocolate or not pieces_to_break_off % columns_in_chocolate

if result : 
    print (f"Это возможно")
else: 
    print (f"Это невозможно")