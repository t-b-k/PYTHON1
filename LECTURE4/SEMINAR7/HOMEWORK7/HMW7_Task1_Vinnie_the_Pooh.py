# Задача 34. 
# Винни-Пух считает, что ритм в стихотворении есть, если число 
# слогов (то есть, количество гласных букв) во всех фразах одинаково. 
# Фраза может состоять из одного слова. Если во фразе несколько слов, 
# то они отделяются друг от друга дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите "Парам пам-пам", если с ритмом все в порядке, 
# и "Пам парам", если ритм "хромает". 

# Алгоритм: 
# 1. Считываем строку-стихотворение. 
# 2. Сплитом разбиваем ее на фразы. Получаем список фраз. 
# 3. Пишем функцию, которая в переданной ей на вход строке-фразе а
#    подсчитывает количество гласных букв и его же и возвращает.
# 4. Эту функцию применяем в методе map ко всем элементам нашего списка.  
# 5. Преобразуем полученный в результате список во множество. 
# 6. Если его мощность равна единице - ответ "Парам пам-пам". Если больше - "Пам парам". 

# test_string = "мА-Ма мЫ-ла ? р№А-му 56-о-кон The truth"

rus_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
winnie_signs = "- "
vowels = "аеёиоуыэюя"

def can_be_poem (test_str) : 
    res = True
    work_str = test_str.strip().rstrip().lower()
    for i in range(len(work_str)) : 
        if not (work_str[i] in rus_letters + winnie_signs) : 
            res = False
            break
    return res

def syllable_qty (phrase) :
    qty = 0
    for i in phrase : 
        if i in vowels : 
            qty += 1
    return qty

if_poem = input("Введите стихи. \nПроверим, все ли в них в порядке с рифмой с т.зр. Винни\n\n => ")

# if_poem = "Пара-ра-рам рам-пам-папам па-ра-па-да"
# if_poem = "Пм-ао пдлов рампамдо коллаборационист не-страшно а я бо-юсь"
# if_poem = "dfkljwe dklfs-ewSD;LKFJ двла вд"
# if_poem = "Мама мы-ла рам-у"
# if_poem = "мА-Ма мЫ-ла ? р№А-му 56-о-кон The truth"
# if_poem = "пп пап пп папапап п"
# if_poem = "пп пп пп пппп п"
# if_poem = "ае о уы иии ё"

if can_be_poem (if_poem) : 
    nums_of_vowels = set(map(syllable_qty, if_poem.split()))
    if len(nums_of_vowels) == 1 and nums_of_vowels != {0} :
            print ("\nРЕЗУЛЬТАТ: Парам пам-пам")
    elif 0 in nums_of_vowels: 
        print ("\nРЕЗУЛЬТАТ: Пам парам... В каждой фразе должна быть хоть одна гласная..., ")
        print("\t   иначе что это за стихи?...")
    else : 
        print ("\nРЕЗУЛЬТАТ: Пам парам")
else: 
    print("Пам парам... Ваши стихи не являются стихами с точки зрения поэзии Винни-Пуха.")

# Разобрано на семинаре. 

# alp = "аеёиоуыэюя"
# word_sug = input().split()
# vowel_letters = [word.count(char) for word in word_sug 
#                  for char in word if char.lower() in alp]

# vowel_letters = []
# for word in word_sug : 
#       for char in word.lower() :
#           if char in alp : 
#               vowel_letters.append(char)
#  
# if len(set(vowel_letters)) == 1 : 
#     print("Парам пам-пам")
# else : 
#     print("Пам парам")
