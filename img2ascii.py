# img2ascii
# Take in an image file and convert it into ASCII art.

from PIL import Image

# The characters used to represent the gray scale images can be found here: http://paulbourke.net/dataformats/asciiart/
# ( .:-=+*#%@)
# ($@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. )

scale = {}


def create_scale(use_long: bool = False):
    short = " .:-=+*#%@"
    long = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

    # could probably use a comprehension of some sort here but this looks fine.

    if use_long:
        val = 0
        step = 255 / len(long)

        for char in long:
            scale[char] = val
            val += step

    else:
        val = 255
        step = 255 / len(short)

        for char in short:
            scale[char] = val
            val -= step


def pixel_to_ascii(pixel: int):

    char = min(scale, key=lambda k: abs(scale[k] - pixel))

    return char


def main():
    # Get image.
    img_name = input("Filename (/img/{filename}): ")
    with Image.open(f"./img/{img_name}") as image:
        image = image.convert("L")
        image = image.resize(size=(50, 50))
        width, height = image.size
        print(f"image {width=}, {height=}")
        px = image.load()

        with open("output.txt", "w") as file:
            for y in range(height):
                for x in range(width):
                    char = pixel_to_ascii(pixel=px[x, y])
                    print(char, end="")
                    file.write(char)
                print()
                file.write("\n")


if __name__ == "__main__":
    create_scale()
    main()
