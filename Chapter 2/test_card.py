from cards import Card


def test_field_access():
    c = Card("Something", "brian", "todo", 123)
    assert c.summary == "Something"
    assert c.owner == "brian"
    assert c.state == "todo"
    assert c.id == 123


def test_default():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None


def test_equality():
    c1 = Card("Something", "brian", "todo", 123)
    c2 = Card("Something", "brian", "todo", 123)
    assert c1 == c2


def test_equality_with_different_ids():
    c1 = Card("Something", "brian", "todo", 123)
    c2 = Card("Something", "brian", "todo", 456)
    assert c1 == c2


def test_inequality_with_different_ids():
    c1 = Card("Something", "brian", "todo", 123)
    c2 = Card("Something", "brian", "done", 456)
    assert c1 != c2


def test_from_dict():
    c1 = Card("Something", "brian", "todo", 123)
    c2_dict = {
        "summary": "Something",
        "owner": "brian",
        "state": "todo",
        "id": 123
    }
    c2 = Card.from_dict(c2_dict)
    assert c1 == c2


def test_to_dict():
    c2 = Card("Something", "brian", "todo", 456)
    c2_dict = {
        "summary": "Something",
        "owner": "brian",
        "state": "todo",
        "id": 456
    }

    assert c2.to_dict() == c2_dict
