import os
from tabulate import tabulate

all_data = []   # Данные хранятся во время работы в списке списков строк
                # Один контакт - один элемент all_data: список строк-полей
last_id = 0     # Идентификатор последней добавленной в справочник записи
                # Идентификатор != индексу списка в структуре all_data
database = 'raw_base.txt'   # Файл, в котором хранятся данные тел. справочника 
                            # Используется по умолчанию
phone_length_in_symbols = 18    # Количество символов, отведенное на телефонный номер
                                # с учетом служебных символов для красивого отображения
                                # номера : "+", "(", ")", "-"
country_code_in_symbols = 4     # Количество символов для отображения кода страны: +007

# Функция проверяет файл с именем file_name на существование и пустоту
#   -1 - такого файла нет
#    0 - файл существует, но он пустой
#    1 - файл существует и не пуст

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

# Функция записи данных из справочника в файл. 
# Про файл txt_file_name уже известно, что он существует и не пуст
def read_records_from_txt (txt_file_name) : 
    global last_id, all_data
    with open (txt_file_name, "r", encoding="utf-8") as f: 
        for next_line in f : 
            last_id += 1
            all_data.append([str(last_id), *next_line.strip().split()])

# Функция добавления данных из справочника в файл. 
# Про файл txt_file_name уже известно, что он существует и не пуст
def add_records_to_txt (txt_file_name) :
    global all_data
    with open (txt_file_name, "a", encoding="utf-8") as f :
        f.write("")
        for i in all_data : 
            f.writelines(" ".join(i[1:])+"\n")

# Функция считывания данных из заданного файла во внутреннюю структуру 
# данных all_data, предназначенную для работы с данными в процессе одного сеанса
# Про файл txt_file_name уже известно, что он существует и не пуст
def write_records_to_txt (txt_file_name) :
    global all_data
    with open (txt_file_name, "w", encoding="utf-8") as f : 
        for i in all_data : 
            f.writelines(" ".join(i[1:])+"\n")

# Функция отображает в консоли текущее содержимое базы данных. 
# Оно не совпадает с состоянием исходного файла, так как 
# данные туда сливаются по окончании сеанса работы со справочником. 
def show_records (data) : 
    columns = ["ID", "Фамилия", "Имя", "Отчество", "Номер телефона"]
    print(tabulate(data, headers=columns))
    print()

# Функция, подготавливающая структуру all_data к сеансу работы. 
# Запрашивает у пользователя имя файла-справочника, с которым 
# он собирается работать, и сообщает, какой справочник используется по умолчанию. 
# Функция возвращает:
#       1, если все готово к взаимодействию со справочником, 
#       0 - если обнаружены проблемы

def launch_interaction () :
    global database, all_data, last_id
    print(f"По умолчанию используется справочник {database}")
    print("Если Вы хотите использовать этот справочник, введите   - 1 ")
    print("Если Вы хотите работать с другим справочником, введите - 0 ")
    user_choice = int(input(" ===> "))

    if (user_choice == 0) : 
        print("Введите имя файла, с которым хотите работать.")
        print("Если такого файла не существует, будет создан пустой справочник. ")
        file_to_use = input("С каким файлом .txt Вы хотите работать? ===> ")
        if file_to_use[-4:].lower() != ".txt" : 
            print("Извините. Справочник может находиться только в файле .txt")
            print("Программа завершает работу.\n")
            return 0
        else :
            database = file_to_use
            answer =  file_exists_and_not_empty(database)
            if answer == 1 :
                print("Такой справочник существует. Будем работать с ним. \n") 
                read_records_from_txt(database)
            elif answer == 0 : 
                print("Справочник пуст. Его сначала придется наполнить.\n")
            else : 
                print(f"Файла с именем {database} не существует. Будет создан новый файл с таким именем.\n")    
                with open (database, "w", encoding="utf-8") as _ : 
                    pass
            return 1
    elif  user_choice == 1 : # Работаем с файлом, который используется по умолчанию
        print(f"Работаем с файлом {database}") 
        read_records_from_txt(database)
        return 1
    else : 
        print(f"Вы ввели недопустимое значение") 
        print(f"Программа завершает свою работу")
        return 0

# Функция принимает из консоли целое положительное число. 
# Если введено что надо, возвращает это число.
# Иначе возвращает 0. На ввод дается 3 попытки. 
def input_positive_integer (max_attempts) : 
    # max_attempts = 3
    for i in range(max_attempts) : 
        id = input(f"{i+1}-я попытка =>  ")
        if id != "" and id.isdigit() and int(id) > 0: 
            return int(id)
    return 0

