import emoji

class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("invalid capacity")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        cookie = emoji.emojize(":cookie:", language = "alias")
        return cookie * self._cookies

    def deposit(self, n):
        if n < 0:
            raise ValueError("must be positive number")
        self._cookies += n
        if self._cookies > self._capacity:
            raise ValueError("exceeding capacity")

    def withdraw(self, n):
        if n < 0:
            raise ValueError("must be positive number")
        self._cookies -= n
        if self._cookies < 0:
            raise ValueError("can't have negative amount of cookies")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies

def main():
    try:
        cap = int(input("Enter size of your cookie jar: "))
    except ValueError:
        print("must be an integer")
        return

    jar = Jar(cap)

    print(jar.capacity)
    print(jar.size)
    print(jar)
    jar.deposit(8)
    print(jar)
    jar.withdraw(5)
    print(jar)
    print(jar.size)

if __name__ == "__main__":
    main()







