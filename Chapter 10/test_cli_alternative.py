import shlex

import cards
import pytest
import typer.testing

from test_typer_testing import card_cli

runner = typer.testing.CliRunner()


@pytest.fixture(scope="session")
def tmp_path(tmp_path_factory):
    with tmp_path_factory.mktemp("CardsDB") as tmp_path:
        yield tmp_path


@pytest.fixture(scope="function")
def cards_db(tmp_path, monkeypatch):
    monkeypatch.setenv("CARDS_DB_DIR", str(tmp_path))
    db_ = cards.CardsDB(tmp_path)
    db_.delete_all()
    yield db_
    db_.close()


def cards_cli(command: str):
    lexical = shlex.split(command)
    runner.invoke(cards.app, command)


def test_add(cards_db: cards.CardsDB):
    expected = cards.Card(summary='something', owner='', state='todo', id=1)
    cards_cli("add something")
    output = cards_db.list_cards()
    assert len(output) == 1
    assert output[0] == expected
