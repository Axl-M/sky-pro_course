import random


def get_random_words(url) -> list:
    """
    Получить перемешанный список слов из файла
    :return: list
    """
    with open(url, encoding='utf8') as fp:
        # words = [word.strip() for word in fp.readlines()]
        words = fp.read().splitlines()

    random.shuffle(words)
    return words


def shuffle_word(word: str) -> str:
    """
    перемешать буквы в слове
    :param word: слово
    :return: измененное слово
    """
    word_lst = list(word)
    random.shuffle(word_lst)
    # print(word)
    return ''.join(word_lst)


def save_score(url, name, score) -> None:
    """
    Сохранить имя и счет
    :param url: путь к файлу
    :param name: Имя
    :param score: счет
    :return: None
    """
    with open(url, 'a', encoding='utf8') as fp:
        fp.write(f'{name}: {score}\n')


def get_statistic(url) -> dict:
    """
    Получить статистику: всего игр было сыграно и максимальный счет
    :return: Cловарь (макс счёт, к-во игр)
    """
    scores = []
    with open(url, 'r', encoding='utf8') as fp:
        # lines = fp.read().splitlines()
        for line in fp:
            score = line.strip().split(' ')[-1]
            scores.append(int(score))

    max_score = max(scores)
    len_score = len(scores)
    return {'maximum': max_score, 'length': len_score}
