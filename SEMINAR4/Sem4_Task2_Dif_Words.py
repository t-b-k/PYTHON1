# Задача № 27. 
# Пользователь вводит текст (строка). 
# Словом считается последовательность непробельных символов, идущих подряд. 
# Слова разделены одним или бОльшим числом пробелов. 
# Определите, сколько РАЗЛИЧНЫХ слов находится в этом тексте. 

# Пример ввода: She sells sea shells on the sea shore The shells that she 
# sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure
# that the shells are sea shore shells

# Результат: 13

# РЕШЕНИЕ: 

words = set(input().lower().split())
print(f"Количество разных слов в вашем тексте = {len(words)}")