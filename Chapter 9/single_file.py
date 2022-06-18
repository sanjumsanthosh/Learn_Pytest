# Testing a simple 2 number calculator

def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def div(num1, num2):
    return num1 / num2


def mul(num1, num2):
    return num1 * num2


def main():  # pragma: no cover
    sample_num1 = 100
    sample_num2 = 10
    print("num1 : ", sample_num1, ", num2 : ", sample_num2)
    print("addition : ", add(sample_num1, sample_num2))
    print("subtraction : ", sub(sample_num1, sample_num2))
    print("division : ", div(sample_num1, sample_num2))
    print("multiplication : ", mul(sample_num1, sample_num2))


if __name__ == "__main__":
    main()
else:
    import pytest


# Test cases

def test_add():
    s1 = 10
    s2 = 20
    assert add(s1, s2) == 30


def test_sub():
    s1 = 10
    s2 = 20
    assert sub(s1, s2) == -10


def test_mul():
    s1 = 10
    s2 = 20
    assert mul(s1, s2) == 200


def test_div():
    s1 = 10
    s2 = 20
    assert div(s1, s2) == 0.5
