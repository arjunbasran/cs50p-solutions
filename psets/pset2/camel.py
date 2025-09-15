def camel_to_snake(name):
    snake = ""
    for char in name:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake

camel = input("camelCase: ")
snake = camel_to_snake(camel)
print(f"snake_case: {snake}")


