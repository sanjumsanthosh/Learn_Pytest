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
