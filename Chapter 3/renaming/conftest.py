import pytest


@pytest.fixture(name="random_number")
def random_number_fixture():
    return 42
