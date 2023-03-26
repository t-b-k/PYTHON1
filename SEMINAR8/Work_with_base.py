import os
from tabulate import tabulate
import keyboard

all_data = []
last_id = 0
database = 'raw_base.txt'
phone_length_in_symbols = 18
country_code_in_symbols = 4

# def press_enter_to_continue() : 
#     print("---------Нажмите Enter для продолжения----------")
#     keyboard.wait('\r')
#     print()

# Функция проверяет файл с именем file_name на существование и пустоту
# -1 - такого файла нет
# 0 - файл существует, но он пустой
# 1 - файл существует и не пуст

def file_exists_and_not_empty (file_name) : 
    if not os.path.exists(file_name) : 
        return -1
        # print(f"Создан новый телефонный справочник {database}")
    elif os.stat(file_name).st_size == 0 : 
        # print(f"Телефонный справочник {database} пуст. В него можно только добавлять данные. ")
        return 0
    else : 
        return 1

# Фунция считывает данные из .txt-файла с телефонным справочником
# Данные хранятся в виде списка списков строк, каждая из которых 
# содержит, соответственно, ID, Фамилию, Имя, Отчество, Телефон   
# Данные упорядочены по возрастанию ID
# ID нумеруются с 1
# ID присваивается и закрепляется за контактом навсегда в момент записи его в
# в all_data. 

def read_records_from_txt (txt_file_name) : 
    global last_id, all_data
    with open (txt_file_name, "r", encoding="utf-8") as f: 
        for next_line in f : 
            last_id += 1
            all_data.append([str(last_id), *next_line.strip().split()])

def show_records (data) : 
    # global all_data 
    # if len(all_data) == 0 : 
    #     print("В настоящий момент данные в справочнике отсутствуют")
    # else: 
    columns = ["ID", "Фамилия", "Имя", "Отчество", "Номер телефона"]
    print(tabulate(data, headers=columns))
    print()

# Функция возвращает 1, если все готово к взаимодействию со справочником, 
# 0 - если обнаружены проблемы

def launch_interaction () :
    global database, all_data, last_id
    print(f"По умолчанию используется справочник {database}")
    print("Если Вы хотите использовать этот справочник, введите   1")
    print("Если Вы хотите работать с другим справочником, введите 0")
    user_choice = int(input("Ваш выбор? => "))

    if (user_choice == 0) : 
        print("Введите путь к файлу, с которым хотите работать.")
        print("Если такого файла не существует, будет создан пустой справочник. ")
        file_to_use = input("С каким файлом .txt хотите работать? =>")
        if file_to_use[-4:].lower() != ".txt" : 
            print("Справочник может находиться только в файле .txt")
            return 0
        else :
            database = file_to_use
            answer =  file_exists_and_not_empty(database)
            if answer == 1 :
                print("Такой справочник существует. Будем работать с ним. ") 
                read_records_from_txt(database)
            elif answer == 0 : 
                print("Справочник пуст. Его прежде придется наполнить.")
            else : 
                print("Такого файла не существует. Будет создан новый файл с таким именем.")
                with open (database, "w", encoding="utf-8") as _ : 
                    pass
            return 1
    elif  user_choice == 1 : 
        print(f"Работаем с базой {database}") 
        read_records_from_txt(database)
        return 1
    else : 
        print(f"Вы ввели недопустимое значение") 
        print(f"Программа завершает свою работу")
        return 0

# Функция принимает из консоли целое положительное число. 
# Если введено что надо, возвращает это число
# Иначе возвращает 0

#####################################################################
def input_positive_integer (max_attempts) : 
    # max_attempts = 3
    for i in range(max_attempts) : 
        id = input(f"{i+1}-я попытка =>  ")
        if id != "" and id.isdigit() and int(id) > 0: 
            return int(id)
    return 0
#####################################################################

# Функция принимает из консоли буквенную строку и возвращает ее же, 
# преобразованную в Title. 
# Если пользователь не справился со вводом, возвращает пустую строку

