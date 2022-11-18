# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных
import os


def log_reading(func):
    def wrapper():
        for file in func():
            if file.endswith(".log"):
                with open(file, mode="r") as files:
                    print(files.read())
                    files.seek(0)
    return wrapper


@log_reading
def get_files():
    file_list = [file.name for file in os.scandir(".") if file.is_file()]
    return file_list


get_files()
