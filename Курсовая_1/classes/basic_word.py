class BasicWord:
    """
    поля:
    исходное слово
    набор допустимых подслов
    методы:
    проверка введенного слова в списке допустимых подслов (вернет bool)
    подсчет к-ва слов (вернет int)
    """

    def __init__(self, word, subwords):
        """
        исходное слово
        набор допустимых подслов сосотавленных из исходного
        """
        self.word = word
        self.subword = subwords

    def __repr__(self):
        pass

    def has_subword(self, candidate):
        """
        проверка введенного слова в списке допустимых подслов
        :param candidate:
        :return: bool
        """
        return True
        # реализовать проверку

    def count_subwords(self):
        """
        подсчет к-ва слов
        :return: int
        """
        return 7
        # реализовать