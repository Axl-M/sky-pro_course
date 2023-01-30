# функции

# import json  # нужен только для парса локального json
import requests
import random
from config import WORDS_ON_JSON_KEEPER
from classes.basic_word import BasicWord

def load_random_word():
    """
        Получает список слов с внешнего ресурса
        выбирает случайное слово (словарь)
        создает экземпляр класса BasicWord
        :return: экземпляр класса BasicWord
        """
    # пробный вариант
    # читаем локальный json
    # DATA_SOURCE = "words.json"
    # with open(DATA_SOURCE, encoding='utf8') as file:
    #     words = json.load(file)
    #

    # ИЛИ
    # реальное получение json из сети
    path = WORDS_ON_JSON_KEEPER
    # print(path)
    response = requests.get(path)
    words = response.json()

    random_word = random.choice(words)    # получить один из словарей
    word = BasicWord(random_word["word"], random_word["subwords"])
    return word # экземпляр класса


# вернуть перемешанный словарь из внешнего ресурса
    # words_from_url = requests.get(path)
    # words = words_from_url.json()
    # random.shuffle(words)
    # return words


# print(load_random_word())