import pytest


@pytest.fixture()
def some_data():
    return 10


def test_some_data(some_data):
    """Using fixtures"""
    assert some_data == 10
