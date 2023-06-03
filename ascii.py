from PIL import Image, ImageDraw, ImageFont
import sys

# We need a function the maps an intensity value (i.e., a colour value of 0 - 255 inclusive), to an ASCII character.
global ascii_chars
ascii_chars = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"

def colour_to_ascii(colour: int) -> str:
    match colour:
        case _ if colour < 10:
            return 
    

#if __name__ == "__main__":
    


