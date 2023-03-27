import os

all_data = []
last_id = 0

def read_records_from_txt (txt_file_name) : 
    global last_id, all_data
    with open (txt_file_name, "r", encoding="utf-8") as f: 
        for next_line in f : 
            last_id += 1
            all_data.append([str(last_id), *next_line.strip().split()])

def write_records_to_txt (txt_file_name) :
    global all_data
    with open (txt_file_name, "w", encoding="utf-8") as f : 
        for i in all_data : 
            f.writelines(" ".join(i[1:])+"\n")

read_records_from_txt ("raw_base.txt") 
write_records_to_txt ("base1.txt")

