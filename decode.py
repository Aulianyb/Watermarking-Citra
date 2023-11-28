import cv2
import numpy as np

def decode_image(original_img_path, watermarked_img_path):
    original_img = cv2.imread(original_img_path, cv2.IMREAD_GRAYSCALE)
    watermarked_img = cv2.imread(watermarked_img_path, cv2.IMREAD_GRAYSCALE)
    diff = cv2.absdiff(original_img, watermarked_img)
    total_diff = np.sum(diff)

    threshold = 100000
    if total_diff > threshold:
        return "The image appears to be watermarked."
    else:
        return "The image does not seem to be watermarked."
    
result = decode_image("./Image.png", "./results.png")
print(result)