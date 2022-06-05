
def test_tmp_path(tmp_path):
    s = "Some random text"
    file = tmp_path / "file.txt"
    file.write_text(s)
    assert file.read_text() == s
