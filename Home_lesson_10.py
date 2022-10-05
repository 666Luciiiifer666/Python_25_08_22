# Все пункты сделать как отдельные функции и их вызовы.
#
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).

# file_name = "Files_homeworks/domains.txt"
# def domain_as_a_list(filename):
#
#     name = open(filename, "r")
#     text = name.read()
#     text = text.replace(".", "")
#     return(text)
# text = domain_as_a_list(file_name)
#
#

# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"

file_name = "Files_homeworks/names.txt"

def read_only_names (file_name):
    file = open(file_name, 'r')
    data = file.read()
    print(data)
    data = data.split('\t')[1::3]
    return data

data = read_only_names(file_name)
print(data)
print(file_name)


# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919"}, {"date": "8th February 1828"},  ...]
#
# По просьбам некоторых студентов начну включать дополнительные задания.
# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - это та же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
