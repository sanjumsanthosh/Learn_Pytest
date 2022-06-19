import shlex

import cards.cli as cli
import typer.testing

runner = typer.testing.CliRunner()


def test_typer_testing():
    result = runner.invoke(cli.app, ["version"])
    print(f'\n version: {result.stdout}')

    result = runner.invoke(cli.app, ["list", "-o", "sanju"])
    print(f'\n result of invoking list -o sanju \n {result.stdout}')


def card_cli(query: str):
    lex_split = shlex.split(query)
    result = runner.invoke(cli.app, lex_split)
    return result.stdout.rstrip()


def test_typer_testing_using_card_cli():
    result = card_cli("version")
    print(f'\n version: {result}')

    result = card_cli("list -o sanju")
    print(f'\n result of invoking list -o sanju \n {result}')
