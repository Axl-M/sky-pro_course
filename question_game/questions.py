class Question:
    def __init__(self, question_text, question_diff, question_answer):
        """
        :param question_text: Вопрос
        :param question_diff: уровень сложности (здесь переводится в int)
        :param question_answer: правильный ответ
        """
        self.question_text = question_text
        self.question_diff = int(question_diff)
        self.question_answer = question_answer

        self.is_asked = False                   #
        self.user_answer = None                 # ответ пользователя
        self.points = self.question_diff * 10   # очки за правильный ответ

    def get_points(self):
        """ Получить к-во очков """
        return self.points


    def is_correct(self):
        """ Проверка правильности ответа
        :return True or False
        """
        return self.user_answer == self.question_answer


    def build_question(self):
        """
        :return: сформированный вопрос
        """
        return f'\nВопрос: {self.question_text}\nСложность {self.question_diff}/5'


    def build_positive_feedback(self):
        """
        :return: Строка в случае верного ответа
        """
        return f'Ответ верный, получено {self.points} баллов'


    def build_negative_feedback(self):
        """
        return: Строка в случае неверного ответа
        """
        return f'Ответ НЕВЕРНЫЙ, верный ответ - {self.question_answer} '


    def __repr__(self):
        """
        :return: Представление объекта при вызове PRINT
        """
        return f'{self.question_text} - {self.question_answer} ({self.question_diff}/5)'