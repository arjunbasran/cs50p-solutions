from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    fonts = figlet.getFonts()
    font = random.choice(fonts)
    figlet.setFont(font=font)

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    font = sys.argv[2]
    if font not in figlet.getFonts():
        sys.exit("Invalid font")
    figlet.setFont(font=font)

else:
    sys.exit("Usage: python figlet.py [-f FONT]")

text = input("Input: ")
print(figlet.renderText(text))







