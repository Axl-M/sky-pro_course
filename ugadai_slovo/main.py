# import random
from utils import get_random_words, shuffle_word, save_score, get_statistic
from settings import WORDS_FILE, SCORES_FILE


def main():

    # rnd_word = random.choice(get_random_words())
    # print(shuffle_word(rnd_word))
    score = 0
    user_name = input("Введите ваше имя: ")
    words = get_random_words(WORDS_FILE)

    for word in words:
        word_shuffled = shuffle_word(word)
        user_input = input(f'\nУгадай слово: {word_shuffled} \n===>')
        if user_input == word:
            print('Верно! Вы получаете 10 очков.')
            score += 10
        else:
            print(f'Неверно. Правильный ответ - {word}')

    save_score(SCORES_FILE, user_name, score)
    stats = get_statistic(SCORES_FILE)
    print(f'\nВаш счёт: {score}\n')
    print(f'\nВсего игр сыграно: {stats.get("length")}')
    print(f'Максимальный рекорд: {stats.get("maximum")}')


if __name__ == '__main__':
    main()
