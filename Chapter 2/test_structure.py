

# Given when then structure
from cards import Card


def test_to_dict():

    # Given
    c1 = Card("Some summary", "Sanjay", "todo", 123)

    # When
    card_dict = c1.to_dict();

    # Then
    expected_card_dict = {
        "summary": "Some summary",
        "owner": "Sanjay",
        "state": "todo",
        "id": 123
    }
    assert card_dict == expected_card_dict
