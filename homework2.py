from pathlib import Path 
import pprint

def get_cats_info(path):
    catsinfo = []
    with open(path, 'r') as fh:
        for line in fh:
            id, name, age = line.strip().split(',')
            cat = {"id": id, "name": name, "age": age}
            catsinfo.append(cat)
    
    return catsinfo


cats_info = get_cats_info('cats.txt')
pprint.pprint(cats_info)
