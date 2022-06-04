from cards import Card


def test_equality_fail():
    c1 = Card("Hello welcome", "Brian")
    c2 = Card("Hi there", "Sanjay")
    assert c1 == c2


# Calling directly
if __name__ == "__main__":
    test_equality_fail()
