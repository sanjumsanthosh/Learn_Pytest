import cards


def test_initial_empty(card_db: cards.CardsDB):
    assert card_db.count() == 0


def test_count(card_db: cards.CardsDB):
    card_db.add_card(cards.Card("card 1"))
    card_db.add_card(cards.Card("card 2"))
    card_db.add_card(cards.Card("card 3"))
    assert card_db.count() == 3
