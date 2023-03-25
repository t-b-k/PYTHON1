import os

all_data = []
last_id = 0
database = 'base.txt'

def show_all () : 
    global all_data 
    if len(all_data) > 0 : 
        print("В справочние содержатся следующие записи: ")
        for i in all_data : 
           string_to_show = i.strip().split()
           string_to_show.pop(0)
           print(*string_to_show) 
    else: 
        print("В справочнике нет ни одной записи")

# Функция возвращает строку из букв и возвращает ту же строку, 
# преобразовав ее в Title. 
# Если пользователь не справился со вводом, возвращает пустую строку

def input_word () : 
    max_attempts = 3
    print("Введите фамилию (у вас {max_attempts} попытки(ок)): ")
    for i in range(max_attempts) : 
        surname = input(f"{i+1} - ")
        if surname != "" and surname.isalpha() : 
            return surname.title()
    return ""

# Функция возвращает строку с кодом страны. Если пользователь не справился 
# с вводом, возвращает пустую строку
def input_country_code () : 
    max_attempts = 3
    print("Введите код страны. У вас {max_attempts} попытка(ки)(ок)). ")
    print("Код страны содержит не более 3-х цифр. ")
    print("По умолчанию используется код России - +7")
    res = "" 
    for i in range(max_attempts) :   
        code = input(f"{i+1} - +")
        if code == "" : 
            res = "+007"
            return res
        elif code.isdigit() and int(code) > 0: 
            if len(code) == 1 : 
                res += "+00" + code
                return res 
            if len(code) == 2 : 
                res += "+0" + code
                return res
            if len(code) == 3 : 
                res += "+" + code
                return res
    return res    
 
# Функция возвращает строку с кодом города. Если пользователь не справился 
# с вводом, возвращает пустую строку
def input_city_code () : 
    max_attempts = 3
    print("Введите код города(оператора). У вас {max_attempts} попытка(ки)(ок)). ")
    print("Код города (оператора) содержит от 2-х до 5-ти цифр. ")
    res = "" 
    for i in range(max_attempts) :   
        code = input(f"{i+1} - ")
        if code.isdigit() and int(code) > 0 and len(code) in range(2,6) : 
            res = code
            return res
    return res    

# Функция возвращает строку с номером телефона внутри населенного пункта. 
# Если пользователь не справился с вводом, возвращает пустую строку
# Номер телефона может содержать от 5 до 8-ми цифр
def input_phone () : 
    max_attempts = 3
    print("Введите номер телефона. У вас {max_attempts} попытка(ки)(ок)). ")
    print("Номер телефона может содержать от 5-ти до 8-ми цифр. ")
    res = "" 
    for i in range(max_attempts) :   
        phone = input(f"{i+1} - ")
        if phone.isdigit() and int(phone) > 0 and len(phone) in range(5,9) : 
            res = phone
            return res
    return res   

def add_new_contact () : 
    new_contact = ""
    max_attempts = 3
    attempt_count = 1
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    while surname == '' and name == '' and attempt_count <= max_attempts: 
        print("Фамилия и имя оба не могут быть пустыми.")
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        attempt_count += 1
    if attempt_count > max_attempts : 
        print("К сожалению, создать контакт без имени и фамилии невозможно. ")
        return 0
    patronymic = input("Введите отчество: ")
    if (patronymic == "") : 
        patronymic = "----------" 
    phone_number = ""
    input("Введите номер телефона: ")
    max_attempts = 3
    attempt_count = 1
    country_code = input("  Введите код страны (только цифры). Enter, если Россия: ")
    if country_code == '' : 
        country_code == "+7"
    else: 
        while country_code.isdigit == 0 and attempt_count <= max_attempts: 
            country_code = input("  Введите код страны (только цифры): ")
            attempt_count += 1
    if attempt_count > max_attempts : 
        print("Вы не справились с вводом кода страны. Считаем, что это Россия (+7).")
        country_code == "+7"


def read_records() : 
    global last_id, all_data, database
    if last_id :  
        with open(database, encoding="utf-8") as f : 
            all_data = [i.strip() for i in f]
        
        return all_data
    return []

def launch_interaction () :
    global database, all_data, last_id
    print(f"По умолчанию используется справочник {database}")
    print("Если Вы хотите использовать этот справочник, введите   1")
    print("Если Вы хотите работать с другим справочником, введите 0")
    if (int(input("Ваш выбор? => ")) == 0) : 
        print("Введите путь к файлу, с которым хотите работать.")
        print("Если такого файла не существует, будет создан пустой справочник. ")
        database = input("С каким файлом хотите работать? =>")
    
    if not os.path.exists(database) : 
        with open (database, "w", encoding="utf-8") as _: 
            print(f"Создан новый телефонный справочник {database}")
    elif os.stat(database).st_size == 0 : 
        print(f"Телефонный справочник {database} пуст. В него можно только добавлять данные. ")
    else : 
        with open (database, "r", encoding="utf-8") as f: 
            last_line = f.readlines()[-1]
            last_id = int(last_line.split()[0])
            read_records()
            print("Справочник не пуст и готов к работе.")
    print(f"Индекс последней записи в справочнике равен {last_id}")
    # for i in all_data : 
    #     print(i)


# isempty = os.stat('path\to\file\filename.ext').st_size == 0
# isempty = os.stat('base1.txt').st_size == 0
# print(f"Файл, с которым вы хотите работать, пуст: {isempty}")



# read_records()
# for i in all_data : 
#     print(i)
# print(last_id)

# with open('base.txt','a', encoding="utf-8") as file :  
#     file.write(f"\n{last_id+1} Степанов Олег Геннадьевич 0079142374932")

# with open('base1.txt', 'r', encoding="utf-8") as file : 
#     for line in file : 
#         # str = file.readline()
#         print(line)
#         str = line.strip()
#         print(str)
#         str_to_list = str.split()
#         print(str_to_list)
#         ind = (int)(str_to_list[0])
#         print(ind)
#         cut_str_to_list = str_to_list
#         cut_str_to_list.pop(0)
#         print(cut_str_to_list)

        # work_str = str.pop(0)
        # print(ind)
        # print(work_str)

def main_menu () : 
    global all_data, last_id, database
    play = True
    while play : 
        answer = input("Введите команду: \n"
                       "1 - Показать все записи \n"
                       "2 - Добавить контакт \n"
                       "3 - Найти контакт по ключу \n"
                       "4 - Изменить контакт \n"
                       "5 - Удалить контакт \n"
                       "6 - Экспортировать/Импортировать данные в/из файла \n"
                       "7 - Завершить работу \n")
# Надо добавить Change, Import, Export
# Export - это выгрузка текущей базы в другой файл: Введите название
# будущей базы, пришиваем .txt, проверяем на существование, отдаем в бета-функцию
# import - это изменение переменной file_base на новое имя, которое
# предоставит пользователь. 

        match answer : 
            case "1": 
                show_all()
            case "2": 
                add_new_contact()
            case "3": 
                pass
            case "4": 
                pass
            case "5": 
                pass
            case "6": 
                pass
            case "7": 
                play = False
            case _ : 
                print("Try again!\n")

launch_interaction ()
show_all ()
# main_menu()       
