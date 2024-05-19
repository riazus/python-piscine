import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Function for load image (jpg/jpeg)
    Returns information about image
    """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        img = Image.open(path)

        header = "The shape of Image is:"
        print(f"{header} ({img.size[1]}, {img.size[0]}, {img.layers})")
        return np.array(img)
    except AssertionError as error:
        print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")
