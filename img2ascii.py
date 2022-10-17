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

    ascii = min(scale, key=lambda k: abs(scale[k] - pixel))

    return ascii


def main(to_file: bool = False):
    # Get image.
    img_name = input("Filename (/img/{filename}): ")
    with Image.open(f"./img/{img_name}") as image:
        image = image.convert("L")
        image = image.resize(size=(50, 50))
        width, height = image.size
        print(f"image {width=}, {height=}")
        px = image.load()

        if to_file:
            with open("output.txt", "w") as file:
                for x in range(width):
                    for y in range(height):
                        file.write(pixel_to_ascii(pixel=px[y, x]))
                    file.write("\n")
        else:

            for y in range(height):
                for x in range(width):
                    # print(f"({x=}, {y=})", end="")
                    print(pixel_to_ascii(pixel=px[x, y]), end="")
                print()


if __name__ == "__main__":
    create_scale()
    resp = input("Write to output.txt? (y/n)")
    main(to_file=(resp == "y"))
