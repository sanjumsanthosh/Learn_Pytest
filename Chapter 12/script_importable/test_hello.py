import _pytest.capture

import hello


def test_importable_hello(capsys: _pytest.capture.CaptureFixture):
    hello.main()
    output = capsys.readouterr().out
    assert output == "Hello World\n"
