import cards


def test_count(db_with_data: cards.CardsDB):
    assert db_with_data.count() == 4