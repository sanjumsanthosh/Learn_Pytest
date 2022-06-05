import cards
import pytest


@pytest.mark.smoke
def test_start(cards_db: cards.CardsDB):
    index = cards_db.add_card(cards.Card("foo", state="todo"))
    cards_db.start(index)
    assert cards_db.get_card(index).state == "in prog"


@pytest.mark.exception
def test_start_non_existent(cards_db: cards.CardsDB):
    any_number = 123
    with pytest.raises(cards.InvalidCardId):
        cards_db.start(any_number)
        assert cards_db.get_card(any_number).state == "in prog"
