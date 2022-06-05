import cards
import pytest


@pytest.fixture(scope="session")
def db(tmp_path_factory) -> cards.CardsDB:
    tmp_path = tmp_path_factory.mktemp("cards_db")
    db = cards.CardsDB(tmp_path)
    yield db
    db.close()


@pytest.fixture(scope="function")
def cards_db(db) -> cards.CardsDB:
    db.delete_all()
    return db
