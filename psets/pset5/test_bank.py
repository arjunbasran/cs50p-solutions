from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("hello friend") == 0

def test_case_insensitivity():
    assert value("HElLo") == 0
    assert value("hi") == 20
    assert value("HEY") == 20

def test_whitespace():
    assert value("      Hello") == 0
