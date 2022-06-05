import time

import pytest


@pytest.fixture(scope="session", autouse=True)
def get_session_time():
    yield
    curr_time = time.localtime()
    print(f'\n\nAll Tests completed at {time.strftime("%d %b %X", curr_time)}')
    print("---------------")


@pytest.fixture(scope='function', autouse=True)
def get_elapsed_time():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'\n\nCompleted in {elapsed_time} seconds')
    print("---------------")
