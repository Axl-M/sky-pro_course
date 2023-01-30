# игра составить слова из заданных букв (в другом слове)

# json также сохранен на внешнем источнике по адресу
# https://jsonkeeper.com/b/6VBM
# реализовать запрос оттуда

# импорт встроенных пакетов, затем импортированных и последими пользовательские

from utils import load_random_word
from classes.player import Player

def main():
    main_word = load_random_word()  # получить экземпляр класса со случайным словарем

    word = main_word.word                   # слово из которого составить
    wordcount = main_word.count_subwords()  # Сколько слов можно составить

    user_name = input("Введите ваше имя\n")
    print(f"Приветствую тебя, {user_name}!")
    player = Player(user_name)
    # print(player)
    print(f"Составьте {wordcount} слов из слова {word}")
    print("Слова должны быть не короче 3-х букв")
    print("Чтобы закончить игру, угадайте все слова или напишите слово 'стоп' или 'stop'")
    print("Поехали, начинаем игру\n")

    # пока кол-во угаданных слов не равно к-ву которое можно угадать
    while len(player.used_words) < wordcount:
        # в каждой итерации получить слово
        user_input = input(f"Можете составить слово из слова '{word}'? Слов осталось - {wordcount - len(player.used_words)}\n")

        # если введено stop или стоп
        # завершить игру
        if user_input.lower() == 'stop' or user_input.lower() == 'стоп':
            break

        # если слово короче 3-х букв
        if len(user_input) < 3:
            print("слишком короткое слово")
            continue

        # если слово уже было угадано пользователем Player
        if user_input in player.used_words:
            print("Вы уже угадали это слово")
            print(f'Угаданные слова: {player.used_words}')
            continue

        # если слово в списке допустимых
        if user_input in main_word.sub_words:
            print("Да, такое слово есть")
            player.add_word(user_input)
        else:
            print("Я не знаю такого слова")
            continue

    # вывести к-во угаданных слов из экземплра класса Player
    print(f'Игра завершена, вы угадали {player.count_words()} слов!')
    print(f'Вы не смогли угадать: ', end=' ')
    for i in set(main_word.sub_words) - set(player.used_words):
        print(i, end=', ')



if __name__ == '__main__':
    main()