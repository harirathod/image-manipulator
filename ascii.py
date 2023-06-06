# The purpose of using PIL, is because I want to calculate the darkness of each ASCII character,
from PIL import Image, ImageDraw, ImageFont
# from matplotlib import font_manager -> Was used for finding locations of system fonts.
import sys
import string
import math
from numpy import uint8

# We need a function the maps an intensity value (i.e., a colour value of 0 - 255 inclusive), to an ASCII character.
# Probably have a dictionary of intensity to ASCII characters. We could have 10 ASCII characters.




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

def get_ascii_chars(step: int = 10, font: str = 'Courier.ttc') -> list:
    """
    Get a list of ASCII characters including, letters, digits and punctuation, ordered by ascending darkness ratios.
    The step determines the spread of the returned ASCII characters. A step of 1 returns all ASCII characters.
    A step of 10 returns the 0th ASCII char in the list sorted by darkness, then the 9th, then the 19th, etc."""

    # For each ASCII character, put it in a map of 'ascii_char: darkness'.
    ascii_chars = string.ascii_letters + string.punctuation + string.digits + ' '
    map = {}
    for ascii in ascii_chars:
         map.update({ascii: get_darkness(ascii, font=font)})

    # Order the dictionary by darkness value.
    sorted_ascii = sorted(map, key=map.get)[::step] # TODO: We haven't checked the darkness values properly. The last two ascii chars may be very close in darkness values. Instead, we should scale the dictionary of darkness to 0.9999 as the max, and get chars for 0.0, 0.1, 0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9.
    sorted_ascii.reverse()
    return sorted_ascii

def colour_to_ascii(luminosity: uint8) -> str:
    """
    Takes a luminosity value, in the range 0 to 255, and returns an ASCII character representing that luminosity.
    """
    if luminosity == 255:
        luminosity -= 1

    # Using global chars, rather than making a call to get_ascii_chars(), massively improves performance.
    global ascii_chars
    index = math.floor((luminosity / 255) * len(ascii_chars))
    return ascii_chars[index]

global ascii_chars
ascii_chars = get_ascii_chars(8)

# Main function. If run as a script, the second argument is used as the parameter of get_darkness(), and the darkness ratio is calculated.
if __name__ == "__main__":
    if len(sys.argv) > 1:
        darkness_ratio = get_darkness(sys.argv[1])
        print(f'Darkness ratio of {sys.argv[1]} is: {darkness_ratio}')
    print(ascii_chars)
    
    