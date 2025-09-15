import re

def main():
    ip = input("IPv4 Address: ").strip()
    print(validate(ip))

def validate(ip):
    pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    if re.search(pattern, ip):
        parts = ip.split(".")
        for part in parts:
            if not part.isdigit():
                return False
            n = int(part)
            if not (0 <= n <= 255):
                return False
            if part != "0" and part.startswith("0"):
                return False
        return True
    return False

if __name__ == "__main__":
    main()


