import pytest
import unittest.mock
import cards


@pytest.fixture()
def mock_cards_db():
    with unittest.mock.patch.object(cards, "CardsDB") as mockCardsDB:
        yield mockCardsDB.return_value
