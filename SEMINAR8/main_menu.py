import os
from tabulate import tabulate

database = 'raw_base.txt'
all_data = []
last_id = 0

def file_exists_and_not_empty (file_name) : 
    global database
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

# Возвращает 1, если все готово к взаимодействию, 0 - если нет
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
        
def main_menu () : 
    global all_data, last_id, database
    if not launch_interaction() : 
        return
    show_records (all_data)
    play = True
    while play : 
        answer = input("Введите команду: \n"
                       "1 - Показать все записи \n"
                       "2 - Добавить контакт \n"
                       "3 - Найти контакт(ы) по ключу \n"
                       "4 - Изменить контакт \n"
                       "5 - Удалить контакт \n"
                       "6 - Экспортировать/Импортировать данные в/из файла \n"
                       "7 - Завершить работу \n")
# Надо добавить Change, Import, Export
# Export - это выгрузка текущей базы в другой файл: Введите название
# будущей базы, пришиваем .txt, проверяем на существование, отдаем в бета-функцию
# import - это изменение переменной file_base на новое имя, которое
# предоставит пользователь. 
        if answer == "1" : 
                print(f"Вы выбрали пункт меню {answer}")
                show_records(all_data)
                play = False
        else : 
            play = False
            # case "2": 
            #     if add_new_contact() : 
            #         print("В справочник добавлена запись: ")
            #         for j in range(1,5) : 
            #             print(all_data[len(all_data)-1][j], end = ' ')
            #     else : 
            #         print("В справочние не внесено никаких изменений. ")
            # case "3": 
            #     fragment = input("Введите строку для поиска: ")
            #     list_of_found_contacts = find_records_by_fragment(all_data,fragment)
            #     if len(list_of_found_contacts) == 0 :
            #         print(f"Искомых контактов нет в справочнике.")
            #     else: 
            #         if len(list_of_found_contacts) == 1 : 
            #             print("Найден контакт:")
            #         else: 
            #             print("Найдено несколько контактов:")
            #             print("Запомните ID контакта, если планируете дальнейшие действия с ним.")
            #         show_records (list_of_found_contacts)
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