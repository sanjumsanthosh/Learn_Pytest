import cards
import pytest


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if "init_state" in metafunc.fixturenames:
        metafunc.parametrize("init_state", ["todo", "in prog", "done"])


def test_finish(cards_db: cards.CardsDB, init_state):
    c = cards.Card("test summary", init_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    assert cards_db.get_card(index).state == "done"
