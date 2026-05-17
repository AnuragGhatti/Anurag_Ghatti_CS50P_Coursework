# test_seasons.py

from seasons import get_minutes, convert_to_words
from datetime import date, timedelta
import pytest


def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_to_words(1051200) == "One million, fifty-one thousand, two hundred minutes"


def test_get_minutes_one_year():
    today = date.today()
    one_year_ago = today - timedelta(days=365)

    expected = 365 * 24 * 60
    assert get_minutes(str(one_year_ago)) == expected


def test_invalid_date():
    with pytest.raises(ValueError):
        get_minutes("invalid-date")

    with pytest.raises(ValueError):
        get_minutes("2025/01/01")

    with pytest.raises(ValueError):
        get_minutes("2025-13-40")
