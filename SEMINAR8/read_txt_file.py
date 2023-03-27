import os
from tabulate import tabulate 

all_data = []
last_id = 0

def read_records_from_txt (txt_file_name) : 
    global last_id, all_data
    with open (txt_file_name, "r", encoding="utf-8") as f: 
        for next_line in f : 
            last_id += 1
            all_data.append([str(last_id), *next_line.strip().split()])

read_records_from_txt ("base2.txt") 
print(all_data)
# print(all_data[3])

# headers = ["ID", "Фамилия", "Имя", "Отчество", "Номер телефона"]
# print()

columns = ["ID", "Фамилия", "Имя", "Отчество", "Номер телефона"]
for i in range(len(all_data)) :
    for j in range(1,5) : 
        print(all_data[i][j], end = ' ')
    print()

# list_to_print.append(all_data[i][0] + all_data[1].split())
print(tabulate(all_data, headers=columns))
print()

