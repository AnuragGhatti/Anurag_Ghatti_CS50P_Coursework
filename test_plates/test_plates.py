from plates import is_valid


def test_valid_cases():
    assert is_valid("CS50") is True
    assert is_valid("CS") is True
    assert is_valid("AAA222") is True


def test_too_short():
    assert is_valid("C") is False
    assert is_valid("") is False


def test_too_long():
    assert is_valid("ABCDEFG") is False
    assert is_valid("CS50ABC1") is False


def test_starting_characters_must_be_letters():
    assert is_valid("1CS50") is False
    assert is_valid("50CS") is False
    assert is_valid("123") is False


def test_numbers_cannot_be_in_middle():
    assert is_valid("CS50P") is False
    assert is_valid("AA22AA") is False


def test_first_number_cannot_be_zero():
    assert is_valid("CS05") is False
    assert is_valid("CS050") is False


def test_no_punctuation_or_spaces():
    assert is_valid("CS.50") is False
    assert is_valid("CS 50") is False
    assert is_valid("CS-50") is False
