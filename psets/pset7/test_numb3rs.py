from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") is True
    assert validate("8.8.8.8") is True
    assert validate("255.255.255.255") is True

def test_out_of_range_octet_not_first():
    assert validate("1.2.3.256") is False
    assert validate("10.10.300.10") is False

def test_wrong_count():
    assert validate("1.2.3") is False
    assert validate("10.10.10.10.10") is False

def test_nondigits():
    assert validate("1.2.3.a") is False
    assert validate("-1.2.3.4") is False


