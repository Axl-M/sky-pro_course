
virus_code = "Я вирус"

with open('zarazheniy_file.py', encoding='utf8') as file:
    content = file.read()
    if virus_code in content:
        print("Файл заражен, обнаружен вирус")
    else:
        print("Вирус не обнаружен")


