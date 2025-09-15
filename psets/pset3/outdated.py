months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break

        elif "," in date:
            parts = date.split()
            if len(parts) != 3:
                continue

            month_name = parts[0]
            day = int(parts[1].replace(",", ""))
            year = int(parts[2])

            if month_name in months:
                month = months.index(month_name) + 1
                if 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break

    except (ValueError, IndexError):
        pass  











