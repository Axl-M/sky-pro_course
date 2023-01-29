# json также сохранен на внешнем источнике по адресу
# https://jsonkeeper.com/b/6VBM
# реализовать запрос оттуда
#
from utils import load_random_word

def main():
    main_word = load_random_word() # () нужны?

    # user_name = input("Введите ваше имя"\n)
    # print(f"Приветствую тебя, {user_name}!")
    # print(f"Составьте {к-во} слов из слова {}")
    # print("Слова должны быть не короче 3-х букв")
    # print("Чтобы закончить игру, угадайте все слова или напишите слово 'stop'")
    user_input = input("Поехали, ваше первое слово?\n")

    if main_word.has_subword(user_input):
        print("Слово есть")
    else:
        print("Слова нет")




if __name__ == '__main__':
    main()