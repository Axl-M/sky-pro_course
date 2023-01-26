import json

def load_question_from_json():
    with open('data.json', encoding='utf8') as file:
        data = json.load(file)
    return data


def show_field(questions):
    """
    Показывает (печатает) таблицу доступных вопросов
    :param questions: данные из json-файла
    :return: None
    """
    # category_name: Транспорт, Еда, Одежда
    # category_questions - всё остальное соответствующее этим категориям
    for category_name, category_questions in questions.items():
        print(category_name.ljust(10), end=' ')
        for score_price, question_data in category_questions.items():
            asked = question_data["asked"]
            if not asked:
                print(score_price.ljust(6), end=' ')
            else:
                print('  '.ljust(7), end='')
        print()


def parse_input(user_input) -> dict:
    """
    Делит ввод пользователя на категорию и число
    """
    user_data = user_input.split(" ")
    if len(user_data) != 2:
        return False
    # вставить всякую валидацию
    return {'category': user_data[0], 'price': user_data[1]}


# def print_question(question_text):
#     print(f"Слово {question_text} в переводе означает .....")


def show_stats(points, correct, incorrect):
    print("\nУ нас закончились вопросы!")
    print(f"\nВаш счёт: {points}")
    print(f"Верных ответов: {correct}")
    print(f"Неверных ответов: {incorrect}")


def save_results_to_file(points, correct, incorrect):
    """
    Запись результатов в файл
    :param points:
    :param correct:
    :param incorrect:
    :return:
    """
    with open('results.json', 'r', encoding='utf8') as file:
        results = json.load(file)
    results.append({"points": points, "correct": correct, "incorrect": incorrect})

    with open('results.json', 'w', encoding='utf8') as file:
        json.dump(results, file)


def get_total_number_of_questions(questions):
    counter = 0
    for category_questions in questions.values():
        counter += len(category_questions)
    return counter