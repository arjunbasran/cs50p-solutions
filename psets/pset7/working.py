import re
import sys

def main():
    s = input("Hours: ")
    print(convert(s))

def convert(s):
    pattern = r"(\d{1,2})(?::([0-5]\d))? (AM|PM) to (\d{1,2})(?::([0-5]\d))? (AM|PM)"
    m = re.fullmatch(pattern, s, flags = re.IGNORECASE)
    if not m:
        raise ValueError("invalid format")

    sh, sm, sampm, eh, em, eampm = m.groups()

    sh = int(sh)
    eh = int(eh)
    sm = int(sm) if sm is not None else 0
    em = int(em) if em is not None else 0
    sampm = sampm.upper()
    eampm = eampm.upper()

    if not (1 <= sh <= 12) or not (1 <= eh <= 12):
        raise ValueError("Hour out of range")

    sH24 = _to24(sh, sampm)
    eH24 = _to24(eh, eampm)

    return f"{sH24:02d}:{sm:02d} to {eH24:02d}:{em:02d}"


def _to24(hour: int, meridiem: str) -> int:
    if meridiem == "AM":
        return 0 if hour == 12 else hour
    else:
        return 12 if hour == 12 else hour + 12


if __name__ == "__main__":
    main()
