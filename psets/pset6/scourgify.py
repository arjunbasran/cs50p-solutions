import csv
import sys

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

try:
    with open (sys.argv[1]) as inp, open(sys.argv[2], "w", newline="") as outp:
        reader = csv.DictReader(inp)
        writer = csv.DictWriter(outp, fieldnames= ["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            last, first = [part.strip() for part in row["name"].split(",", 1)]
            clean = {"first": first, "last": last, "house": row["house"]}
            writer.writerow(clean)

except FileNotFoundError:
    print("File not found")
    sys.exit(1)
