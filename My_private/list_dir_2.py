# записать в файл список директорий и файлов в этих директориях
# уровень вложенности 2
import os
 
root = '.'
dirs =[]

list_all = os.listdir()
# print(list_all)

with open('__files_list.txt', 'w', encoding='utf8') as fp:
    for name in list_all:
        if os.path.isfile(os.path.join(root, name)):
            # print(name)
            fp.write(name)
            fp.write('\n')
        else:       # если это папка
            dirs.append(name)

    # print(dirs)
    for dir in dirs:
        # print('\n', dir)
        # print('-' * 20)
        fp.write('\n')
        fp.write(dir)
        fp.write('\n')
        fp.write('-' * 20)
        fp.write('\n')
        for file in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, file)):
                # print(file)
                fp.write(file)
                fp.write('\n')
