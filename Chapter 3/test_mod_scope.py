import pathlib
import tempfile

import cards
import pytest


@pytest.fixture(scope="module")
def card_db():
    with tempfile.TemporaryDirectory() as db_dir:
        db = cards.CardsDB(pathlib.Path(db_dir))
        yield db
        db.close()


def test_empty(card_db: cards.CardsDB):
    assert card_db.count() == 0


def test_count(card_db: cards.CardsDB):
    card_db.add_card(cards.Card("one card"))
    card_db.add_card(cards.Card("two card"))
    assert card_db.count() == 2
