def idiotic_str(input_str):
    """
    Вернуть полученную строку, сделав каждую вторую букву заглавной:
    Пример: тестовая строка -> тЕсТоВаЯ СтРоКа
    """
    # your code here
    lst = ''.join(l.upper() if i % 2 else l for i, l in enumerate(input_str))
    return lst


def filter_unique_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    убрать из него повторяющиеся элементы
    """
    # your code here
    unique_int_list = list(set(input_list))
    return unique_int_list


def DNA_pair(chain):
    """
    Дана одна цепь ДНК. Найти вторую цепь ДНК зная, что связи
    аденин (A) возможны с тимином (T), а гуанина (G) с цитозином (C).

    A <-> T, G <-> C

    in: "ATTGC" out: "TAACG"
    in: "GTAT" out: "CATA"
    """
    # your code here
    maps = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    pair = "".join(maps[i] for i in chain)
    return pair


def avg_score(score_list):
    """
    Дописать функцию, которая принимает список строк с оценками, а возвращает
    список строк со средним баллом
    Пример: ["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"] ->
    ["Mike|65", "Jane|42"]
    """
    # your code here
    avg_scores = list()
    for student in score_list:
        name, score_str = student.split("|")
        scores = [int(i) for i in score_str.split(", ")]
        avg_scores.append(f"{name}|{int(sum(scores) / len(scores))}")
    return avg_scores


avg_score(["Mike|83, 90, 34, 54", "Jane|45, 46, 53, 23"])


def three_biggest_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """
    # your code here
    biggest_ints = []
    i = True
    while i:
        if biggest_ints.count(max(input_list)) < 1:
            biggest_ints.append(max(input_list))
        if len(biggest_ints) == 3:
            i = False
        input_list.remove(max(input_list))
    return biggest_ints


def lowest_int_index(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """
    # your code here
    min_index_element = input_list.index(min(input_list))
    return min_index_element


def reversed_list(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """
    # your code here
    reversed = input_list[::-1]
    return reversed
