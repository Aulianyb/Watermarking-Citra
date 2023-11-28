import cv2
import numpy as np
import tkinter

def generate_watermark(height, width, k, seed): 
    np.random.seed(seed)
    watermark = np.random.randint(2, size=(width, height))
    watermark = watermark.astype(np.int16)
    watermark[watermark == 0] = -1
    watermark = watermark * k
    return watermark


def encode_image(img_path, k, seed): 
    file_name = img_path.split("/")[-1]
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = np.array(img, dtype=np.int16)
    img_width, img_height = img.shape[:2]
    watermark = generate_watermark(img_height, img_width, k, seed)
    watermarked_img = cv2.add(img, watermark)
    return watermarked_img



    

results = encode_image('./Image.png', 1, 9032003)
cv2.imwrite("results.png", results)