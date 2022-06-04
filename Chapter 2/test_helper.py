from cards import Card
import pytest


def test_identical():
    c1 = Card("Some description", "Sanju", id=10)
    c2 = Card("Some description", "Sanju", id=11)
    assert c1 == c2


def assert_identical(c1: Card, c2: Card):
    __tracebackhide__ = True
    assert c1 == c2
    if c1.id != c2.id:
        pytest.fail("Id's are not equal!!")


def test_identical_strict():
    c1 = Card("Some description", "Sanju", id=10)
    c2 = Card("Some description", "Sanju", id=11)
    assert_identical(c1, c2)
    assert_identical(c1, c2)


if __name__ == "__main__":
    test_identical()
    test_identical_strict()
