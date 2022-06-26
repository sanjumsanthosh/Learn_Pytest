import typer.testing
import hello

runner = typer.testing.CliRunner()


def test_hello_default():
    result = runner.invoke(hello.app)
    assert result.stdout == "Hello, World !\n"


def test_hello_name():
    result = runner.invoke(hello.app, ["Sanju"])
    assert result.stdout == "Hello, Sanju !\n"
