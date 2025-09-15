from jar import Jar


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    assert str(jar) == "🍪🍪🍪"

    jar.deposit(2)
    assert jar.size == 5

    try:
        jar.deposit(1)
        assert False
    except ValueError:
        assert True


def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    assert jar.size == 4

    jar.withdraw(2)
    assert jar.size == 2
    assert str(jar) == "🍪🍪"

    try:
        jar.withdraw(5)
        assert False
    except ValueError:
        assert True
