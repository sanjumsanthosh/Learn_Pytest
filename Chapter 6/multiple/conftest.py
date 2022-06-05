import cards
import pytest


@pytest.fixture(scope="session")
def db(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("Cards_db")
    db = cards.CardsDB(tmp_dir)
    yield db
    db.close()


@pytest.fixture()
def cards_db(db: cards.CardsDB):
    db.delete_all()
    return db
