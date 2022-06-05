import argparse
import pathlib
import tempfile

import cards
import pytest


def db_scope(fixture_name: str, config: pytest.Config) -> str:
    if config.getoption("--func-db", None):
        return "function"
    return "session"


# Using MultiFixtures hook to determine register the --funct-db argument
def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--func-db",
        action="store_true",
        default=False
    )


@pytest.fixture(scope=db_scope)
def db():
    with tempfile.TemporaryDirectory() as temp_db_dir:
        db = cards.CardsDB(pathlib.Path(temp_db_dir))
        yield db
        db.close()


@pytest.fixture(scope="function")
def card_db(db: cards.CardsDB):
    db.delete_all()
    return db


@pytest.fixture(scope="session")
def sample_test_data():
    data = [
        cards.Card("test data 1"),
        cards.Card("test data 2"),
        cards.Card("test data 3"),
        cards.Card("test data 4")
    ]
    return data


@pytest.fixture(scope="function")
def two_count_db(card_db: cards.CardsDB, sample_test_data: list[cards.Card]):
    for i in range(2):
        card_db.add_card(sample_test_data[i])
    return card_db


@pytest.fixture(scope="function")
def four_count_db(card_db: cards.CardsDB, sample_test_data: list[cards.Card]):
    for i in range(4):
        card_db.add_card(sample_test_data[i])
    return card_db
