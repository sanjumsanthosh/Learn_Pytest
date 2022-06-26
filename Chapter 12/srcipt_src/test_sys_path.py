import sys


def test_sys_paths():
    print("System paths are : ")
    for path in sys.path:
        print(path)
