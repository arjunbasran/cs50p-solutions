import emoji

def main():

    while True:
        emoticon = input("Input: ")
        new = emoji.emojize(emoticon, language = "alias")

        if new == emoticon:
            print("Inccorect spelling of alias")
        else:
            print("Output: ", new)
            break

main()




