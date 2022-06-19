import unittest.mock

import cards

from test_typer_testing import card_cli


def test_add_with_owner(mock_cards_db: unittest.mock.MagicMock):
    result = card_cli("add some task -o brian")
    expected = cards.Card('some task', 'brian')
    mock_cards_db.add_card.assert_called_with(expected)


def test_delete_card_with_invalid_id(mock_cards_db: unittest.mock.MagicMock):
    mock_cards_db.delete_card.side_effect = cards.InvalidCardId
    output = card_cli("delete 1")
    assert "Invalid card" in output
