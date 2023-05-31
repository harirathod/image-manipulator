
# Need to read over
import cv2 as cv
import numpy as np
import sys


def convert_image_to_grayscale(image_path: str) -> np.ndarray:
    """
    Converts a coloured image to grayscale image.
    Takes an image path of a coloured image, and converts it to a grayscale version of the image, represented as a 
    as a two-dimensional np.ndarray.

    @param image_path The path of the image.
    @throws FileNotFoundException If the image could not be read.
    @return The grayscale image, represented as a two-dimensional array (np.ndarray).
    """
    image = cv.imread(image_path, cv.IMREAD_UNCHANGED)

    if image is None:
         raise FileNotFoundError(f'Image \'{image_path}\' could not be found.')
    if image.ndim < 3:
        raise Exception("Image should already be grayscale.")
    # An image with ndim of 3 has width x, height y, and each pixel in the third-dimension is composed of 3 rgb colours.
    # To convert the image to grayscale, we need to give each pixel a new rgb value, where the new rgb value  = (r + g + b) / 3.
    # As the new r = g = b, the pixel is grey.
    temp = np.mean(image, axis=2).astype('uint8')
    return temp

def display_image(image: np.ndarray, title_of_window: str = "My Image") -> str:
    """
    Displays the image in a window.
    
    The window closes once the user presses any key."""
    cv.imshow(title_of_window, image)
    # Display the image until the user presses any key, upon which the image should close.
    cv.waitKey(0)

def save_image(image: np.ndarray, name_of_image: str = "my-edited-image.jpg") -> None:
    cv.imwrite(filename=name_of_image, img=image)

image = convert_image_to_grayscale(sys.argv[1])
display_image(image)
save_image(image)