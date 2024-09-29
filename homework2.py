from pathlib import Path 
path = 'cats.txt'


def get_cats_info(path):
    catsinfo = []
    with open(path, 'r') as fh:
        for line in fh:
            id, name, age = line.strip().split(',')
            cat = {"id": id, "name": name, "age": age}
            catsinfo.append(cat)
    result = '[\n'
    for cat in catsinfo:
        result += f'   {cat},\n'
    result += ']'
    return result


print(get_cats_info(path))
    