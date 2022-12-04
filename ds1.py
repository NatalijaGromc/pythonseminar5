# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

file_words = []
new_file_words = []
with open('file_input1.txt','r',encoding='utf-8') as data:
    for line in data:
            file_words+=line.split(" ")
print(file_words)
for word in file_words:
    if "абв" not in word:
        new_file_words.append(word)
print(new_file_words)
with open('file_output1.txt', 'w',encoding='utf-8') as data:
    for word in new_file_words:
        data.write(word+' ')
