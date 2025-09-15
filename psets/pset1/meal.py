def main():
    time = input("What time is it? ")
    hour = convert(time)

    if 7 <= hour <= 8:
        print("breakfast time")
    elif 12 <= hour <= 13:
        print("lunch time")
    elif 18 <= hour <= 19:
        print("dinner time")


def convert(time):
    time = time.strip().upper()

    if ":" not in time:
        raise ValueError("Time must be in HH:MM format")

    elif time.endswith("AM") or time.endswith("PM"):
        is_pm = time.endswith("PM")
        time = time[:-2].strip()
    else:
        hour, minutes = map(int, time.split(":"))
        if hour < 0 or hour > 23 or minutes < 0 or minutes >= 60:
            raise ValueError ("Must enter a valid time")
        else:
            return hour + minutes / 60

    hour, minutes = map(int, time.split(":"))

    if hour < 1 or hour > 12 or minutes < 0 or minutes >= 60:
        raise ValueError("Invalid time")

    if hour == 12:
        hour = 0
    if is_pm:
        hour += 12

    return hour + minutes / 60


if __name__ == "__main__":
    main()



