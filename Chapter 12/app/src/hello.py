import typing

import typer

app = typer.Typer()


def full_output(name: str):
    return f"Hello, {name} !"


@app.command()
def main(name: typing.Optional[str] = typer.Argument("World")):
    print(full_output(name))


if __name__ == "__main__":
    app()
