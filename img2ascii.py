# img2ascii
# Take in an image file and convert it into ASCII art.

from PIL import Image

# The characters used to represent the gray scale images can be found here: http://paulbourke.net/dataformats/asciiart/
# ( .:-=+*#%@)

scale = {" ": 0, ".": 55, ":":80, "-":105, "=":130, "+":155, "*":180, "#":205, "%":230, "@":255}

def pixel_to_ascii(pixel: int):
    
    ascii = min(scale, key=lambda k: abs(scale[k] - pixel))

    return ascii

def main():
    # Get image.
    img_name = input("Filename (/img/{filename}): ")
    with Image.open(f"./img/{img_name}") as image:
        image = image.convert("L")
        image = image.resize(size=(100, 100))
        width, height = image.size
        px = image.load()

        with open('output.txt', 'w') as file:
            for x in range(width):
                for y in range(height):
                    print(pixel_to_ascii(pixel=px[y, x]), end = '')
                    # file.write(pixel_to_ascii(pixel=px[y, x]))
                # file.write('\n')
                print()

if __name__ == "__main__":
    main()