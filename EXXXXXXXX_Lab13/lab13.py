import cv2
import numpy as np
def img2gary(img):
    B = img[:, :, 0]
    G = img[:, :, 1]
    R = img[:, :, 2]
    gray = (B+G+R)/3
    print(gray)
    gray = gray.astype(np.uint8)
    return gray
def thresholding(img):
    threshold = 76
    img = np.array(img)
    binary_image = np.where(img >= threshold, 255, 0).astype(np.uint8)
    print(binary_image)
    return binary_image
image = cv2.imread("TW.jpg")
cv2.imshow('image', image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
cv2.imshow('gray', gray)
gray2 = img2gary(image)
cv2.imshow('gray2', gray2)
binary_image = thresholding(gray2)
cv2.imshow('binary_image', binary_image)
zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.waitKey(0) 
cv2.destroyAllWindows()