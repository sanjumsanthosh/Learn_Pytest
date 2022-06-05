import cards
import pytest

pytestmark = pytest.mark.finish


@pytest.mark.smoke
class TestFinish:
    def test_finish_from_todo(self, cards_db: cards.CardsDB):
        indx = cards_db.add_card(cards.Card("foo", state="todo"))
        cards_db.finish(indx)
        assert cards_db.get_card(indx).state == "done"

    def test_finish_from_in_prog(self, cards_db: cards.CardsDB):
        indx = cards_db.add_card(cards.Card("foo", state="in prog"))
        cards_db.finish(indx)
        assert cards_db.get_card(indx).state == "done"

    def test_finish_from_done(self, cards_db: cards.CardsDB):
        indx = cards_db.add_card(cards.Card("foo", state="done"))
        cards_db.finish(indx)
        assert cards_db.get_card(indx).state == "done"


@pytest.mark.parametrize("start_state", [
    "todo",
    pytest.param("in prog", marks=pytest.mark.smoke),
    "done"
])
def test_finish_function(cards_db, start_state: str):
    indx = cards_db.add_card(cards.Card("foo", state=start_state))
    cards_db.finish(indx)
    assert cards_db.get_card(indx).state == "done"


@pytest.fixture(params=[
    "todo",
    pytest.param("in prog", marks=pytest.mark.smoke),
    "done"
])
def start_state_fixture(request):
    return request.param


def test_finish_fix(cards_db: cards.CardsDB, start_state_fixture: str):
    indx = cards_db.add_card(cards.Card("Test summary", start_state_fixture))
    cards_db.finish(indx)
    assert cards_db.get_card(indx).state == "done"
