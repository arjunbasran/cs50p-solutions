def Vowel_Remover(phrase):
    new_phrase = ""
    for char in phrase:
        if char.lower() not in "aeiou":
            new_phrase += char
    return new_phrase


string = input("Input: ")
new_phrase = Vowel_Remover(string)
print(f"Output: {new_phrase}")
