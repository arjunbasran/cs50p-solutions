import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/3") == 33

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge (30) == "30%"

def test_errors():
    with pytest.raises(ValueError):
        convert("-1/3")
    with pytest.raises(ValueError):
        convert("3/1")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")




