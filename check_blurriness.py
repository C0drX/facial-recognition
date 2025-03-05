import os
import time
import cv2


def estimate_blurriness(image):
    """
    Estimate the blurriness of an image using the Laplacian variance method.

    Parameters:
    image (numpy.ndarray): The image for which to estimate the blurriness.

    Returns:
    float: Blurriness score. Lower values indicate blurrier images.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var
