import sys
from PIL import Image, ImageOps

ALLOWED = (".jpg", ".jpeg", ".png")

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1].lower()
    output_file = sys.argv[2].lower()

    if not input_file.endswith(ALLOWED) or not output_file.endswith(ALLOWED):
        sys.exit("Invalid input")

    if input_file.split(".")[-1] != output_file.split(".")[-1]:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(sys.argv[1]) as photo, Image.open("shirt.png") as shirt:
            resized = ImageOps.fit(photo, shirt.size)
            resized.paste(shirt, mask=shirt)
            resized.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()