def input_word (max_attempts) : 
    # max_attempts = 3
    for i in range(max_attempts) : 
        surname = input(f"{i+1}-я попытка =>  ")
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
        code = input(f"{i+1}-я попытка => +")
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
 
# Функция возвращает строку с кодом города, заключенным в круглые скобки. 
# Если пользователь не справился с вводом, возвращает пустую строку
def input_city_code () : 
    max_attempts = 3
    print("Введите код города(оператора). У вас {max_attempts} попытка(ки)(ок)). ")
    print("Код города (оператора) содержит от 2-х до 5-ти цифр. ")
    res = "" 
    for i in range(max_attempts) :   
        code = input(f"{i+1}-я попытка => ")
        if code.isdigit() and int(code) > 0 and len(code) in range(2,6) : 
            res = "(" + code + ")"
            break
    print(f"Код гороода - {res}")
    return res    

# Функция возвращает строку с номером телефона внутри населенного пункта. 
# Если пользователь не справился с вводом, возвращает пустую строку
# Номер телефона может содержать от 5 до 8-ми цифр
def input_phone (phone_length) : 
    max_attempts = 3
    print("Введите номер телефона. У вас {max_attempts} попытка(ки)(ок)). ")
    print(f"Номер телефона {phone_length} цифр без посторонних символов ")
    print("и он не может состоять из одних нулей. ")
    res = "" 
    for i in range(max_attempts) :   
        phone = input(f"{i+1}-я попытка => ")
        length = len(phone)
        if length == phone_length and phone.isdigit() and int(phone) > 0 : 
            res = phone[:length-4] + "-" + phone[length-4:length-2] + "-" + phone[length-2:]
            break
    print(f"Номер телефона внутри города: {res}")
    return res   

# Контакт - это список строк: "ID", "Фамилия", "Имя", "Отчество", "Телефон"
def add_new_contact () : 
    global all_data, last_id
    new_contact = []
    success = False
    max_attempts = 3
    attempt = 1
    while not success and attempt <= max_attempts : 
        print("Введите фамилию (у вас {max_attempts} попытки(ок)): ")
        surname = input_word(max_attempts)
        print("Введите имя (у вас {max_attempts} попытки(ок)): ")
        name = input_word(max_attempts)
        success = surname != "" or name != ""
        if success : 
            if name != "" : 
                print("Введите отчество (у вас {max_attempts} попытки(ок)): ")
                patronymic = input_word(max_attempts)
            else : 
                patronymic = ""
            print ("Введите номер телефона: ")
            country_code = input_country_code()
            len_of_country_code = len(country_code)
            print(f"Country code is {country_code}")
            city_code = input_city_code()
            len_of_city_code = len(city_code)
            success = len(country_code) > 0 and len(city_code) > 0
            if success : 
                phone_number_length = phone_length_in_symbols - len(country_code) - len(city_code)-2
                phone_number = input_phone(phone_number_length)
                success = phone_number != ""
        attempt += 1
    if success : 
        last_id += 1
        new_contact = [str(last_id), surname,  name, patronymic, 
                       country_code + city_code + phone_number]
        all_data.append(new_contact)
        return 1
    else : 
        return 0

