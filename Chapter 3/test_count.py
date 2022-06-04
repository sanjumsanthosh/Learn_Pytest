from pathlib import Path

import cards
import pytest
from tempfile import TemporaryDirectory


@pytest.fixture()
def card_db():
    with TemporaryDirectory() as db_dir:
        db = cards.CardsDB(Path(db_dir))
        yield db
        db.close()


def test_empty(card_db: cards.CardsDB):
    initial_count = card_db.count()
    assert initial_count == 0


def test_two_count2(card_db: cards.CardsDB):
    card_db.add_card(cards.Card("summary 1"))
    card_db.add_card(cards.Card("summary 2"))
    count = card_db.count()
    assert count == 2
