# The purpose of using PIL, is because I want to calculate the darkness of each ASCII character,
from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
import sys
import string

# We need a function the maps an intensity value (i.e., a colour value of 0 - 255 inclusive), to an ASCII character.
# Probably have a dictionary of intensity to ASCII characters. We could have 10 ASCII characters.
global ascii_chars
ascii_chars = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"



def get_darkness(text: str, font: str = 'Courier.ttc') -> float:
    """
    Get the darkness value of text as a decimal between 0 and 1. A value of 0 represents no darkness.
    For example, ' ' (the space character) has no (0) darkness. Should ideally be used with characters e.g., 'h' and 'i' as opposed to 'hi'.

    The darkness is typically font specific.

    @param text The text we want to find the darkness of.
    @param font The font of the text.
    @return The darkness ratio of the text.
    """

    font = ImageFont.truetype(font=font, size=40)

    # Get the box dimensions of the text, from which, we can calculate the size of the text.
    size = font.getbbox(text)

    # Create a grayscale image. Used size(right, bottom) for (width, height) in Image.new(size=).
    image = Image.new('1', (size[2], size[3]), 1)
    draw = ImageDraw.Draw(image)

    # Render the text to the bitmap
    draw.text((0, 0), text=text, font=font)

    # Count the number of pixels taken up by the text in its 'bounding box'.
    pixel_count = [0]
    for column in range(image.size[0]):
        for row in range(image.size[1]):
            if image.getpixel((column, row)) == 0:
                pixel_count[0] += 1
    return pixel_count[0] / ((image.size[0]) * image.size[1])


# Main function. If run as a script, the second argument is used as the parameter of get_darkness(), and the darkness ratio is calculated.
if __name__ == "__main__":
    darkness_ratio = get_darkness(sys.argv[1])
    print(darkness_ratio)

    
    # For each ASCII character, put it in a map of 'ascii_char: darkness'.
    ascii_chars = string.ascii_letters + string.punctuation + string.digits + ' '
    map = {}
    for ascii in ascii_chars:
         map.update({ascii: get_darkness(ascii)})

    # Order the dictionary by darkness value.
    sorted_ascii = sorted(map, key=map.get)[::10]
    print(sorted_ascii)
    print(len(sorted_ascii))

    