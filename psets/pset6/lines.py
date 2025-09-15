import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

elif not sys.argv[1].endswith(".py"):
    print("Not a Python file")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        length = 0
        for line in f:
            stripped = line.strip()
            if stripped == "":
                continue
            if stripped.startswith("#"):
                continue
            length += 1
        print(length)

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)






