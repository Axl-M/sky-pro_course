# функции
import json

# DATA_SOURCE = "data/quest.json"
#
# def load_data(path):
#     with open(path):
#         return json.load(file)
#
# data = load_data(DATA_SOURCE)


import requests

from config import WORDS_ON_JSON_KEEPER
from classes.basic_word import BasicWord
import random

def load_random_word():
    """
    получает список слов с внешнего ресурса
    выбирает случайное слово (словарь)
    создает экземпляр класса BasicWord
    :return: экземпляр класса BasicWord
    """
    path = WORDS_ON_JSON_KEEPER
    # реализовать реальное получение из json
    # response = requests.get(path)
    # words = response.json()
    # random_word = random.choice(words)

    data = {
    "word": "питон",
    "sub_words": ["пони", "тон", "ион", "опт", "пот", "тип", "пион", "понт"]
    }
    word = BasicWord(data["word"], data["sub_words"])
    # word = BasicWord(darandom_wordta["word"], random_word["sub_words"])

    return word # экземпляр класса


# print(load_random_word())
