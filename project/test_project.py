from project import add_transaction, calculate_summary, category_totals


def test_add_transaction():
    data = []
    result = add_transaction(data, "income", "job", 1000, "2026-01-01")

    assert len(result) == 1
    assert result[0]["type"] == "income"
    assert result[0]["amount"] == 1000


def test_calculate_summary():
    data = [
        {"type": "income", "category": "job", "amount": 1000, "date": "2026-01-01"},
        {"type": "expense", "category": "food", "amount": 200, "date": "2026-01-02"}
    ]

    income, expense, net = calculate_summary(data)

    assert income == 1000
    assert expense == 200
    assert net == 800


def test_category_totals():
    data = [
        {"type": "expense", "category": "food", "amount": 100, "date": "2026-01-01"},
        {"type": "expense", "category": "food", "amount": 50, "date": "2026-01-02"},
        {"type": "expense", "category": "transport", "amount": 20, "date": "2026-01-03"}
    ]

    result = category_totals(data)

    assert result["food"] == 150
    assert result["transport"] == 20
