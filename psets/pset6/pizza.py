import csv
from tabulate import tabulate
import sys

if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

elif not (sys.argv[1]).endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        reader = csv.DictReader(f)
        print(tabulate(reader, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    print("File doesn't exist")
    sys.exit(1)
