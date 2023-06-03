from PIL import Image, ImageDraw, ImageFont
import sys

# We need a function the maps an intensity value (i.e., a colour value of 0 - 255 inclusive), to an ASCII character.
global ascii_chars
ascii_chars = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"

def colour_to_ascii(colour: int) -> str:
    match colour:
        case _ if colour < 10:
            return 

# The purpose of using PIL, is because I want to calculate the darkness of each ASCII character,

def get_darkness(text: str) -> float:
    """
    Get the darkness value of a character as a decimal between 0 and 1. 0 represents no darkness.
    For example, ' ' (the space character) has no darkness.
    """

    font = ImageFont.truetype('Courier New.ttf', 30)

    # Get the box dimensions of the text, from which, we can calculate the size of the text.
    size = font.getsize(text)

    # Create a grayscale image.
    image = Image.new('1', (size), 2)
    
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text=text, font=font) # Render the text to the bitmap
    image.save('text.png')

    for rownum in range(image.size[1]):
        line = []
        for colnum in range(image.size[0]):
            if image.getpixel((colnum, rownum)): line.append(' .'),
            else: line.append(' #'),
        print (''.join(line))


    # Count the number of pixels taken up by the text in its 'bounding box'.
    pixel_count = [0]
    for column in range(image.size[0]):
        for row in range(image.size[1]):
            if image.getpixel((column, row)) == 0:
                pixel_count[0] += 1
            
    return pixel_count[0] / (image.size[0] * image.size[1])


if __name__ == "__main__":
    print(get_darkness(sys.argv[1]))