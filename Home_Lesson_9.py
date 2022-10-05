import random
import string
# 1. Написать функцию которой передается один параметр - список строк my_list.
# # Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

def line_reversal(my_list):
    new_list = []
    for index, str_ in enumerate(my_list):
        if index % 2:
            new_list.append(str_[::-1])
        else:
            new_list.append(str_)
    return new_list

my_list = "qwe"
new_list = line_reversal(my_list)


#####################################################
# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".

def elements_with_letter_a(my_list):
    new_list = []
    for str_ in my_list:
         if "a" == str_[0]:
            new_list.append(str_)
    return new_list


my_list = ["appe", "htpat"]
new_list = elements_with_letter_a(my_list)

########################################################


# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.

def elements_with_letter_a_anywhere(my_list):
    new_list = []
    for str_ in my_list:
        if "a" in str_:
            new_list.append(str_)
    return new_list


my_list = ["appe", "htpat"]
new_list = elements_with_letter_a_anywhere(my_list)
##########################################################################

# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.

def get_string_list(my_list):
    result_list = []
    for value in my_list:
        if isinstance(value, str):
            result_list.append(value)
    return result_list

my_list = [1, 2, 3, "11", "22", 33]
result_list = get_string_list(my_list)
#################################################################
# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.

def get_unique_list(my_str):
    my_list = []
    my_set = set(my_str)
    for symbol in my_set:
        amount = my_str.count(symbol)
        if amount == 1:
            my_list.append(symbol)
    return my_list


my_str = "trollo"
my_list = get_unique_list(my_str)
####################################################################
# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

def get_duplicate_symbols_list(my_str_1, my_str_2):
    my_list = []
    for symb_1 in my_str_1:
        for symb_2 in my_str_2:
            if symb_1 == symb_2:
                my_list.append(symb_1)
    my_list = list(set(my_list))
    return my_list


my_str_1 = "qwerty"
my_str_2 = "qryip"
my_list = get_duplicate_symbols_list(my_str_1, my_str_2)
############################################################
# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
def characters_in_lines_one_at_a_time(my_str1, my_str2):
    common_elements = list(set(my_str1) & set(my_str2))
    unique_common_elements = []

    for element in common_elements:
        if my_str1.count(element) == 1 and my_str2.count(element) == 1:
            unique_common_elements.append(element)
    return unique_common_elements

my_str1 = "aaaasdf1"
my_str2 = "asdfff2"
unique_common_elements = characters_in_lines_one_at_a_time(my_str1, my_str2)

################################################################
# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
def generate_random_string():
    randon_lenths = random.randint(5, 7)
    random_string = random.choices(string.ascii_lowercase, k=randon_lenths)
    random_string = ''.join(random_string)
    return random_string


def create_email(domains,names):
    random_domain = random.choice(domains)
    random_number = random.randint(100, 999)
    random_names = random.choice(names)
    random_string = generate_random_string()

    emails = str(random_names) + "." + str(random_number) + "@" + str(random_string) + "." + random_domain
    return emails

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
