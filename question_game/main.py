import random
from questions import Question
from data import questions_data

def main():
    questions = []

    for question_data in questions_data:
        questions.append(Question(
            question_data["q"],
            question_data["d"],
            question_data["a"]
        ))

    random.shuffle(questions)

    for question in questions:
        print(question.build_question())
        user_answer = input()
        question.user_answer = user_answer

        if question.is_correct():
            print(question.build_positive_feedback())
        else:
            print(question.build_negative_feedback())

    correct_counter = 0
    points = 0

    for question in questions:
        if question.is_correct():
            correct_counter += 1
            points += question.get_points()

    print("\nВот и всё!")
    print(f"Отвечено {correct_counter} вопросов из {len(questions)}")
    print(f"Набрано баллов: {points}")

if __name__ == '__main__':
    main()


