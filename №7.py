import csv
import statistics

def read_csv_file(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def task_a(data):
    first_app_name = data[0]['App']
    print(f"a. Назва першої програми у наборі даних: {first_app_name}")

def task_b(data):
    last_category = data[-1]['Category']
    print(f"b. Категорія останньої програми у наборі даних: {last_category}")

def task_c(data):
    num_columns = len(data[0])
    print(f"c. Кількість стовпців у наборі даних: {num_columns}")

def task_d(data):
    sizes = []
    for app in data:
        size = app['Size']
        if size.endswith('M'):
            size = float(size.replace('M', ''))
            sizes.append(size)
        elif size.endswith('k'):
            size = float(size.replace('k', '')) * 1024
            sizes.append(size)
        else:
            continue
    if sizes:  # перевірка, чи є дані у списку
        average_size = statistics.mean(sizes)
        median_size = statistics.median(sizes)
        print(f"d. Середнє арифметичне розміру додатків: {average_size} байт")
        print(f"   Медіана розміру додатків: {median_size} байт")
    else:
        print("У наборі даних немає вказаних розмірів додатків.")


def task_e(data):
    max_reviews_app = max(data, key=lambda x: int(x['Reviews']))
    max_reviews_category = max_reviews_app['Category']
    print(f"e. Категорія додатка з найбільшою кількістю відгуків: {max_reviews_category}")

def task_f(data):
    expensive_apps = [float(app['Rating']) for app in data if app['Price'] != '0']
    if len(expensive_apps) > 0:
        average_rating_expensive = statistics.mean(expensive_apps)
    else:
        average_rating_expensive = 0
    print(f"f. Середній рейтинг дорогих додатків: {average_rating_expensive}")

# Основна функція для виконання всіх завдань
def main():
    filename = 'GoogleApps.csv'
    data = read_csv_file(filename)
    task_a(data)
    task_b(data)
    task_c(data)
    task_d(data)
    task_e(data)
    task_f(data)

if __name__ == "__main__":
    main()
