import time

l = []
# Прочитаем исходные данные из файла
with open("project_1.txt", encoding="utf8") as f:
    # Чтение данных происходит построчно
    for line in f:
        l.append(line.replace("\n", "").split())


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


@timer
def mult_numeric(args):
    result = 1
    if args == float("inf"):
        return "Бесконечность!"
    for numeric in args:
        for i in numeric:
            try:
                result *= float(i)
            except OverflowError:
                print("Бесконечность!")
    if result == float("inf"):
        return "Бесконечность!"
    else:
        return result


if __name__ == "__main__":
    print(min_numeric(l))
    print(max_numeric(l))
    print(sum_numeric(l))
    print(mult_numeric(l))
