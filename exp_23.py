import cv2
import numpy as np
from matplotlib import pyplot as plt

def display(img, title):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

# Load image
image = cv2.imread(r'C:\Users\divya\OneDrive\Pictures\Totoro.jpg')  # Replace with your image path
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Blur image
blurred = cv2.GaussianBlur(gray, (9, 9), 10)

# Subtract blurred from original
unsharp = cv2.addWeighted(gray, 1.5, blurred, -0.5, 0)
display(unsharp, 'Unsharp Masking (Q23)')
