import random
from data import questions_data
from questions import Question

def load_questions():
    questions = []

    for question_data in questions_data:
        questions.append(Question(
            question_data["q"],
            question_data["d"],
            question_data["a"]
        ))

    random.shuffle(questions)
    return questions

def count_correct_answers(questions):
    correct_counter = 0

    for question in questions:
        if question.is_correct():
            correct_counter += 1

    return correct_counter


def count_points(questions):
    count_points = 0

    for question in questions:
        if question.is_correct():
            count_points += question.get_points()

    return count_points