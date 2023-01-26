
from functions_all import *
# from pprint import pprint


def main():
    questions = load_question_from_json()  # получить данные json
    # изменять будем в этом словаре (question: True/False).
    # Оригинал json не трогаем
    points, correct, incorrect = 0, 0, 0
    questions_total = get_total_number_of_questions(questions)
    questions_asked = 0

    while correct + incorrect < questions_total:
        show_field(questions)
        user_input = input("Выберите категорию и баллы (через пробел): ").title()
        user_data = parse_input(user_input)

        if not user_data:
            continue
        category, price = user_data["category"], user_data["price"]
        # print(category, price)

        try:
            question = questions[category][price]
        except:
            print("Неверная категория\n")
            continue

        if question["asked"]:
            print("Вы уже отвечали на этот вопрос")
            continue

        # print_question(question["question"])
        print(f'Слово {question["question"]} в переводе означает .....')
        user_answer = input()

        if user_answer == question["answer"]:
            print("Ответ верный!\n")
            points += int(price)
            correct += 1
        else:
            print("Ответ НЕверный!\n")
            points -= int(price)
            incorrect += 1

        question["asked"] = True
        questions_asked += 1

    show_stats(points, correct, incorrect)
    save_results_to_file(points, correct, incorrect)


if __name__ == "__main__":
    main()
