# Все пункты сделать как отдельные функции и их вызовы.
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).

file_name = "Files_homeworks/domains.txt"
def domain_as_a_list(filename):
 with open(filename, "r") as file:
    text = file.read()
    text = text.replace(".", "").split("\n")
    return(text)
text = domain_as_a_list(file_name)



# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"

file_name = "Files_homeworks/names.txt"

def read_only_names(file_name):
    result = list()
    with open(file_name, 'r') as file:
        file = file.read()
        read_file = file.splitlines()
        for line in read_file:
            info = line.split('\t')
            dates = info[1]
            result.append(dates)
    return result

result = read_only_names(file_name)



# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919"}, {"date": "8th February 1828"},  ...]


input = "Files_homeworks/authors.txt"


def parse_dates(input_file):
    result = list()
    with open(input_file, "r") as file:
        file = file.read()
        read_file = file.splitlines()
        for line in read_file:
             if line != "":
                info = line.split('-')
                dates = info[0]
                if len(dates.split()) > 2:
                    result.append({'date': dates})
    return result


test = parse_dates(input)
