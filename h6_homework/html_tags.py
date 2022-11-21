# Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline
# Результатом работы декоратора с аргументами italic, bold должно быть преобразование
# из строки вида "test string" в "<i><b>test string</b></i>"


def str_to_html(tags):
    def decorator(func):
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }

        def wrapper(text):
            conversion_to_html = "%text%"
            for row in tags:
                conversion_to_html = conversion_to_html.replace("%text%", tag_base[row])
            conversion_to_html = conversion_to_html.replace("%text%", func(text))
            return conversion_to_html
        return wrapper
    return decorator


@str_to_html(["italic", "bold"])
def get_text(text):
    return text


print(get_text("salam"))
