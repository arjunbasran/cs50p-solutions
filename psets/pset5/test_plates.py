from plates import is_valid

def test_length():
    assert is_valid("C") == False
    assert is_valid("CCCCCCC") == False

def test_startswith():
    assert is_valid("C1") == False

def test_0():
    assert is_valid("AA01") == False

def test_number_position():
    assert is_valid("AAA22A") == False

def test_punctuation():
    assert is_valid("AAA22!") == False



