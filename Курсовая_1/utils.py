from config import WORDS_ON_JSON_KEEPER
def load_random_word():
    """
    получает список слов с внешнего ресурса
    выбирает случайное слово
    создает экземпляр класса BasicWord
    :return: экземпляр класса BasicWord
    """
    path = WORDS_ON_JSON_KEEPER