import cards
import faker.proxy
import pytest


@pytest.fixture(scope="session")
def db(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("Cards_db")
    db = cards.CardsDB(tmp_dir)
    yield db
    db.close()


@pytest.fixture()
def cards_db(db: cards.CardsDB):
    db.delete_all()
    return db


@pytest.fixture()
def cards_db_init(cards_db: cards.CardsDB, request, faker:faker.proxy.Faker):
    m = request.node.get_closest_marker("num_cards")
    faker.seed_instance(101)
    if m and len(m.args) > 0 and m.args[0] > 0:
        for i in range(m.args[0]):
            cards_db.add_card(cards.Card(
                summary=faker.sentence(),
                owner=faker.first_name()
            ))
    return cards_db
