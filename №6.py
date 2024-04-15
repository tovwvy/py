import requests
from bs4 import BeautifulSoup
import sqlite3

# Функція для отримання HTML-коду сторінки
def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Error:", response.status_code)
        return None

# Функція для парсингу товарів
def parse_amazon(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = soup.find_all('div', class_='s-result-item')  # знайдемо контейнери для кожного товару
    for product in products:
        title = product.find('span', class_='a-text-normal').text.strip()  # отримаємо назву товару
        price = product.find('span', class_='a-price')  # отримаємо ціну
        if price:
            price = price.find('span', class_='a-offscreen').text.strip()
        else:
            price = 'Ціна недоступна'
        print("Title:", title)
        print("Price:", price)
        print()

# Отримуємо HTML-код сторінки Amazon з категорії товарів, наприклад, електроніка
url = 'https://www.amazon.com/s?k=electronics'
html = get_html(url)

# Парсимо і виводимо інформацію про товари
if html:
    parse_amazon(html)

# Створення бази даних та таблиці
conn = sqlite3.connect('amazon_products.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    title TEXT,
    price TEXT
)
''')

# Додавання даних до таблиці
def add_product(title, price):
    cursor.execute('INSERT INTO products (title, price) VALUES (?, ?)', (title, price))
    conn.commit()

# Додавання прикладових даних
# Для реального використання можна додати дані з отриманих результатів парсингу
add_product("Samsung Galaxy S21", "$799")
add_product("Apple iPhone 13", "$999")

# Закриваємо з'єднання з базою даних
conn.close()
