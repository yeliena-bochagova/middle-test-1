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

def filter_last_month_data(data):
    """Фільтрує записи за останній місяць."""
    today = datetime.date.today()
    last_month = today - datetime.timedelta(days=30)
    return [entry for entry in data if entry[1] >= last_month]


def analyze_price_changes(data):
    """Аналізує зміни цін для всіх товарів за останній місяць."""
    product_data = defaultdict(list)

    for name, date, price in data:
        product_data[name].append((date, price))

    results = []
    for product_name, entries in product_data.items():
        sorted_entries = sorted(entries, key=lambda x: x[0])
        first_price = sorted_entries[0][1]
        last_price = sorted_entries[-1][1]
        price_diff = last_price - first_price
        results.append(
            f"Зміна ціни на '{product_name}': {first_price} -> {last_price} ({'+' if price_diff > 0 else ''}{price_diff}) грн")

    return "\n".join(results)

if __name__ == "__main__":
    filename = "products.txt"  # Ім'я файлу з даними
    data = read_data_from_file(filename)
    last_month_data = filter_last_month_data(data)
    result = analyze_price_changes(last_month_data)
    print(result)