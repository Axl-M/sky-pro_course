class Question():
    def __init__(self, question_text, question_diff, question_answer):
        self.question_text = question_text
        self.question_diff = int(question_diff)
        self.question_answer = question_answer

        self.is_asked = False
        self.user_answer = None
        self.points = self.question_diff * 10

    def get_points(self):
        """ Получить к-во очков """
        return self.points


    def is_correct(self):
        """ Проверка правильности ответа """
        return self.user_answer == self.question_answer


    def build_question(self):
        return f'Вопрос: {self.question_text}\nСложность {self.question_diff}/5'


    def build_positive_feedback(self):
        return f'Ответ верный, получено {self.points} баллов'


    def build_negative_feedback(self):
        return f'Ответ НЕВЕРНЫЙ, верный ответ - {self.question_answer} '

