import pytest
from datetime import date
from seasons import validate, time_diff

def test_validate_invalid():
    with pytest.raises(ValueError):
        validate("2021-03-36")
    with pytest.raises(ValueError):
        validate("2021-13-21")
    with pytest.raises(ValueError):
        validate("February 6th, 1998") 

def test_time_diff():
    today = date(2025, 9, 2)
    assert time_diff(date(2025, 9, 2), today) == 0
    assert time_diff(date(2025, 9, 1), today) == 1440
    assert time_diff(date(2025, 8, 31), today) == 2880




