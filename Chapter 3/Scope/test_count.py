import cards


def test_initial_empty(card_db: cards.CardsDB):
    assert card_db.count() == 0


def test_two_count(two_count_db: cards.CardsDB):
    assert two_count_db.count() == 2


def test_four_count(four_count_db: cards.CardsDB):
    assert four_count_db.count() == 4
