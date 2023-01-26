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

    # print(questions)
    random.shuffle(questions)

    for question in questions:
        print(question)


if __name__ == '__main__':
    main()


