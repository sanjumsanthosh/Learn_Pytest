from cards import Card
import pytest


def test_alt_fail():
    c1 = Card("Hello welcome", "Brian")
    c2 = Card("Hi there", "Sanjay")
    if c1 != c2:
        pytest.fail("The two cards don't match")


# Calling directly
if __name__ == "__main__":
    test_alt_fail()
