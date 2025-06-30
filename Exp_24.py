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
A = 4
kernel_high_boost = np.array([[ 0, -1,  0],
                              [-1, A+1, -1],
                              [ 0, -1,  0]])

high_boost_img = cv2.filter2D(gray, -1, kernel_high_boost)
display(high_boost_img, f'High-Boost Filter (A={A}) (Q24)')
