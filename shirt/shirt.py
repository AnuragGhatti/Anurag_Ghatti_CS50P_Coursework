import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = {".jpg", ".jpeg", ".png"}

    input_ext = "." + input_file.rsplit(".", 1)[-1].lower() if "." in input_file else ""
    output_ext = "." + output_file.rsplit(".", 1)[-1].lower() if "." in output_file else ""

    if input_ext not in valid_extensions:
        sys.exit("Invalid input")
    if output_ext not in valid_extensions:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        input_image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size

    input_image = ImageOps.fit(input_image, size)
    input_image = input_image.convert("RGBA")  # ensure alpha channel exists
    input_image.paste(shirt, mask=shirt)
    input_image = input_image.convert("RGB")   # convert back for JPEG saving
    input_image.save(output_file)

main()
