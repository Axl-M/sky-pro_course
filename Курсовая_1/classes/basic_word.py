class BasicWord:
    """
    поля:
    исходное слово
    набор допустимых подслов
    методы:
    проверка введенного слова в списке допустимых подслов (вернет bool)
    подсчет к-ва слов (вернет int)
    """

    def __init__(self, word, sub_words):
        """
        исходное слово
        набор допустимых подслов сосотавленных из исходного
        """
        self.word = word
        self.sub_words = sub_words

    def __repr__(self):
        return f"{self.word} содержит {len(self.sub_words)} слов"

    def has_subword(self, candidate):
        """
        проверка введенного слова в списке допустимых подслов
        :param candidate:
        :return: bool
        """
        return candidate.lower() in self.sub_words
        # реализовать проверку

    def count_subwords(self):
        """
        подсчет к-ва слов
        :return: int
        """
        return 7
        # реализовать