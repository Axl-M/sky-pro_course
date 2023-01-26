# Главный файл
from utils import load_questions, count_correct_answers, count__points

def main():
    # получаем список из перемешанных экземпляров вопросов (Question)
    questions = load_questions()

    for question in questions:              # для каждого экземпляра вопроса
        print(question.build_question())    # формируем текст вопроса
        question.user_answer = input()      # получаем от пользователя его вариант ответа

        if question.is_correct():           # ответ пользователя совпадает с правильным ответом?
            print(question.build_positive_feedback())
        else:
            print(question.build_negative_feedback())

    # к-во правильных ответов
    correct_counter = count_correct_answers(questions)
    # к-во заработанных очков
    points = count__points(questions)

    # вывод результата
    print("\nВот и всё!")
    print(f"Отвечено {correct_counter} вопросов из {len(questions)}")
    print(f"Набрано баллов: {points}")


if __name__ == '__main__':
    main()


