import unittest.mock
import cards
import pytest

from test_typer_testing import card_cli


def test_mock_version():
    mock_version = "1.2.3"
    with unittest.mock.patch.object(cards, "__version__", mock_version, autospec=True):
        result = card_cli("version")
        print(f"\nversion : {result}")
        assert result == mock_version


def test_mock_cardsDB():
    mock_config_path = "/foo"
    with unittest.mock.patch.object(cards, "CardsDB") as mockCardsDB:
        print(f"\n cardsDB : {mockCardsDB.return_value}")
        mockCardsDB.return_value.path.return_value = mock_config_path
        result = card_cli("config")
        assert result == mock_config_path


@pytest.fixture()
def mock_cards_db():
    with unittest.mock.patch.object(cards, "CardsDB") as mockCardsDB:
        yield mockCardsDB.return_value


def test_config_with_fixture(mock_cards_db: unittest.mock.MagicMock):
    mock_config_path = "./foo"
    mock_cards_db.path.return_value = mock_config_path
    config_result = card_cli("config")
    assert config_result == mock_config_path


@pytest.fixture()
def mock_cards_db_norm():
    with unittest.mock.patch.object(cards, "CardsDB") as mockCardsDB:
        yield mockCardsDB.return_value


def test_config_bad(mock_cards_db_norm: unittest.mock.MagicMock):
    mock_config_path = "./foo"
    mock_cards_db_norm.path.return_value = mock_config_path
    mock_cards_db_norm.pat.return_value = mock_config_path
    config_result = card_cli("config")
    assert config_result == mock_config_path


@pytest.fixture()
def mock_cards_db_autospec():
    with unittest.mock.patch.object(cards, "CardsDB", autospec=True) as mockCardsDB:
        yield mockCardsDB.return_value


@pytest.mark.skip()
def test_config_bad_autospec(mock_cards_db_autospec: unittest.mock.MagicMock):
    mock_config_path = "./foo"
    mock_cards_db_autospec.path.return_value = mock_config_path
    mock_cards_db_autospec.pat.return_value = mock_config_path
    config_result = card_cli("config")
    assert config_result == mock_config_path
