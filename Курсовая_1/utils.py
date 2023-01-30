# функции

import json
import requests
import random
from config import WORDS_ON_JSON_KEEPER
from classes.basic_word import BasicWord

def load_random_word():
    """
        получает список слов с внешнего ресурса
        выбирает случайное слово (словарь)
        создает экземпляр класса BasicWord
        :return: экземпляр класса BasicWord
        """
    # пробный вариант
    # читаем локальный json
    DATA_SOURCE = "words.json"

    # def load_data(path):
    with open(DATA_SOURCE, encoding='utf8') as file:
        words = json.load(file)
        # return random.choice(words)   # вернуть случайный словарь
        # random.shuffle(words)
        # return words                    # или перемешанный список словарей


    # data = load_data(DATA_SOURCE)

    path = WORDS_ON_JSON_KEEPER
    # реализовать реальное получение из json
    # response = requests.get(path)
    # words = response.json()
    # random_word = random.choice(words)

# вернуть перемешанный словарь из внешнего ресурса
    # words_from_url = requests.get(path)
    # words = words_from_url.json()
    # random.shuffle(words)
    # return words


    # data = {
    #     "word": "питон",
    #     "sub_words": ["пони", "тон", "ион", "опт", "пот", "тип", "пион", "понт"]
    # }
    data = random.choice(words)
    word = BasicWord(data["word"], data["subwords"])
    # # word = BasicWord(random_word["word"], random_word["sub_words"])
    #

    return word # экземпляр класса


# print(load_random_word())
