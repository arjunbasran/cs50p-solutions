def main():
    while True:
        try:
            s = input("Fraction: ")
            pct = convert(s)
            print(gauge(pct))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x_str, y_str = fraction.split("/")
    x = int(x_str)
    y = int(y_str)

    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0 or x > y:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()


