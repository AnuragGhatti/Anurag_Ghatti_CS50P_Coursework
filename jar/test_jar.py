# test_jar.py

from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    custom_jar = Jar(5)
    assert custom_jar.capacity == 5

    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("hello")


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(2)

    assert jar.size == 2

    jar.deposit(3)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)

    jar.withdraw(2)
    assert jar.size == 3

    jar.withdraw(3)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)
