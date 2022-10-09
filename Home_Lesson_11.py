import string
import random as rnd
import json

# Функция generate_txt_data. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы.

lenght = rnd.randint(100, 1000)

def generate_txt_data (lenght):

    list_of_symbols = string.ascii_letters + string.digits + string.whitespace[0]
    final_str = ''.join(rnd.choice(list_of_symbols) for _ in range(lenght))
    return final_str

final_str = generate_txt_data (lenght)
#



# Функция generate_json_data. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool

lenght = rnd.randint(5, 20)
def generate_json_data(lenght):

    data = []
    for _ in range(lenght):
        keys = ''.join(rnd.choice(string.ascii_lowercase) for _ in range(5))
        values = rnd.choice([rnd.randint(-100, 100), rnd.random(), rnd.choice([True, False])])
        dict = {keys: values}
        data.append(dict)
        json_data = json.dumps(data)
    return json_data
json_data = generate_json_data(lenght)



Функция generate_and_write_file. Написать функцию которая принимает один параметр - полный путь к файлу.
В зависимости от расширения файла (txt, json) сгенерировать данные для записи и записать в данный файл.
Если расширение не соответствует заданным, то вывести текст "Unsupported file format"

Разрешается создавать дополнительные (вспомогательные) функции.



