import pathlib
import tempfile

import cards
import pytest


@pytest.fixture(scope="session")
def db():
    with tempfile.TemporaryDirectory() as temp_dir:
        db = cards.CardsDB(pathlib.Path(temp_dir))
        yield db
        db.close()


@pytest.fixture(scope="function")
def card_db(db):
    db.delete_all()
    return db


@pytest.fixture(scope="session")
def test_cards():
    test_cards = [
        cards.Card("test card 1"),
        cards.Card("test card 2"),
        cards.Card("test card 3"),
        cards.Card("test card 4")
    ]
    return test_cards


@pytest.fixture(scope="function")
def test_card_db(card_db: cards.CardsDB, test_cards: list[cards.Card]):
    for card in test_cards:
        card_db.add_card(card)
    return card_db
