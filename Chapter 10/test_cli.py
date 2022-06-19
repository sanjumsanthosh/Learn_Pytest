import unittest.mock

import cards

from test_typer_testing import card_cli


def test_add_with_owner(mock_cards_db: unittest.mock.MagicMock):
    result = card_cli("add some task -o brian")
    expected = cards.Card('some task', 'brian')
    mock_cards_db.add_card.assert_called_with(expected)
