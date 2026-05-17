from fuel import convert, gauge
import pytest


# --------------------
# TEST convert()
# --------------------

def test_convert_basic_fractions():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75


def test_convert_edge_cases():
    assert convert("0/1") == 0
    assert convert("99/100") == 99


def test_convert_rounding():
    assert convert("2/3") == 67


def test_convert_negative_values():
    with pytest.raises(ValueError):
        convert("-1/2")

    with pytest.raises(ValueError):
        convert("1/-2")

    with pytest.raises(ValueError):
        convert("-1/-2")


def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("a/b")

    with pytest.raises(ValueError):
        convert("3/2")  # numerator > denominator

    with pytest.raises(ValueError):
        convert("1/2/3")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


# --------------------
# TEST gauge()
# --------------------

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
