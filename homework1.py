from pathlib import Path


def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r') as fh:
            for line in fh:
                name, salary = line.split(',')
                total += float(salary)
                count += 1
            average = total / count
            return total, average
    except (FileNotFoundError, ZeroDivisionError):
            return None

result = total_salary('plata.txt')
if result is not None:    
    total, average = total_salary('plata.txt')
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
else:
     print('Файл не був знайден або він пустий')
