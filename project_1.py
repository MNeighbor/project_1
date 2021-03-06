import time
import typing


# Реализовать чтение данных из файла именно как функцию
# Функция, читающая файл
# read_file должен принимать имя (путь) файла
# Функция read_file принимает путь к файлу
def read_file(name_file):
    # Пустой список куда данные будут заноситься построчно
    l = []
    # Прочитаем исходные данные из файла
    with open(name_file, encoding="utf8") as f:
        # Чтение данных происходит построчно
        for line in f:
            l.append(line.replace("\n", "").split())
    return l


# Тестирование времени работы программы
class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kwargs):
        # Начальный отсчет времени
        start_time = time.time()
        # Выполение функции
        original_result = self.func(*args, **kwargs)
        # Разница во времени
        result_time = time.time() - start_time
        # Счетчик времени выполнение функции
        self.alltime += result_time
        # Печать имя функции и время его выполнения
        print(f"Общее время выполнения функции {self.func.__name__} "
              f"составило {self.alltime}")
        # Возвращаем функцию
        return original_result


@timer
def min_numeric(args):
    min_list = []
    for i in args:
        i = list(map(float, i))
        min_list.append(min(i))
    return min(min_list)


@timer
def max_numeric(args):
    max_list = []
    for i in args:
        i = list(map(float, i))
        max_list.append(max(i))
    return max(max_list)


@timer
def sum_numeric(args):
    result = 0
    for i in args:
        q = list(map(float, i))
        result += sum(q)
    return result


# Лучше возвращать Optional[float], нежели строку в случае переполнения
# Не args: typing.Optional[float] А args: typing.Optional[List[float]]
@timer
def mult_numeric(args: typing.Optional[list[float]]):
    result = 1
    if args == float("inf"):
        return args
    for numeric in args:
        for i in numeric:
            try:
                result *= float(i)
            except OverflowError:
                print("Бесконечность!")
    # if result == float("inf"): return result else: return result И в чем смысл этого условного оператора?
    # Просто возвращаем результат вычислений без условий
    return result


if __name__ == "__main__":
    # В функцию read_file передаем путь к файлу
    # В рамках компьютера путь к файлу будет выглядеть следующим образом, например
    # print(min_numeric(read_file(r"C:\Users\stars\PythonCourse\project\project_1.txt")))
    # Для git оставим следующим образом
    print(min_numeric(read_file(r"project_1.txt")))
    print(max_numeric(read_file(r"project_1.txt")))
    print(sum_numeric(read_file(r"project_1.txt")))
    print(mult_numeric(read_file(r"project_1.txt")))
