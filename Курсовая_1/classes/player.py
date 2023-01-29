class Player:
    def __init__(self, name):
        self.name = name        # имя пользователя
        self.used_words = []    # использованные слова пользователя

    def __repr__(self):
        pass

    def count_words(self):
        """
        Получение к-ва использованных слов
        :return: int
        """
        return 3
    # реализовать

    def add_word(self, word):
        """
        Добавление слова в использованные слова
        :return: None
        """
        self.used_words += word

    def has_used(self, word):
        """
        Проверка использования данного слова до этого
        :param word:
        :return: bool
        """
        return word in self.used_words

