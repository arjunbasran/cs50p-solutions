from working import convert
import pytest

def test_basic():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_with_minutes():
    assert convert("9:30 AM to 5:15 PM") == "09:30 to 17:15"

def test_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

def test_without_to():
    with pytest.raises(ValueError):
        convert("9:30 AM 5 PM")



