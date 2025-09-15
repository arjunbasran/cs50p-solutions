import random

def main():

    level = get_level()
    a = random.randint(1,level)

    while True:
        guess = get_guess()
        if guess > a:
            print("Too large!")
        elif guess < a:
            print("Too small!")
        elif guess == a:
            print("Just right!")
            break

def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if l > 0:
                return l

        except ValueError:
            continue

def get_guess():
    while True:
        try:
            g = int(input("Guess: "))
            if g > 0:
                return g

        except ValueError:
            continue

main()
