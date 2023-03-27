import os
from tabulate import tabulate 

all_data = []
last_id = 0
database = 'raw_base.txt'

def read_records_from_txt (txt_file_name) : 
    global last_id, all_data
    with open (txt_file_name, "r", encoding="utf-8") as f: 
        for next_line in f : 
            last_id += 1
            all_data.append([str(last_id), *next_line.strip().split()])

read_records_from_txt (database) 
print(all_data)

fragment = input("Введите строку для поиска: ")
print(f"Вы ввели строку {fragment}")

def find_records_by_fragment (data, fragment) : 
    found_records = []
    for i in range(len(data)) : 
        print (f"i = {i}")
        result = False
        for j in range(1, len(data[i])) : 
            print (f"Внутренний цикл для i = {i}")
            element = data[i][j].lower()
            print(f"Проверяем {data[i][j]}")
            if fragment.lower() in element : 
                result = True
                break
        print(result)
        if result : 
            found_records.append(data[i])
    return found_records

search_result = find_records_by_fragment (all_data, fragment)
columns = ["ID", "Фамилия", "Имя", "Отчество", "Номер телефона"]
print(tabulate(search_result, headers=columns))

# print(all_data[3])

# headers = ["ID", "Фамилия", "Имя", "Отчество", "Номер телефона"]
# print()

# columns = ["ID", "Фамилия", "Имя", "Отчество", "Номер телефона"]
# for i in range(len(all_data)) :
#     for j in range(1,5) : 
#         print(all_data[i][j], end = ' ')
#     print()

# list_to_print.append(all_data[i][0] + all_data[1].split())
# print(tabulate(all_data, headers=columns))
# print()

