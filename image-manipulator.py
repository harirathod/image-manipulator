
# Need to read over
import cv2 as cv
import numpy as np
import sys


def convertImageToGrayscale(image_path: str) -> np.ndarray:
    """
    Converts a coloured image to grayscale image.
    Takes an image path of a coloured image, and converts it to a grayscale version of the image, represented as a 
    as a two-dimensional np.ndarray.

    @param image_path The path of the image.
    @throws FileNotFoundException If the image could not be read.
    @return The grayscale image, represented as a two-dimensional array (np.ndarray).
    """
    image = cv.imread(image_path)
    if image is None:
         raise FileNotFoundError(f'Image \'{image_path}\' could not be read.')
    if image.ndim < 3:
        raise Exception("Image should already be grayscale.")
    # An image with ndim of 3 has width x, height y, and each pixel in the third-dimension is composed of 3 rgb colours.
    # To convert the image to grayscale, we need to give each pixel a new rgb value, where the new rgb value  = (r + g + b) / 3.
    # As the new r = g = b, the pixel is grey.
    temp = np.mean(image, axis=2).astype('uint8')
    return temp

def display_image(image: np.ndarray) -> None:
    cv.imshow("My Image", image)

