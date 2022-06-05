def print_dummy():
    print("dummy 1")
    print("dummy 2")
    print("dummy 3")


def test_normal_out():
    print_dummy()


def test_capsys_disabled(capsys):
    with capsys.disabled():
        print_dummy()
