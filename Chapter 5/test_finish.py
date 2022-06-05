import cards


def test_finish_from_todo(cards_db: cards.CardsDB):
    index = cards_db.add_card(cards.Card("New test card", state="todo"))
    cards_db.finish(index)
    assert cards_db.get_card(index).state == "done"


def test_finish_from_in_prog(cards_db: cards.CardsDB):
    index = cards_db.add_card(cards.Card("New test card", state="in prog"))
    cards_db.finish(index)
    assert cards_db.get_card(index).state == "done"


def test_finish_from_done(cards_db: cards.CardsDB):
    index = cards_db.add_card(cards.Card("New test card", state='done'))
    cards_db.finish(index)
    assert cards_db.get_card(index).state == "done"


def test_grouped(cards_db: cards.CardsDB):
    test_groups = [
        cards.Card("New card", state="todo"),
        cards.Card("New card", state="in prog"),
        cards.Card("New card", state="done"),
    ]
    for card in test_groups:
        index = cards_db.add_card(card)
        cards_db.finish(index)
        assert cards_db.get_card(index).state == "done"