# Функция принимает из консоли строку букв и возвращает ее же, 
# преобразованную в Title. 
# Если пользователь не справился с вводом, возвращает пустую строку

def input_word (max_attempts) : 
    # max_attempts = 3
    for i in range(max_attempts) : 
        word = input(f"{i+1}-я попытка ===> ")
        if word != "" and word.isalpha() : 
            return word.title()
    return ""

# Функция возвращает строку в формате кода страны для записи в справочник:
# +DDD, где D - цифра.  
# Пользователь вводит только цифры. Ему дается три попытки
# Если он не справился с вводом, функция возвращает пустую строку

def input_country_code (max_attempts) : 
    # max_attempts = 3
    print("Введите код страны. У вас {max_attempts} попыток(ка/ки). ")
    print("Код страны содержит не более 3-х цифр. "
          "По умолчанию используется код России - +007")
    res = "" 
    for i in range(max_attempts) :   
        code = input(f"{i+1}-я попытка ===> +")
        if code == "" : 
            res = "+007"
            return res
        elif code.isdigit() and int(code) != 0 and len(code) in range(1,4): 
            if len(code) == 1 : 
                res += "+00" + code
                return res 
            elif len(code) == 2 : 
                res += "+0" + code
                return res
            elif len(code) == 3 : 
                res += "+" + code
                return res
        else : 
            print("Вы ввели некорректный код страны\n")
            return res    
 
# Функция возвращает строку с кодом города, заключенным в круглые скобки. 
# Если пользователь не справился с вводом, возвращает пустую строку
# Код города должен содержать от 3-х до 5-ти цифр
def input_city_code (max_attempts) : 
    # max_attempts = 3
    print(f"Введите код города(оператора) - от 3-х до 5-ти цифр. У вас {max_attempts} попытки). ")
    res = "" 
    for i in range(max_attempts) :   
        code = input(f"{i+1}-я попытка ===> ")
        if code.isdigit() and len(code) in range(3,6) and int(code) > 0 : 
            res = "(" + code + ")"
            print(f"Код города - {res}")
            break
        else : 
            print("Вы ввели некорректный код города\n")
    return res  

# Функция возвращает строку с номером телефона внутри населенного пункта. 
# Если пользователь не справился с вводом, возвращает пустую строку
# Номер телефона может содержать от 5 до 8-ми цифр
def input_phone (phone_length, max_attempts) : 
    # max_attempts = 3
    print(f"Введите номер телефона (у вас {max_attempts} попытки). ")
    print(f"Номер телефона должен содержать {phone_length} цифр, "
          "и он не может состоять из одних нулей. \n")
    res = "" 
    for i in range(max_attempts) :   
        phone = input(f"{i+1}-я попытка ===> ")
        length = len(phone)
        if length == phone_length and phone.isdigit() and int(phone) != 0 : 
            res = phone[:length-4] + "-" + phone[length-4:length-2] + "-" + phone[length-2:]
            break
        else : 
            print("Вы ввели некорректный номер телефона\n")
            return res  
#    print(f"Номер телефона внутри города: {res} ")
    return res   

# Функция add_new_contact добавляет контакт в базу данных
# Контакт - это список строк в определенной последовательности: 
# "ID", "Фамилия", "Имя", "Отчество", "Телефон"
# Если пользователю удается корректно ввести данные, контакт будет создан, 
# и функция вернет 1
# Если ввод не удастся - вернет 0