# Контакт - это список строк: "ID", "Фамилия", "Имя", "Отчество", "Телефон"
# Контакт с заданным идентификатором будет полностью изменен
def replace_contact (id) : 
    global all_data, last_id
    res = -1
    index = find_record_by_id (all_data, id)
    if index == -1 : 
        return res
    max_attempts = 3
    attempt = 1
    success = False
    while not success and attempt <= max_attempts : 
        change_surname = int(print("Меняем фамилию? 1 - Да, 0 - Нет => "))
        if change_surname : 
            print("Введите фамилию (у вас {max_attempts} попытки(ок)): ")
            surname = input_word(max_attempts)
        else : 
            surname = all_data[index][1]
        change_name = int(print("Меняем имя? 1 - Да, 0 - Нет => "))
        if change_name : 
            print("Введите имя (у вас {max_attempts} попытки(ок)): ")
            name = input_word(max_attempts)
        else : 
            name = all_data[index][2]
        success = surname != "" or name != ""
        if success : 
            if name != "" : 
                change_patronymic = int(print("Меняем отчество? 1 - Да, 0 - Нет => "))
                if change_patronymic : 
                    print("Введите отчество (у вас {max_attempts} попытки(ок)): ")
                    patronymic = input_word(max_attempts)
                else : 
                    patronymic = all_data[index][3]
            change_phone_number = int(print("Меняем номер телефона? 1 - Да, 0 - Нет => "))
            if change_phone_number :     
                print ("Введите номер телефона: ")
                country_code = input_country_code()
                len_of_country_code = len(country_code)
                print(f"Country code is {country_code}")
                city_code = input_city_code()
                len_of_city_code = len(city_code)
                print(f"City code is {country_code}")
                success = len(country_code) > 0 and len(city_code) > 0
                if success : 
                    phone_number_length = phone_length_in_symbols - len(country_code) - len(city_code)-2
                    phone_number = input_phone(phone_number_length)
                    success = phone_number != ""
        attempt += 1
    if success : 
        all_data[index] = [id, surname,  name, patronymic, 
                       country_code + city_code + phone_number]
    res = success
    return res

# Функция ищет в базе данных (список списков строк) все контакты, в которых содержится 
# некоторая подстрока (fragment), и возвращает список таких контактов

def find_records_by_fragment (data, fragment) : 
    found_records = []
    for i in range(len(data)) : 
        # print (f"i = {i}")
        result = False
        for j in range(1, len(data[i])) : 
            # print (f"Внутренний цикл для i = {i}")
            element = data[i][j].lower()
            # print(f"Проверяем {data[i][j]}")
            if fragment.lower() in element : 
                result = True
                break
        # print(result)
        if result : 
            found_records.append(data[i])
    return found_records

# Функция ищет в базе данных (список списков строк) контакт c идентификатором id 
# и возвращает -1, если такого контакта нет, и его индекс в списке, 
# если он найден

def find_record_by_id (data, id) : 
    res = -1
    for i in range(len(data)) : 
        # print (f"i = {i}")
        if data[i][0] == str(id) : 
            res = i
            break   
    return res

# Функция вносит изменения в поле контакта с идентификатором id
# Возвращает -1, если контакт с таким id не найден в базе данных
# 1 - если изменения были внесены, 
# 0 - если база данных осталась без изменений

def change_record (id) : 
    global all_data
    res = -1
    index = find_record_by_id (all_data, id)
    if index == -1 : 
        return res
    contact_to_show = [all_data[index]]
    print("Вот информация об этом контакте, "
          "хранящаяся в настоящее время в справочнике: \n")
    show_records (contact_to_show)
    user_choice = int(input("Какое поле Вы хотите изменить? \n"
          "     1 - Фамилия\n"
          "     2 - Имя\n"
          "     3 - Отчество\n"
          "     4 - Телефон\n"
          "     5 - Мне нужно поменять несколько полей\n"
          "     6 - Меня все устраивает\n"
          "Введите цифру Вашего выбора ===> "))
    
    print(f"Вы ввели цифру {user_choice}")
    if user_choice < 1 or user_choice > 5 : 
        res = 0
        return res
    
    max_attempts = 3
    confirmed = 0
    print(f"user_choice = {user_choice}")
    if user_choice in {1, 2, 3} : 
        print("Введите новое значение ===> ")
        meaning = input_word (max_attempts)
        if meaning == "" : 
            confirmed = int(input("То, что вы ввели, не является словом. \n"
                            "Меняем на пустую строку? (Да - 1, Нет - 0) => "))
        else : 
            confirmed = int(input(f"Вы хотите изменить текущее значение на {meaning}. \n"
                            "Меняем? (Да - 1, Нет - 0) => "))
        if confirmed : 
            all_data[index][user_choice] = meaning
            res = 1
        else : 
            res = 0
        return res
    elif user_choice == 4 : 
        new_phone_number = ""
        attempts = 1
        confirmed = 0
        while new_phone_number == "" and attempts <= max_attempts : 
            print ("Введите номер телефона: ")
            country_code = input_country_code()
            len_of_country_code = len(country_code)
            # print(f"Country code is {country_code}")
            city_code = input_city_code()
            len_of_city_code = len(city_code)
            # 
            if len(country_code) > 0 and len(city_code) > 0 : 
                phone_number_length = phone_length_in_symbols - len(country_code) - len(city_code)-2
                phone_number = input_phone(phone_number_length)
                new_phone_number = country_code + city_code + phone_number
            attempts += 1  
        if new_phone_number == "" : 
            confirmed = int(input("То, что вы ввели, не является номером телефона. \n"
                            "Меняем на пустую строку? (Да - 1, Нет - 0) => "))
        else : 
            confirmed = int(input(f"Вы хотите изменить номер телефона на {new_phone_number}. \n"
                            "Меняем? (Да - 1, Нет - 0) => "))
        if confirmed : 
            all_data[index][user_choice] = new_phone_number
            res = 1
        else : 
            res = 0
        return res
    elif user_choice == 5 :
        print("Введите новые данные контакта")
        res = replace_contact(id)
        return res
   

