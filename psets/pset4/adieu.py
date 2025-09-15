import inflect

p = inflect.engine()
namelist = []

try:
    while True:
        name = input().strip()
        if not name:
            continue
        namelist.append(name)
except EOFError:
    pass

print(f"Adieu, adieu, to {p.join(namelist)}")





