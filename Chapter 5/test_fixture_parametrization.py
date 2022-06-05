import cards
import pytest


@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
    return request.param


def test_finish(cards_db: cards.CardsDB, start_state: str):
    index = cards_db.add_card(cards.Card("A test summary", start_state))
    cards_db.finish(index)
    assert cards_db.get_card(index).state == "done"
