import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"(?i)(?<![A-Za-z])um(?![A-Za-z])"
    return len(re.findall(pattern, s, flags=re.IGNORECASE))


if __name__ == "__main__":
    main()
