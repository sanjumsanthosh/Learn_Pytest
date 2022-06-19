import unittest.mock
import cards

from test_typer_testing import card_cli


def test_mock_version():
    mock_version = "1.2.3"
    with unittest.mock.patch.object(cards, "__version__", mock_version):
        result = card_cli("version")
        print(f"\nversion : {result}")
        assert result==mock_version

