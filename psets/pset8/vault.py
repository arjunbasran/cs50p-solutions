class Vault:
    def __init__(self, galleons=0, sickles=0):
        self.galleons = galleons
        self.sickles = sickles

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles"

    def  __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        return Vault(galleons, sickles)

potter = Vault(100, 50)
weasley = Vault(25, 50)
total = potter + weasley
print(total)

