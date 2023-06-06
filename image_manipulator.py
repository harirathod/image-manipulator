import cv2 as cv
import numpy as np
from image_exceptions import InvalidImageMatrixException
import sys
import ascii

def get_image_from_path(image_path: str) -> np.ndarray:
    """
    Takes the path of an image, and returns a matrix (ndarray) representing
    that image.
    
    @param image_path The path of the image.
    @throws FileNotFoundException If the image could not be read.
    @return The image, represented by a matrix.
    """

    image = cv.imread(image_path, cv.IMREAD_UNCHANGED)
    if image is None:
        raise FileNotFoundError(f'Image \'{image_path}\' could not be found')
    return image

def convert_image_to_greyscale(image: np.ndarray) -> np.ndarray:
    """
    Converts a coloured image to greyscale image.
    Takes a matrix (three-dimensional np.ndarray) representing a coloured image, and converts it to a greyscale version of the image (as a two-dimensional np.ndarray).
    This method does not modify the original image array. It returns a copy.

    @param image The matrix representing the image. If the matrix does not represent an image correctly, i.e., if it is four-dimensional, then this method will throw an error.
    @throws InvalidImageMatrixException If the dimensions of the matrix are less than 3.
    @return The greyscale image, represented as a two-dimensional array (np.ndarray).
    """

    if image.ndim < 3:
        raise InvalidImageMatrixException(f"Image should already be greyscale, as it only has {image.ndim} dimensions")
    # An image with ndim of 3 has width x, height y, and each pixel in the third-dimension is composed of 3 rgb colours.
    # To convert the image to greyscale, we need to give each pixel a new rgb value, where the new rgb value  = (r + g + b) / 3.
    # As the new r = g = b, the pixel is grey.
    temp = np.mean(image, axis=(image.ndim - 1)).astype(image.dtype)
    return temp

def display_image(image: np.ndarray, title_of_window: str = "My Image") -> str:
    """
    Displays the image in a window.
    The window closes once the user presses any key.

    @param image The image, as a matrix, to be displayed.
    @param title_of_window The title of the display window.
    @throws InvalidImageMatrixexception if an invalid image matrix is provided. I.e., if it doesn't have an ndim of 3 or less.
    """
    try:
        cv.imshow(title_of_window, image)
    except cv.error as err:
        raise InvalidImageMatrixException("Invalid image matrix provided")
    # Display the image until the user presses any key, upon which the image should close.
    cv.waitKey(0)

def save_image(image: np.ndarray, name_of_file: str = "my-edited-image.jpg") -> None:
    """
    Saves the image to a file in the current directory.
    @param image The image, as a matrix, to be saved.
    @param name_of_image The filename to save the image with.
    @throws InvalidImageMatrixexception if an invalid image matrix is provided. I.e., if it doesn't have an ndim of 3 or less."""
    # Write the image to a file locally.
    try:
        cv.imwrite(filename="images/" + name_of_file, img=image, )
    except cv.error as err:
        raise InvalidImageMatrixException("Invalid image matrix provided")

def save_text(text: str, name_of_file: str = "my_text.txt") -> None:
    """
    Saves the text, as a text file, to the current directory.
    @param text The text to save.
    @name_of_file The name of the file.
    """
    try:
        with open(name_of_file, 'x') as f:
            f.write(text)
    except FileExistsError:
        with open(name_of_file, 'w') as f:
            f.write(text)

def convert_image_to_sepia(image: np.ndarray) -> np.ndarray:
    """
    Takes an image, and return the image (as a three-dimensional matrix) with a sepia filter applied.
    This method does not modify the original image array. It returns a copy.

    @param image The matrix representing the image. The image must be coloured (i.e., a three-dimensional matrix).
    @throws InvalidImageMatrixException If the ndim of the image is not equal to 3.
    @return The matrix representing the sepia image copy."""
    copy = np.copy(image)

    if image.ndim < 3:
        raise InvalidImageMatrixException(f"Image is greyscale, as it only has {image.ndim} dimensions; it cannot be converted to sepia")
    elif image.ndim > 3:
        raise InvalidImageMatrixException(f"Array with {image.ndim} dimensions is not a valid image")
    
    # When using cv.imread, the order of the colours is BGR. [0] is B, [1] is G, [2] is R.
    # Values for sepia taken from https://stackoverflow.com/a/9449159
    blue = image[..., 0] * 0.131 + image[..., 1] * 0.534 + image[..., 2] * 0.272
    green = image[..., 0] * 0.168 + image[..., 1] * 0.686 + image[..., 2] * 0.349
    red = image[..., 0] * 0.189 + image[..., 1] * 0.769 + image[..., 2] * 0.393

    # Make sure no values are above 255.
    blue[blue > 255] = 255
    green[green > 255] = 255
    red[red > 255] = 255

    # Assign the new values to the sepia copy of the image.
    copy[..., 0] = blue
    copy[..., 1] = green
    copy[..., 2] = red
    return copy

def convert_image_to_ascii(image: np.ndarray) -> str:
    """
    Takes an image (MUST be greyscale, i.e., only have 2 dimensions or less) and returns a string containing the ASCII representation
    of the image."""

    # Check the image is greyscale.
    if image.ndim > 2: 
        raise InvalidImageMatrixException('Only grayscale images can be passed into this method')
    
    result = ""
    # Loop over the image and convert every pixel to an ASCII character.
    for row in image:
        line = []
        for pixel in row:
            line.append(ascii.colour_to_ascii(pixel))
        result += ''.join(line)
        result += '\n'
    return result


# Main function that runs if this .py file is run as a script.
if __name__ == "__main__":
    image = get_image_from_path(sys.argv[1])

    image = convert_image_to_greyscale(image)
    text = convert_image_to_ascii(image)

    save_text(text)
    save_image(image)

    
    # image = convert_image_to_sepia(image)

    # display_image(image)