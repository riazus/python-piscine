import os
import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt


def transpose_image(image):
    width, height = image.size
    transposed_image = Image.new("RGB", (height, width))

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            transposed_image.putpixel((y, x), pixel)

    return transposed_image


def crop_image(image):
    crp_size = min(image.width, image.height)
    crp_left = (image.width - crp_size) // 2
    crp_top = (image.height - crp_size) // 2
    crp_right = crp_left + crp_size
    crp_bottom = crp_top + crp_size

    return image.crop((crp_left, crp_top, crp_right, crp_bottom))


def ft_rotate():
    try:
        path = "animal.jpeg"
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        image = Image.open(path)
        if image is None:
            raise AssertionError("Failed to load image.")
        image.show()

        square_crop = crop_image(image)
        square_crop.save("square_crop.jpg")
        ft_load("square_crop.jpg")

        print(np.array(square_crop.convert("L")))

        transposed_image = transpose_image(square_crop)
        print(np.array(transposed_image.convert("L")))
        transposed_image.show()
        mirrored_image = transposed_image.transpose(Image.FLIP_LEFT_RIGHT)
        mirrored_image.show()
        print(f"New shape after Transpose: {transposed_image.size}")

        plt.imshow(transposed_image)
        plt.title("Transposed Image")
        plt.axis('on')
        plt.show()
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


def main():
    ft_rotate()


if __name__ == "__main__":
    main()