def add_new_contact () : 
    global all_data, last_id
    new_contact = [] # пустой список. Будет превращаться в список строковых значений
    max_attempts = 3

    print(f"Введите фамилию (у вас {max_attempts} попытки) ===> ")
    surname = input_word(max_attempts)
    if (surname == "") : 
        print("Введенная последовательность символов не может быть фамилией. \n"
              "Поле 'Фамилия' останется пустым. \n")
    print(f"Введите имя (у вас {max_attempts} попытки) ===> ")
    name = input_word(max_attempts)
    if name == "" :
        print("Введенная последовательность символов не может быть именем. \n"
              "Поле 'Имя' останется пустым. \n")
        if surname == "" : 
            print("Контакт без имени и фамилии не может быть добавлен в справочник \n")
            return False
        patronymic = ""
    else : 
        print(f"Введите отчество (у вас {max_attempts} попытки) ===> ")
        patronymic = input_word(max_attempts)
        if patronymic == "" :
            print("Введенная последовательность символов не может быть отчеством. \n"
              "Поле 'Отчество' останется пустым. \n")
        
    print ("Введите номер телефона ===> ")
    country_code = input_country_code(max_attempts)
    # print(f"Country code is {country_code}")   
    if country_code == "" : 
        print("Вы ввели некорректные данные. \n")
        return False
    city_code = input_city_code(max_attempts)
    print(city_code)
    if city_code == "" : 
        print("Вы ввели некорректные данные. \n")
        return False
    phone_number_length = phone_length_in_symbols - len(country_code) - len(city_code)-2
    phone_number = input_phone(phone_number_length, max_attempts)
    if phone_number == "" :
        print("Вы ввели некорректные данные. \n")
        return False
    
    last_id += 1
    new_contact = [str(last_id), surname,  name, patronymic, 
                       country_code + city_code + phone_number]
    all_data.append(new_contact)
    return 1

# Контакт - это список строк: "ID", "Фамилия", "Имя", "Отчество", "Телефон"
# Контакт с заданным идентификатором будет полностью изменен
# Функция возвращает: 
#   -1  -   если контакт с таким идентификатором отсутствует в базе
#    1  -   если пользователь успешно ввел все необходимые данные, 
#           и контакт был изменен
#    0  -   если пользователь предоставил некорректные данные. 
#           В этом случае запись о контакт остается без изменений. 

def replace_contact (id) : 
    global all_data, last_id
    index = find_record_by_id (id)
    if index == -1 : 
        return index
    res = 0
    max_attempts = 3
    change_surname = int(input("Меняем фамилию? 1 - Да, 0 - Нет ===> "))
    if change_surname : 
        print(f"Введите фамилию (у вас {max_attempts} попытки) ===> ")
        surname = input_word(max_attempts)
        if (surname == "") : 
            print("Введенная последовательность символов не может быть фамилией. \n"
                  "Поле 'Фамилия' останется без изменений. \n")
        else : 
            all_data[index][1] = surname
            res = 1
    change_name = int(input("Меняем имя? 1 - Да, 0 - Нет ===> "))
    if change_name : 
        print(f"Введите имя (у вас {max_attempts} попытки) ===> ")
        name = input_word(max_attempts)
        if (name == "") : 
            print("Введенная последовательность символов не может быть именем. \n"
                  "Поле 'Имя' останется без изменений. \n")
        else : 
            all_data[index][2] = name    
            res = 1       
    change_patronymic = int(input("Меняем отчество? 1 - Да, 0 - Нет ===> "))
    if change_patronymic : 
        print(f"Введите отчество (у вас {max_attempts} попытки) ===> ")
        patronymic = input_word(max_attempts)
        if (patronymic == "") : 
            print("Введенная последовательность символов не может быть отчеством. \n"
                  "Поле 'Отчество' останется без изменений. \n")
        else : 
            all_data[index][3] = patronymic
            res = 1
    change_phone_number = int(input("Меняем номер телефона? 1 - Да, 0 - Нет ===> "))
    if change_phone_number :     
        print ("Введите номер телефона ===> ")
        country_code = input_country_code(max_attempts)
        # print(f"Country code is {country_code}")   
        if country_code == "" : 
            print("Поле 'Номер телефона' останется без изменений.\n")
        else : 
            city_code = input_city_code(max_attempts)
            if city_code == "" : 
                print("Поле 'Номер телефона' останется без изменений.\n")
            else : 
                phone_number_length = phone_length_in_symbols - len(country_code) - len(city_code)-2
                phone_number = input_phone(phone_number_length, max_attempts)
                if phone_number == "" :
                    print("Поле 'Номер телефона' останется без изменений.\n")
                else : 
                    all_data[index][4] = country_code + city_code + phone_number
                    res = 1
    return res

# Функция ищет в базе данных (список списков строк) контакты, в которых содержится 
# заданная подстрока (fragment), и возвращает список всех таких контактов в формате all_data

def find_records_by_fragment (fragment) : 
    global all_data
    found_records = []
    for i in range(len(all_data)) : 
        result = False
        for j in range(1, len(all_data[i])) : 
            element = all_data[i][j].lower()
            if fragment.lower() in element : 
                result = True
                break
        # print(result)
        if result : 
            found_records.append(all_data[i])
    return found_records

