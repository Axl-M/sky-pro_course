# запускать в консоли !!! (RUN в PyCharm не работает)

from time import sleep

# import colorama
# from colorama import Fore, Back, Style
# colorama.init()
# print(Fore.RED + 'Красный текст')
# print(Back.BLUE + 'Синий фон')
# print(Style.RESET_ALL)

for i in range(0, 101, 1):
    eq = '=' * i
    spaces = ' ' * (100 - len(eq))
    print(f' [ {eq} > {spaces} {i}%]', end='\r')
    sleep(0.3)


