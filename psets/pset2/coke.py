Am_D = 50

while Am_D > 0:
    print(f"Amount Due: {Am_D}")
    coin = int(input("Insert Coin: "))

    if coin == 25:
        Am_D-=25

    elif coin == 10:
        Am_D-=10

    elif coin == 5:
        Am_D-=5

if Am_D <= 0:
    change_owed = Am_D * -1
    print(f"Change Owed: {change_owed}")