# Функция ищет в базе данных (список списков строк) контакт c идентификатором id
# (целое число) 
# и возвращает -1, если такого контакта нет, и его индекс в списке, 
# если он найден

def find_record_by_id (id) : 
    global all_data, last_id
    if id > last_id : 
        res = -1
    else : 
        for i in range(len(all_data)) : 
            if all_data[i][0] == str(id) : 
                res = i
                break   
    return res

# Функция вносит изменения в одно поле контакта с идентификатором id
# Возвращает:
# -1, если контакт с таким id не найден в базе данных
#  1 - если изменения были внесены, 
#  0 - если база данных осталась без изменений

def change_record (id) : 
    global all_data
    index = find_record_by_id (id)
    if index == -1 : 
        return res
    res = 0
    contact_to_show = [all_data[index]]
    print("Вот информация об этом контакте, "
          "хранящаяся в настоящее время в справочнике: \n")
    show_records (contact_to_show)
    user_choice = int(input("Какое именно поле Вы хотите изменить? \n"
          "     1 - Фамилия\n"
          "     2 - Имя\n"
          "     3 - Отчество\n"
          "     4 - Телефон\n"
          "     5 - Мне нужно поменять несколько полей\n"
          "     6 - Меня все устраивает\n"
          "Введите цифру Вашего выбора ===> "))
    if user_choice < 1 or user_choice > 5 : 
        res = 0
        return res   
    max_attempts = 3
    confirmed = 0
    if user_choice in {1, 2, 3} : 
        print("Введите новое значение ===> ")
        meaning = input_word(max_attempts)
        if meaning == "" : 
            confirmed = int(input("То, что вы ввели, не является словом. "
                            "Меняем на пустую строку? (Да - 1, Нет - 0) ===> "))
        else : 
            confirmed = int(input(f"Вы хотите изменить текущее значение на {meaning}. "
                            "Меняем? (Да - 1, Нет - 0) ===> "))
        if confirmed : 
            all_data[index][user_choice] = meaning
            res = 1
        return res
    elif user_choice == 4 : 
        new_phone_number = ""
        confirmed = 0
        print ("Введите номер телефона ===> ")
        country_code = input_country_code(max_attempts)
        city_code = input_city_code(max_attempts)
        if len(country_code) > 0 and len(city_code) > 0 : 
            phone_number_length = phone_length_in_symbols - len(country_code) - len(city_code)-2
            phone_number = input_phone(phone_number_length, max_attempts)
            new_phone_number = country_code + city_code + phone_number
        if new_phone_number == "" : 
            print("То, что вы ввели, не является корректным номером телефона. "
                  "Номер телефона останется без изменений ===> ")
        else : 
            if int(input(f"Вы хотите изменить номер телефона на {new_phone_number}. "
                            "Меняем? (Да - 1, Нет - 0) ===> ")) : 
                all_data[index][user_choice] = new_phone_number
                res = 1
        return res
    elif user_choice == 5 :
        print("Тогда будете вводить все данные контакта")
        res = replace_contact(id)
        return res
   

# Функция удаляет из базы контакт с индексом ind
# Предполагается, что такой контакт точно существует

def remove_contact(ind) : 
    global all_data, last_id
    removed = all_data.pop(ind)
    return removed

# Главный метод программы. 
# Запрашивает у пользователя имя файла, в котором находится справочник, 
# с которым он планирует работать, и запускает бесконечный цикл для 
# ввода пользователем команды, которую он желает выполнить. 
# Команда завершения работы - 7. 

