# шифр Цезаря (сдвиг букв на фиксированную длину)
# ф-ции для шифрования и расшифровки

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'


def shift_encode(string: str, shift: int) -> str:
    """
    Шифровка строки
    Заменяет каждую букву в строке на другую согласно значения переданного сдвига
    :param string: строка которую необходимо зашифровать
    :param shift: величина сдвига (может быть также и отрицательной)
    :return: зашифрованная строка
    """
    string_encoded = ''
    for letter in string:
        position = alphabet.find(letter)
        position_next = (position + shift) % len(alphabet)  # % для закольцовки сдвигов
        next_letter = alphabet[position_next]
        string_encoded += next_letter

    return string_encoded


def shift_decode(string: str, shift: int) -> str:
    """
    Дешифровка строки
    Заменяет каждую букву в строке на другую согласно значения переданного сдвига
    :param string: строка которую необходимо расшифровать
    :param shift: величина сдвига (может быть также и отрицательной) - то же значение что и при шифровании
    :return: расшифрованная строка
    """
    string_dencoded = ''
    for letter in string:
        position = alphabet.find(letter)  # если не найдет вернет последний (-1) что есть НЕПРАВИЛЬНО
        position_next = (position - shift) % len(alphabet)  # % для закольцовки сдвигов
        next_letter = alphabet[position_next]
        string_dencoded += next_letter 

    return string_dencoded


print(shift_encode('абвгдэюя', -1))
print(shift_decode('яабвгъэю', -1))
