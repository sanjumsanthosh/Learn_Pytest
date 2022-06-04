from cards import Card


class TestEquality:
    def test_equality(self):
        c1 = Card("Summary", "test name", 'todo', 123);
        c2 = Card("Summary", "test name", 'todo', 123);
        assert c1 == c2

    def test_equality_with_diff_id(self):
        c1 = Card("Summary", "test name", 'todo', 123);
        c2 = Card("Summary", "test name", 'todo', 456);
        assert c1 == c2

    def test_inequality_(self):
        c1 = Card("Summary", "test name", 'todo', 123);
        c2 = Card("Summary", "test new name", 'todo', 456);
        assert c1 != c2
