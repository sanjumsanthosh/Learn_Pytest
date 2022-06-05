import cards
import pytest


@pytest.mark.xfail()
def test_surely_fail():
    c1 = cards.Card("Summary", "test name")
    c2 = cards.Card("Summary", "test name")
    assert c1 > c2


@pytest.mark.xfail()
def test_will_pass():
    c1 = cards.Card("Summary", "test name")
    c2 = cards.Card("Summary", "test name")
    assert c1 == c2


@pytest.mark.xfail(strict=True)
def test_will_pass_but_make_it_fail():
    c1 = cards.Card("Summary", "test name")
    c2 = cards.Card("Summary", "test name")
    assert c1 == c2
