import cv2
import src
import numpy as np

def red_mask(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 50, 70), (9, 255, 255))
    size_x = img.shape[0]
    size_y = img.shape[1]
    return mask

def green_mask(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (36, 50, 70), (89, 255, 255))
    size_x = img.shape[0]
    size_y = img.shape[1]
    return mask



