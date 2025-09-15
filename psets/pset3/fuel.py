while True:
    try:
        fuel = input("Fraction: ")
        x, y = fuel.split("/")
        x = int(x)
        y = int(y)
        if x > y or x < 0 or y < 0:
            raise ValueError
        percentage = round((x/y)*100)
        break
    except (ValueError, ZeroDivisionError):
        pass

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")






