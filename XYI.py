input = "Files_homeworks/authors.txt"


def parse_dates(input_file):
    result = list()
    file = open(input_file, "r")
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
print(test)

# text = text.split('\t')