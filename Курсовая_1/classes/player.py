class Player:
    def __init__(self, name):
        self.name = name        # имя пользователя
        self.used_words = []    # использованные слова пользователя

    def __repr__(self):
        return f'{self.name} угадал слова: {", ".join(self.used_words)}'

    def count_words(self):
        """
        Получение к-ва использованных слов
        :return: int
        """
        return len(self.used_words)
    # реализовать

    def add_word(self, new_word):
        """
        Добавление слова в использованные слова
        :return: None
        """
        self.used_words.append(new_word)

    def has_used(self, word):
        """
        Проверка использования данного слова до этого
        :param word:
        :return: bool
        """
        return word in self.used_words


# test
vasiliy = Player("Василий")
vasiliy.add_word('жопа')
vasiliy.add_word('внатуре')
print(vasiliy)
print(vasiliy.has_used('жопа'))
print(vasiliy.has_used('что-то'))