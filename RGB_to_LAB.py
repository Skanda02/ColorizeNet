# pip install opencv-python

import cv2
import os

# Paths
input_dir = "data/"
output_dir = "lab_images"

# Create output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through images
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_dir, filename)

        # Read image (OpenCV reads as BGR)
        bgr = cv2.imread(img_path)
        if bgr is None:
            continue

        # Convert BGR → RGB
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

        # Convert RGB → LAB
        lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB)

        # Save LAB image
        out_path = os.path.join(output_dir, filename)
        cv2.imwrite(out_path, lab)

print("✅ Conversion completed.")
