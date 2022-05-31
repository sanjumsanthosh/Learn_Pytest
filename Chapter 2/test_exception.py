import cards
import pytest

Regex_arg_error = "missing .* arguments"


def test_no_path_raise_exception():
    with pytest.raises(TypeError):
        cards.DB()


def test_raise_with_info():
    with pytest.raises(TypeError) as error:
        cards.DB()
    expected = "missing 2 required positional arguments"
    assert expected in str(error.value)


def test_raise_with_regex():
    with pytest.raises(TypeError, match=Regex_arg_error):
        cards.DB();


if __name__ == "__main__":
    test_no_path_raise_exception()
    test_raise_with_regex()
    test_raise_with_info()