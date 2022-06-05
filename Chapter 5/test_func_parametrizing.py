import cards
import pytest


@pytest.mark.parametrize(
    ["init_summary", "init_state"],
    [
        ("todo summary", "todo"),
        ("in prog summary", "in prog"),
        ("done summary", "done"),
    ])
def test_func_parametrize(cards_db: cards.CardsDB, init_summary, init_state):
    card_index = cards_db.add_card(cards.Card(init_summary, init_state))
    cards_db.finish(card_index)
    assert cards_db.get_card(card_index).state == "done"
