from pathlib import Path
path = 'plata.txt'


def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r') as fh:
            for line in fh:
                name, salary = line.split(',')
                total += int(salary)
                count += 1
        average = int(total / count)
        result = f'Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}'
    except FileNotFoundError:
        result = print(f'Вказаного файла не існує або шлях "{path}" не є правильним')
        

    return result

print(total_salary(path))