def main():

    string = input("Input: ")
    new_phrase = shorten(string)
    print(f"Output: {new_phrase}")


def shorten(word):
    new_phrase = ""
    for char in word:
        if char.lower() not in "aeiou":
            new_phrase += char
    return new_phrase

if __name__ == "__main__":
    main()
