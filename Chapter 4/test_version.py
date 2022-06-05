import subprocess

import cards.cli
import typer.testing


def test_version_v1():
    process = subprocess.run(
        ['cards', 'version'],
        capture_output=True,
        text=True
    )
    output = process.stdout.rstrip('\n')
    assert output == cards.__version__


def test_version_v2(capsys):
    cards.cli.version()
    result = capsys.readouterr()
    output = result.out.rstrip('\n')
    assert output == cards.__version__


# using typer.testing.CliRunner for testing the package
def test_version_v3():
    runner = typer.testing.CliRunner()
    result = runner.invoke(cards.app, ["version"])
    output = result.output.rstrip('\n')
    assert output == cards.__version__