# Функция удаляет из базы контакт с идентификатором id
# Предполагается, что уже проверено, что такой контакт существует
def remove_contact(ind) : 
    global all_data, last_id
    removed = all_data.pop(ind)
    return removed

# Стартовая функция. 
# Запрашивает у пользователя имя файла, в котором находится справочник, 
# с которым он планирует работать, и запускает бесконечный цикл для 
# ввода пользователем команды, которую он желает выполнить. 
# Команда завершения работы - 7. 

def main_menu () : 
    global all_data, last_id, database
    if not launch_interaction() : 
        return
    # show_records (all_data)
    play = True
    while play : 
        answer = input("\nВведите команду: \n"
                       "1 - Показать все записи \n"
                       "2 - Добавить контакт \n"
                       "3 - Найти контакт(ы) по ключу \n"
                       "4 - Изменить контакт \n"
                       "5 - Удалить контакт \n"
                       "6 - Экспортировать/Импортировать данные в/из файла \n"
                       "7 - Завершить работу \n"
                       "====> ")
        match answer : 
            case "1" : 
                show_records(all_data)
            case "2" : 
                if add_new_contact() : 
                    print("В справочник добавлена запись: ")
                    for j in range(1,5) : 
                        print(all_data[len(all_data)-1][j], end = ' ')
                    print()
                else : 
                    print("В справочник не внесено никаких изменений. ")
                # press_enter_to_continue()
            case "3" : 
                fragment = input("Введите ключ для поиска контакта: ")
                list_of_found_contacts = find_records_by_fragment(all_data, fragment)
                if len(list_of_found_contacts) == 0 :
                    print(f"В справочнике отсутствуют контакты с ключом {fragment}.")
                else: 
                    if len(list_of_found_contacts) == 1 : 
                        print("Найден контакт:")
                    else: 
                        print("Найдено несколько контактов:")
                        print("Запомните ID контакта, если планируете дальнейшие действия с ним.")
                    show_records (list_of_found_contacts)
            case "4" : 
                ident = int(input("Если знаете идентификатор записи, введите его, "
                                   "если не знаете - 0 => "))
                if ident == 0 : 
                    print("Вернитесь к пункту меню 3, чтобы узнать ID интересующего Вас контакта")
                else :  
                    if find_record_by_id (all_data, ident) != -1 : 
                        if change_record(ident) : 
                            print("Изменения внесены в справочник")
                        else : 
                            print("В справочнике не было сделано никаких изменений. ")
                
                    
            case _ : 
                play = False
            # case "4": 
            #     pass
            # case "5": 
            #     pass
            # case "6": 
            #     pass
            # case "7": 
            #     play = False
            # case _ : 
            #     print("Try again!\n")
main_menu()