def energy_mass_equivalence(mass):
    c = 300000000
    E = mass*c*c
    return E

def main():
    mass = int(input("Enter mass value: "))
    print(energy_mass_equivalence(mass))

main()




