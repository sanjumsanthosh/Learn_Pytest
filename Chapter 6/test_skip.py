import cards
import pytest


@pytest.mark.skip("Skipping this test for some reason :| ")
def test_skip():
    c1 = cards.Card("Test card 1", owner="New owner")
    c2 = cards.Card("Test card 2", owner="Great owner")
    assert c1 == c2
