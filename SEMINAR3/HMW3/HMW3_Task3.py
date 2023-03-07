# Задача 20. 
# В настольной игре Scrabble каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так: 

# A, E, I, O, U, L, N, S, T, R - 1 очко
# D, G - 2 очка
# B, C, M, P - 3 очка
# F, H, V, W, Y - 4 очка
# K - 5 очков
# J, X - 8 очков
# Q, Z - 10 очков

# А русские буквы оцениваются так: 

# А, В, Е, И, Н, О, Р, С, Т - 1 очко
# Д, К, Л, М, П, У - 2 очка
# Б, Г, Ё, Ь, Я - 3 очка
# Й, Ы - 4 очка
# Ж, З, Х, Ч, Ц - 5 очков
# Ш, Э, Ю - 8 очков
# Ф, Щ, Ъ - 10 очков

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается ровно одно слово, которое содержит 
# только английские или только русские буквы

# РЕШЕНИЕ: 
# Введенное пользователем слово - это строка. Сделаем все буквы большими - upper(). 
# Создадим словари: русский и английский, в которых ключом буду являться строки 
# символов соответствующего алфавита, имеющих одинаковый вес, а значением - сам их вес. 
# Сначала по первому символу введенного слова определим язык. 
# Затем пройдемся по нашему слову и для каждого встреченного символа прибавим 
# к результату его вес, найденный в соответствующем словаре

# I вариант: 

word = input("Введите слово для анализа его стоимости => ").upper()
print(word)

dict_rus = {"АВЕИНОРСТ": 1, "ДКЛМПУ": 2, "БГЁЬЯ": 3, "ЙЫ": 4, "ЖЗХЦЧ": 5, "ШЭЮ": 8, "ФЩЪ": 10}
dict_eng = {"AEIOULNSTR": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}

# Для каждого символа во веденной пользователем строке прибавим к результату 
# его вес, найденный по ключу в соответствующем словаре

language = "Русский"
for item in dict_eng : 
    if word[0] in item : 
        language = "Английский"
        break

print(f"Ваш язык - {language}")

weight_of_word = 0
if language == "Русский" : 
    for symbol in word : 
        for item in dict_rus : 
            if symbol in item : 
                weight_of_word += dict_rus[item]
else : 
    for symbol in word : 
        for item in dict_eng : 
            if symbol in item : 
                weight_of_word += dict_eng[item]
    
print(f"Вес введенного Вами слова равен {weight_of_word}")

# II вариант: с использованием comprehensions (сокращенная форма for)

word = input("Введите слово для анализа его стоимости => ").upper()
print(word)

dict_rus = {"АВЕИНОРСТ": 1, "ДКЛМПУ": 2, "БГЁЬЯ": 3, "ЙЫ": 4, "ЖЗХЦЧ": 5, "ШЭЮ": 8, "ФЩЪ": 10}
dict_eng = {"AEIOULNSTR": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}

language = "Русский"
for item in dict_eng : 
    if word[0] in item : 
        language = "Английский"
        break

print(f"Ваш язык - {language}")
if language == "Русский" : 
    weight_of_word = sum([item[1] for item in dict_rus.items() for symbol 
                          in word if symbol in item[0]])
    # for symbol in word : 
    #     for item in dict_rus : 
    #         if symbol in item : 
    #             weight_of_word += dict_rus[item]
else : 
    weight_of_word = sum([item[1] for item in dict_eng.items() for symbol 
                          in word if symbol in item[0]])
    # for symbol in word : 
    #     for item in dict_eng : 
    #         if symbol in item : 
    #             weight_of_word += dict_eng[item]

print(f"Вес введенного Вами слова равен {weight_of_word}")

