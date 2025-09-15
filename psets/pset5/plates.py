def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False

    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
            if s[i] == "0":
                return False
            break

    return True

if __name__ == "__main__":
    main()
