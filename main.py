import datetime
from collections import defaultdict

def read_data_from_file(filename):
    """Зчитує дані з текстового файлу та повертає список кортежів (назва, дата, ціна)."""
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(', ')
            if len(parts) != 3:
                continue  # Пропускаємо некоректні рядки
            name, date_str, price_str = parts
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                price = float(price_str)
                data.append((name, date, price))
            except ValueError:
                continue  # Пропускаємо рядки з помилками у форматі
    return data

