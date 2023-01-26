# вынес функции
import random
from data import questions_data     # вопросы
from questions import Question      # класс Вопрос

def load_questions():
    questions = []
                                        # из словарей (вопросов) из списка
    for question_data in questions_data:
        questions.append(Question(      # создать список ОБЪЕКТОВ вопросов
            question_data["q"],
            question_data["d"],
            question_data["a"]
        ))

    random.shuffle(questions)           # перемешиваем
    return questions

def count_correct_answers(questions):
    """
    :param questions: Список ОБЪЕКТОВ вопросов
    :return: к-во правильных ответов
    """
    correct_counter = 0

    for question in questions:      # для каждого объекта вопроса
        if question.is_correct():   # проверяем правильность ответа
            correct_counter += 1

    return correct_counter


def count__points(questions):
    """
    :param questions: Список ОБЪЕКТОВ вопросов
    :return: к-во очков
    """
    count_points = 0

    for question in questions:
        if question.is_correct():                   # # для каждого правильного объекта вопроса
            count_points += question.get_points()   # прибавить его к-во баллов

    return count_points