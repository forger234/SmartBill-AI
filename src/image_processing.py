import cv2
import numpy as np
from PIL import Image


def preprocess_image(image_file):
    # Convert uploaded image into a PIL image
    image = Image.open(image_file).convert("RGB")

    # Convert PIL image into NumPy array
    image_array = np.array(image)

    # Convert RGB to OpenCV BGR format
    image_array = cv2.cvtColor(
        image_array,
        cv2.COLOR_RGB2BGR
    )

    # Convert color image into grayscale
    grayscale = cv2.cvtColor(
        image_array,
        cv2.COLOR_BGR2GRAY
    )

    # Remove image noise
    denoised = cv2.GaussianBlur(
        grayscale,
        (3, 3),
        0
    )

    # Convert into black and white
    processed = cv2.threshold(
        denoised,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return grayscale, denoised, processed