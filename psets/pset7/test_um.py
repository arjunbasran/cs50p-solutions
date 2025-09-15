from um import count

def test_case_insensitivity():
    assert count("Um uM UM") == 3

def test_um_in_word():
    assert count("Um, thanks for the album") == 1

def test_punctuation():
    assert count("Um?") == 1

