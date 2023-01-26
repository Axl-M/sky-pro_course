# считает количество букв (знаки препинани и пробелы исключаются)
# считает колличество слов ( = кол-во пробелов + 1)

string = "Я графоман, спасите!"

word_count = 0
letter_count = 0
space_count = 0

for letter in string:
    if letter not in list(',./?!@#$%^&*()_+=-;:[]{}~ '):
        letter_count += 1
    # elif letter == ' ':
    #     space_count += 1

space_count = string.count(' ')

word_count = space_count + 1

print(f'Букв - {letter_count}')
print(f'Слов - {word_count}')
