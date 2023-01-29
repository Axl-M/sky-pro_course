# получить подслова
#
# получить к-во подслов
#
# проверить влетс ли слово подсловом

class BasicWord:
    def __init__(self, word, sub_words):
        self.word = word            # исходное слово
        self.sub_words = sub_words  # набор допустимых подслов сосотавленных из исходного

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
        # return len(self.sub_words)

