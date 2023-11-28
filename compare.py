import cv2
import numpy as np

def compare_image(original_img_path, watermarked_img_path):
    original_img = cv2.imread(original_img_path, cv2.IMREAD_GRAYSCALE)
    watermarked_img = cv2.imread(watermarked_img_path, cv2.IMREAD_GRAYSCALE)
    diff = cv2.absdiff(original_img, watermarked_img)
    total_diff = np.sum(diff)

    threshold = 100000
    if total_diff > threshold:
        return "The result image has a watermark"
    else:
        return "The result image does not has a watermark"