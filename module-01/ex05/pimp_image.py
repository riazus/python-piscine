import numpy as np
from PIL import Image


def ft_invert(array):
    """
    Inverts the colors of the given image array.

    Parameters:
    array (numpy.ndarray): A 3D numpy array representing
    an image with shape (height, width, channels).

    Returns:
    None: The function displays the inverted image using
    the default image viewer.
    """
    image = 255 - array
    Image.fromarray(image).show()


def ft_red(array):
    """
    Isolates the red channel of the given image array,
    setting the green and blue channels to zero.

    Parameters:
    array (numpy.ndarray): A 3D numpy array representing
    an image with shape (height, width, channels).

    Returns:
    None: The function displays the red channel image using
    the default image viewer.
    """
    red_channel = array[:, :, 0]
    image = np.zeros_like(array)
    image[:, :, 0] = red_channel
    Image.fromarray(image).show()


def ft_green(array):
    """
    Isolates the green channel of the given image array,
    setting the red and blue channels to zero.

    Parameters:
    array (numpy.ndarray): A 3D numpy array representing
    an image with shape (height, width, channels).

    Returns:
    None: The function displays the green channel image using
    the default image viewer.
    """
    green_channel = array[:, :, 1]
    image = array.copy()
    image[:, :, 0] = 0
    image[:, :, 2] = 0
    image[:, :, 1] = green_channel
    Image.fromarray(image).show()


def ft_blue(array):
    """
    Isolates the blue channel of the given image array,
    setting the red and green channels to zero.

    Parameters:
    array (numpy.ndarray): A 3D numpy array representing
    an image with shape (height, width, channels).

    Returns:
    None: The function displays the blue channel image using
    the default image viewer.
    """
    blue_channel = array[:, :, 2]
    image = np.zeros_like(array)
    image[:, :, 2] = blue_channel
    Image.fromarray(image).show()


def ft_grey(array):
    """
    Converts the given image array to grayscale
    by averaging the red, green, and blue channels.

    Parameters:
    array (numpy.ndarray): A 3D numpy array representing
    an image with shape (height, width, channels).

    Returns:
    None: The function displays the grayscale image using
      the default image viewer.
    """
    red_channel = array[:, :, 0] / 3
    green_channel = array[:, :, 1] / 3
    blue_channel = array[:, :, 2] / 3
    grey_channel = red_channel + green_channel + blue_channel
    grey_image = np.stack([grey_channel, grey_channel, grey_channel], axis=2)
    Image.fromarray(grey_image.astype(np.uint8)).show()
