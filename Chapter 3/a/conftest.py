import pathlib
import tempfile

import cards
import pytest


@pytest.fixture(scope="session")
def card_db():
    with tempfile.TemporaryDirectory() as temp_dir:
        db = cards.CardsDB(pathlib.Path(temp_dir))
        yield db
        db.close()
