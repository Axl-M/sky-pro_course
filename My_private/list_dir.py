# обойти текущую папку и записать назнания всех файлов в ней в файл
# а потом зайти в каждую подпапку и сделать то же самое дл нее
# глубина прохождения ограничена до 2-х
# пишем результат в файл

import os

level_depth = 0

with open('__files_list.txt', 'w', encoding='utf8') as fp:
    for root, dirs, files in os.walk('..'):
        """
        root:   имя текущей папки
                имя каждой подпапки
                ......
                для каждого прохода
        dirs:   [список подпапок в текущей папке]
                [папки в подпапке]
                .......
        files:  [файлы в текущей папке]
                [ф - лы в подпапке]
                ....
        
        """
        # print(dirs)
        # print(root, dirs, files)
        # print('\n', root)
        # for filename in files:
        #     print(filename)

# ограничиваем вложенность 2-мя уровнями (только ф-лы в подпапках текущей папки)
#         level_depth += 1
#
#         if level_depth > 7:
#             break

        # print('\n', root)
        # ПИШЕМ В ФАЙЛ


        fp.write('\n')
        fp.write(root)
        fp.write('\n')
        for file in os.listdir(root):
            if os.path.isfile(os.path.join(root, file)):
                # print(file)
                fp.write(file)
                fp.write('\n')
