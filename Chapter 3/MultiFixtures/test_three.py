import cards


def test_three(card_db: cards.CardsDB):
    card_db.add_card(cards.Card("card1"))
    card_db.add_card(cards.Card("card2"))
    card_db.add_card(cards.Card("card3"))
    assert card_db.count() == 3
