class NotInRangeError(Exception):
    def init(self, message=None):
        super().__init__(message)

def verbose_grade(gradeint):
    if gradeint == 2:
        return "Плохо"
    elif gradeint == 3:
        return "Плохо"
    elif gradeint == 4:
        return "Хорошо"
    elif gradeint == 5:
        return "Отлично"
    raise NotInRangeError("Value from 2 to 5 expected")

# И сразу же вызовем с неверными данными
try:
    verbose_grade(1)
except NotlnRangeError:
    print("Значение вне диапазона разрешенных значений")


