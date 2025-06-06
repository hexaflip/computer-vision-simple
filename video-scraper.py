import cv2 as cv
import numpy as np
import random as rn
import os

# Create output folder if it doesn't exist
output_folder = "framed frames"
os.makedirs(output_folder, exist_ok=True)

cap = cv.VideoCapture("video.mp4")

n = 0
while cap.isOpened():
    # using random integers, so you can use multiple videos without overlap hopefully
    mul = rn.randint(100000, 999999)
    ret, frame = cap.read()

    if not ret:
        print("ending")
        break
    # change the 250 to be however many other frames you need 
    if n % 250 == 0:
        filename = f"image{mul}.jpg"
        file_path = os.path.join(output_folder, file_name)
        cv.imwrite(file_path, frame)
    n += 1

cap.release()
