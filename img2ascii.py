# img2ascii
# Take in an image file and convert it into ASCII art.

from PIL import Image
import argparse

# The characters used to represent the gray scale images can be found here: http://paulbourke.net/dataformats/asciiart/
# ( .:-=+*#%@)
# ($@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. ) Short looks way better than long, but the option will be there in case someone wants it.


# Arguments for running in command line.
parser = argparse.ArgumentParser(description="Turn an image into ASCII art.")
parser.add_argument(
    "scale",
    default="short",
    const="short",
    nargs="?",
    type=str,
    choices=["short", "long"],
    help="Scale to be used. Either scale will use different characters.",
)
parser.add_argument(
    "--flip",
    action="store_true",
    help="Flips scale when converting grayscale to ASCII.",
)


def create_scale(scale_type: str = "short", flip: bool = False):
    if scale_type == "short":
        chars = " .:-=+*#%@"
    elif scale_type == "long":
        chars = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    scale = {}
    val = 255  # white = ' ', black = '@'
    step = -(255 // len(chars))

    if flip:  # This will make white == "@" and black == " "
        val = 0
        step = abs(step)

    for char in chars:
        scale[char] = val
        val += step
    
    return scale


def pixel_to_ascii(pixel: int, scale):
    char = min(scale, key=lambda k: abs(scale[k] - pixel))
    return char


def convert(scale_type: str = "short", flip: bool = False):
    # Create scale
    scale = create_scale(scale_type, flip)
    # Get image.
    img_name = input("Filename (/img/{filename}): ")
    with Image.open(f"./img/{img_name}") as image:
        image = image.convert("L")
        image = image.resize(size=(100, 100))
        width, height = image.size
        print(f"image {width=}, {height=}")
        px = image.load()

        with open("output.txt", "w") as file:
            for y in range(0, height, 2): # Sample half the height, due to the aspect ratio of the characters
                for x in range(width):
                    char = pixel_to_ascii(pixel=px[x, y], scale=scale)
                    print(char, end="")
                    file.write(char)
                print()
                file.write("\n")

    print("Done!")


if __name__ == "__main__":
    args = parser.parse_args()
    print(args.scale, args.flip)
    convert(args.scale, args.flip)
