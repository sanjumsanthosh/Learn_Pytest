import cards
import pytest


@pytest.fixture(scope="session")
def db(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("card_db")
    db = cards.CardsDB(tmp_dir)
    yield db
    db.close()


@pytest.fixture(scope='session')
def test_data():
    return [
        cards.Card("Test data 1"),
        cards.Card("Test data 2"),
        cards.Card("Test data 3"),
        cards.Card("Test data 4"),
    ]


@pytest.fixture(scope="function", name="db_with_data")
def db_with_data_fixture(db: cards.CardsDB, test_data: list[cards.Card]):
    db.delete_all()
    for card in test_data:
        db.add_card(card)
    return db
