# Напишите программу, которая принимает на вход строку и
# к каждому символу через подчерк добавляет количество его вхождений в строку: 
# Вход:     aaabcaadcdd
# Выход:    a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию split()

# РЕШЕНИЕ: 
# string = list(input())
# print(string)

# result = dict.fromkeys(string, 0)
# print(result)

# for i in string : 
#     if result[i] == 0 :
#         print(i, end=' ')
#     else : 
#         print(i+'_', result[i], end=' ')
#     result[i] += 1
# print()

# РЕШЕНИЕ НА СЕМИНАРЕ: (предполагается, что символы вводятся через пробел)

# text = input().split()
# print(text)

# my_dict={}
# for i in text: 
#     if i in my_dict : 
#         print(f"{i}_{my_dict[i]}", end=' ')
#     else : 
#         print(i, end = ' ')
#     my_dict[i] = my_dict.get(i,0) + 1

# Метод get(<ключ>, [<значение по умолчанию>]) - 
# возвращает значение по ключу. Если такого ключа не существует - 
# значение по умолчанию. 
# Запишем это же решение в сжатой форме: 

chars = input().split()
dict_chars = {}.fromkeys(chars,0)
print(dict_chars)

for i in chars : 
    print(f'{i}_{dict_chars[i]}' if dict_chars[i] else i, end=' ')
    dict_chars[i] += 1    
    
