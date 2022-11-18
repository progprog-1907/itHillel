def validate_password(password):
    """
    Функция принимает пароль строкой и выполняет валидацию с помощью трёх
    вспомогательных функций:
    1. Содержит только a−z, A−Z, 0−9
    2. Содержит четное количество букв
    3. Содержит нечетное количество цифр
    Основная функция возвращает True, если пароль валидный.
    Если пароль не валидный, возвращает лист стрингов, в которых перечислены
    причины неуспешной проверки. Например: ["содержит запрещенные символы"]
    """
    if not _validate_symbols(password):
        return ["Пароль содержит запрещенные символы"]
    if not _validate_letters_even(password):
        return ['Пароль содержит не четное количество букв']
    if not _validate_numbers_odd(password):
        return ["Пароль содержит четное количество цифр"]
    return True


def _validate_symbols(input_str):
    """
    Проверяет строку на наличие запрещенных символов
    Подсказка: у строк есть метод, проверяющий наличие только був и цифр
    Возвращает True\False
  """
    if not input_str.isalnum():
        return False
    return True


def _validate_letters_even(input_str):
    """
    Проверяет строку на четное количество букв
    Возвращает True\False
    """
    len_letter = len([let for let in input_str if let.isalpha()])
    if len_letter % 2:
        return False
    return True


def _validate_numbers_odd(input_str):
    """
    Проверяет строку на нечетное количество цифр
    Возвращает True\False
    """
    len_number = len([num for num in input_str if num.isdigit()])
    if not len_number % 2:
        return False
    return True


passw = "i3l2e9fb7q11!"
data = validate_password(passw)
print(data)
