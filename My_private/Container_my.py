# КОНТЕЙНЕР-ПОСЛЕДОВАТЕЛЬНОСТЬ
# доступ к любому элементу по индексу

class MutableString:
    """
    строка которую МОЖНО изменять как и список
    """
    def __init__(self, s):
        self.__s = list(s)

    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        if self.__i > len(self.__s) - 1:
            raise StopIteration
        else:
            a = self.__s[self.__i]
            self.__i = self.__i + 1
            return a

    def __len__(self):
        return len(self.__s)

    def __str__(self):
        return "".join(self.__s)

    def __is_correct_index(self, i):
        if type(i) == int or type(i) == slice:
            if type(i) == int and i > self.__len__() - 1:
                raise IndexError
        else:
            raise TypeError

    # функциональность контейнера
    def __getitem__(self, i):
        self.__is_correct_index(i)
        return self.__s[i]
    def __setitem__(self, i, value):
        self.__is_correct_index(i)
        self.__s[i] = value
    def __delitem__(self, i):
        self.__is_correct_index(i)
        del self.__s[i]
    def __contains__(self, value):
        return value in self.__s



# test
s = MutableString("Python")
print(s)
print(s[-1])
s[0] = "J"
print(s)
del s[2:4]
print(s)
# print(s[9]) # ошибка индекса


# КОНТЕЙНЕР-ОТОБРАЖЕНИЕ
# доступ по ключу

class Version:
    """
    хранит версию интерпретатора разбитую на части
    """
    def __init__(self, major, minor, sub):
        self.__major = major    # Старшая версия
        self.__minor = minor    # Младшая версия
        self.__sub = sub        # Модификация

    def __str__(self):
        return str(self.__major) + "." + str(self.__minor) + "." + str(self.__sub)

    # функциональность отображения
    def __getitem__(self, key):
        if key == 'major':
            return self.__major
        if key == 'minor':
            return self.__minor
        if key == 'sub':
            return self.__sub
        else:
            raise KeyError
    def __setitem__(self, key, value):
        if key == 'major':
            self.__major = value
        if key == 'minor':
            self.__minor = value
        if key == 'sub':
            self.__sub = value
        else:
            raise KeyError
    def __delitem__(self, key):
        raise NotImplementedError
    def __contains__(self, v):
        return v == 'major' or v == 'minor' or v == 'sub'


# test
v = Version(3, 10, 1)
print(v)
print(v['major'])
print(v['minor'])
print(v['sub'])
v['sub'] = 2
print(v)
print(v['some'])        # ошибка.
