from config import WORDS_ON_JSON_KEEPER
from classes.basic_word import BasicWord

def load_random_word():
    """
    получает список слов с внешнего ресурса
    выбирает случайное слово
    создает экземпляр класса BasicWord
    :return: экземпляр класса BasicWord
    """
    path = WORDS_ON_JSON_KEEPER
    # реализовать реальное получение из json
    data = {
    "word": "питон",
    "sub_words": ["пони", "тон", "ион", "опт", "пот", "тип", "пион", "понт"]
    }
    word = BasicWord(data["word"], data["sub_words"])

    return word


print(load_random_word())
