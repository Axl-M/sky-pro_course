# with open('zarazheniy_file.py', encoding='utf8') as file:
#     print(file.read())


virus_code = 'print("Я вирус")'
# print(virus_code)

with open('zarazheniy_file.py', 'a', encoding='utf8') as file:
    print(file.write(f'\n\n#=============\n{virus_code} \n'))