from twttr import shorten

def test_vowel_removal():
    assert shorten("hello") == "hll"


def test_case_insensitivity():
    assert shorten("Phrase") == "Phrs"
    assert shorten("HELLO") == "HLL"

def test_number_input():
    assert shorten("37828") == "37828"

def test_punctuation():
    assert shorten("Hel,lo") == "Hl,l"



