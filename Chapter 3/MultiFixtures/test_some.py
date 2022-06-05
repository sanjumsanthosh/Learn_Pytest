import cards


def test_multiple_1(card_db: cards.CardsDB, test_cards: list[cards.Card]):
    for card in test_cards:
        card_db.add_card(card)

    assert card_db.count() == len(test_cards)


def test_multiple_2(test_card_db: cards.CardsDB):
    assert test_card_db.count() > 0
