from CS50P.um.um import count


def test_single():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("hello, um, world") == 1


def test_multiple():
    assert count("Um, thanks, um...") == 2
    assert count("um um um") == 3


def test_case_insensitive():
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("uM") == 1


def test_not_substring():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0
    assert count("Um, thanks for the album.") == 1


def test_none():
    assert count("hello world") == 0
    assert count("") == 0
