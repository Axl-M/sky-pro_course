print("Введите слово 'stop' для получения результата")
summa = 0
while (x := input('Введите число: ')) != 'stop':
    try:
        x = int(x)
    except ValueError:
        print('Необходимо ввести целое число')
    else:
        summa += x

print('Сумма чисел равна:', summa)
