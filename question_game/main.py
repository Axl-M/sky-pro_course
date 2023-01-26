from questions import Question
from data import questions_data

def main():
    questions = []

    for question_data in questions_data:
        new_question = Question(
            question_data["q"],
            question_data["d"],
            question_data["a"]
        )

# test __repr__
        print(new_question)
        questions.append(new_question)

if __name__ == '__main__':
    main()


