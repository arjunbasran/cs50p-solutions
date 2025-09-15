import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'<iframe src="https?://(?:www\.)?youtube\.com/embed/xvFZjo5PgG0".*></iframe>'
    if re.search(pattern, s):
        return "https://youtu.be/xvFZjo5PgG0"

if __name__ == "__main__":
    main()

