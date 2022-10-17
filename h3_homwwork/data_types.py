def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    # your code here
    result_list = [i for i in url_list if i.find("/catalog/") != -1]
    return result_list


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    # your code here
    output_str = input_str
    return output_str


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    # your code here
    output_list = list(set(input_str))
    output_list.sort()
    output_dict = {f"{i}": input_str.count(i) for i in output_list}
    return output_dict


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    # your code here
    result_str = str1[:int(len(str1) / 2) + str2 + str1[int(len(str1) / 2)]:]
    return result_str


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    # your code here
    even_int_list = [i for i in range(100) if i % 2 == 0]
    return even_int_list