def main_menu () : 
    global all_data, last_id, database
    if not launch_interaction() : 
        return
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
                       "===> ")
        match answer : 
            case "1" : 
                show_records(all_data)
            case "2" : 
                if add_new_contact() : 
                    print("В справочник добавлена запись: \n")
                    contact_to_show = [all_data[len(all_data)-1]]
                    show_records(contact_to_show)
                    print()
                else : 
                    print("В справочник не внесено никаких изменений. \n")
            case "3" : 
                fragment = input("Введите ключ для поиска контакта ===> ")
                list_of_found_contacts = find_records_by_fragment(fragment)
                if len(list_of_found_contacts) == 0 :
                    print(f"В справочнике отсутствуют контакты с ключом {fragment}.\n")
                else: 
                    if len(list_of_found_contacts) == 1 : 
                        print("Найден один контакт:")
                    else: 
                        print("Найдено несколько контактов.")
                        print("Запомните ID контакта, если планируете дальнейшие действия с ним.")
                    show_records (list_of_found_contacts)
            case "4" : 
                ident = int(input("Если знаете идентификатор записи, введите его, "
                                   "если не знаете - 0 ===> "))
                if ident == 0 : 
                    print("Вернитесь к пунктам меню 1 или 3, чтобы узнать ID интересующего Вас контакта\n")
                else :  
                    if find_record_by_id (ident) != -1 : 
                        if change_record(ident) : 
                            print("Изменения внесены в справочник! \n")
                        else : 
                            print("В справочнике не было сделано никаких изменений. \n")
            case "5" : 
                print("По какому признаку Вы хотите выбрать контакт для удаления? ")
                user_choice = int(input("   1 - по идентификатору,\n"
                                        "   2 - по текстовому ключу\n"
                                        " ===> "))
                if user_choice == 1 : 
                    id = int(input("Введите идентификатор ===> "))
                    index = find_record_by_id (id)
                    if index != -1 : 
                        deleted_contact = [remove_contact(index)]
                        print(f"Контакт: ")
                        show_records(deleted_contact)
                        print("удален из справочника. ")
                    else: 
                        print(f"Контакт c ID = {id} отсутствует в справочнике. \n")
                else: 
                    fragment = input("Введите текст для поиска контакта ===> ")
                    found_contacts = find_records_by_fragment (fragment)
                    if len(found_contacts) == 1 : 
                        print("Найден один контакт: ")
                        show_records (found_contacts)
                        index = find_record_by_id (int(found_contacts[0][0]))
                    else: 
                        print("Найдено несколько контактов:")
                        show_records (found_contacts)
                        id = int(input("Введите ID контакта, который нужно удалить ===> "))
                        index = find_record_by_id (id)
                    confirmed = int(input("Удаляем контакт? 1 - Да, 0 - Нет ===> "))
                    if confirmed: 
                        deleted_contact = [remove_contact(index)]
                        print(f"Контакт: ")
                        show_records(deleted_contact)
                        print("удален из справочника. ")
                    
            case "6" : 
                # Сохраняем наши данные в исходный справочник
                write_records_to_txt (database)
                user_choice = int(input("Введите 0 для экспорта, 1 - для импорта ===> "))
                if user_choice not in {0,1} : 
                    print("Ошибка ввода! \n")
                elif user_choice == 0 : 
                    file_name = input("Введите имя файла (с расширением .txt) ===> ")
                    if file_name[-4:].lower() != ".txt" : 
                        print("Справочник может находиться только в файле .txt"
                              "Операция экспорта не может быть выполнена.\n")
                    else :
                        check_point =  file_exists_and_not_empty(file_name)
                        if check_point == 1 :
                            to_do = int(input(f"Файл {file_name} не пуст. Информация будет потеряна.\n"
                                  "Перезаписываем в него справочник или добавляем записи?\n"
                                  " 1 - Перезаписываем, 2 - Добавляем, 0 - Отмена экспорта ===>"))
                            if to_do == 1 : 
                                write_records_to_txt(file_name)
                                print(f"Справочник записан в файл{file_name}\n")
                            elif to_do == 2 : 
                                add_records_to_txt(file_name)
                                print(f"Справочник добавлен в файл{file_name}\n")
                            else : 
                                print("Операция экспорта не выполнена!\n")  
                        else : 
                            if check_point == -1 : 
                                print(f"Создан новый файл {file_name}. Выполняем операцию экспорта...\n") 
                            else : #check_point == 0 : 
                                print(f"Файл {file_name} существует и пуст. Выполняем операцию экспорта...\n")
                            write_records_to_txt (file_name)

                else :  # пользователь хочет имортировать данные из некоторого файла                  
                    file_name = input("Введите имя файла (с расширением .txt) для импорта данных ===> ")
                    if file_name[-4:].lower() != ".txt" : 
                        print("Справочник может находиться только в файле .txt"
                              "Операция прервана.\n")
                    else :
                    # Считываем в all_data данные из указанного пользователем файла,
                    # присваиваем записям идентификаторы и обновляем last_id
                        print(f"С этого момента мы работаем со справочником из файла {file_name}\n")
                        database = file_name
                        all_data.clear()
                        last_id = 0
                        read_records_from_txt (database)
            case _ : 
                # Сохраняем наши наработки в текущий справочник и завершаем работу
                write_records_to_txt (database)
                play = False

main_menu()