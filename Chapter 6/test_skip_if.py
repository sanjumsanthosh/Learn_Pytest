import cards
import pytest


@pytest.mark.skipif(cards.__version__ == "1.0.0", reason=f"Option not supported in {cards.__version__}")
def test_skip_if():
    c1 = cards.Card("Some one ", "some owner")
    c2 = cards.Card("Some two ", "some owner")
    assert c2 > c1
