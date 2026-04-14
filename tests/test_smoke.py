from mockapp.main import farewell, greet


def test_greet_returns_expected_text():
    assert greet() == "hello from mockapp"


def test_farewell_returns_expected_text():
    assert farewell() == "goodbye from mockapp"
