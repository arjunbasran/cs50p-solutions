from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    dob_str = input("Date of Birth: ")
    try:
        dob = validate(dob_str) 
    except ValueError:
        sys.exit("Invalid date")

    minutes = time_diff(dob)
    words = p.number_to_words(minutes, andword="")
    print(f"{words.capitalize()} minutes")

def validate(date_of_birth: str) -> date:
    return date.fromisoformat(date_of_birth)

def time_diff(dob: date, today: date = None) -> int:
    if today is None:
        today = date.today()
    diff = today - dob
    return round(diff.total_seconds() / 60)

if __name__ == "__main__":
    main()

