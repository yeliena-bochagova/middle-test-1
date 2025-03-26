import datetime
import pytest
from main import read_data_from_file, filter_last_month_data, analyze_price_changes


def test_read_data_from_file(tmp_path):
    test_file = tmp_path / "test_products.txt"
    test_file.write_text("""
    Яблуко, 2024-03-10, 20.5
    Груша, 2024-03-15, 18.0
    """.strip(), encoding="utf-8")

    data = read_data_from_file(test_file)
    assert len(data) == 2
    assert data[0] == ("Яблуко", datetime.date(2024, 3, 10), 20.5)
    assert data[1] == ("Груша", datetime.date(2024, 3, 15), 18.0)


def test_filter_last_month_data():
    today = datetime.date.today()
    last_month = today - datetime.timedelta(days=20)
    old_date = today - datetime.timedelta(days=40)

    data = [("Яблуко", last_month, 20.5), ("Груша", old_date, 18.0)]
    filtered = filter_last_month_data(data)
    assert len(filtered) == 1
    assert filtered[0][0] == "Яблуко"


def test_analyze_price_changes():
    today = datetime.date.today()

    data = [("Яблуко", today - datetime.timedelta(days=10), 20.5),
            ("Яблуко", today, 22.0),
            ("Груша", today - datetime.timedelta(days=15), 18.0),
            ("Груша", today, 19.5)]

    result = analyze_price_changes(data)
    assert "Зміна ціни на 'Яблуко': 20.5 -> 22.0 (+1.5) грн" in result
    assert "Зміна ціни на 'Груша': 18.0 -> 19.5 (+1.5) грн" in result