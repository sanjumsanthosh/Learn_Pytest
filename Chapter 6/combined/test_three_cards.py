import cards
import pytest


@pytest.mark.num_cards(0)
def test_zero(cards_db_init: cards.CardsDB):
    assert cards_db_init.count() == 0


@pytest.mark.num_cards(3)
def test_three(cards_db_init: cards.CardsDB):
    for card in cards_db_init.list_cards():
        print(card)
    assert cards_db_init.count() == 3
