import json
import re

# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.

filename = "Files_homeworks//data.json"


def Current_data_state(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


data = Current_data_state(filename)


# 2. Написать "функцию сортировки" данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
#


def sort_by_name(item):
    name = item['name']
    surname = name.split(' ')[-1]
    return surname


surname_data = sorted(data, key=sort_by_name)


# 3. Написать функцию сортировки по количеству слов в поле "text".

def sort_by_text(item):
    text = item['text']
    number_words = len(text.split(' '))
    return number_words


sorted_by_text_len = sorted(data, key=sort_by_text)


# 4. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
#
#
# Кроме функций сортировки также надо написать их использование.


def sort_by_years(a: str) -> int:
    year = re.match(".+\s(\d+)\D", a).group(1)
    year = -int(year) if ("bc" in a.lower()) else int(year)
    return year


sorted_by_year = sorted(data, key=lambda x: sort_by_years(x["years"]))

