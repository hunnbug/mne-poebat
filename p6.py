def countWords(s):
    s = s.strip() # убираем пробелы сначала и с конца
    return len(s.split()) # возвращаем количество слов без пробелов

s = "Hello, World!"
print(countWords(s)) 

