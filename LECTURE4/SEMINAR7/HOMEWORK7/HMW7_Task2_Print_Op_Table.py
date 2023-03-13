# Напишите функцию print_operation_table(operation, num_rows=6, num_rows=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру 
# строки и столбца. 
# Аргументы num_rows и num_columns задают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы. 
# ПРИМЕЧАНИЕ: Бинарной операцией называется любая операция, у которой ровно 
# два аргумента, как, например, у операции умножения. 

def print_operation_table(operation, num_rows=6, num_columns=6) : 
    matrix = [[j+1 for j in range(num_columns)]]
    for i in range(1, num_rows) : 
        matrix.append([i+1])
        matrix[i].extend([operation(i+1,j+1) for j in range(1,num_columns)])
    
    for row in matrix : 
        for item in row : 
            print("%3d" %(item), end=' ')
        print()
    
print_operation_table(lambda i, j : i*j)
# print_operation_table(lambda i, j : i*j, 5, 2)
# print_operation_table(lambda i, j : i*j, 1, 1)
# print_operation_table(lambda i, j : i*j, 2, 2)
# print_operation_table(lambda i, j : i*j, 8, 10)

        
