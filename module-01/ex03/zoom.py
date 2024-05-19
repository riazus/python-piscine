import os
import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_zoom():
    try:
        path = "animal.jpeg"
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        image = Image.open(path)
        if image is None:
            raise AssertionError("Failed to load image.")

        print(ft_load(path))
        image.show()

        zoomed_image = image.crop((400, 100, 800, 600))
        zoomed_image.save("zoomed_image.jpg")
        print(f"New shape after slicing: {zoomed_image.size}")

        grayscale_image = zoomed_image.convert("L")
        grayscale_image.show()
        print(np.array(grayscale_image))

        plt.imshow(zoomed_image)
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


def main():
    ft_zoom()


if __name__ == "__main__":
    main()
