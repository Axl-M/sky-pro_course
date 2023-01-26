"""
Программа для тренировки расшифровки кода Морзе
"""
import random

words = ["code", "bit", "list", "soul", "next"]
MORZE_CODE = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•',
              'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•',
              'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•', 's': '•••', 't': '—', 'u': '••—',
              'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••'}
answers = []


def morse_encode(word):
    """
    Переводит слово в последовательность точек и тире
    :param word: исходное слово
    :return: строка морзянки
    """
    word_encoded = []
    for letter in word:
        word_encoded.append(MORZE_CODE.get(letter, ''))

    return '  '.join(word_encoded)


def get_word():
    """
    Получить случайное слово из списка
    :return:
    """
    return random.choice(words)


def print_statistics(answers):
    """
    На основании списка answers выводит статистику
    :param answers: список верных ответов вида [True, False, ...]
    :return:
    """
    answers_total = len(answers)
    # answers_correct = answers.count('True')
    answers_correct = sum(answers)  # boolean можно сложить
    answers_wrong = answers_total - answers_correct

    print(f'\nВопросов всего: {answers_total} \n'
          f'Правильных ответов: {answers_correct} \n'
          f'Неправильных ответов: {answers_wrong} \n')


def main():
    input('\nДавай потренируемся в расшифровке азбуки морзе. \nНажми [ENTER] для продолжения ...')
    # print(morse_encode('note'))

    for i in range(len(words)):
        rnd_word = get_word()
        words.remove(rnd_word)
        word_encoded = morse_encode(rnd_word)
        print(f'Слово #{i + 1}:  {word_encoded}')
        user_input = input()

        if user_input.lower() == rnd_word:
            print("Верно!")
            answers.append(True)
        else:
            print(f'Неверно. \nПравильный ответ - {rnd_word}')
            answers.append(False)

    print_statistics(answers)


if __name__ == '__main__':
    main()
