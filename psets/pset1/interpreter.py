expression = input("Expression: ")

x, y, z = expression.split(" ")
x = int(x)
z = int(z)

if y == "+":
    answer = x + z
elif y == "-":
    answer = x - z
elif y == "*":
    answer = x * z
elif y == "/":
    answer = x / z
else:
    print("redo in correct format!")

print(f"{answer:.1f}")


