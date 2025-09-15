import random

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1:
                return level
            elif level == 2:
                return level
            elif level == 3:
                return level
            else:
                continue


        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)

    elif level == 2:
        return random.randint(10, 99)

    else:
        return random.randint(100, 999)

def ask(x, y):
    correct_answer = x + y
    for _ in range(3):
        try:
            ans = int(input(f"{x} + {y} = "))

        except ValueError:
            print("EEE")
            continue

        if ans == correct_answer:
            return True
        else:
            print("EEE")

    print(f"{x} + {y} = {correct_answer}")
    return False

def main():

    lvl = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        if ask(x, y):
            score += 1

    print(f"Score: {score}")

if __name__ == "__main__":
    main()







