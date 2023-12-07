import cv2
import src
import numpy as np

def red_mask(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 50, 70), (9, 255, 255))
    return mask

def green_mask(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (36, 50, 70), (89, 255, 255))
    return mask

def segment_image(img):
    color = (0, 0, 255)  # red
    thickness = 2
    num_segments = 3
    segment_width = img.shape[1] // num_segments
    segment_height = img.shape[0] // num_segments

    for i in range(1, num_segments):
        x_position = i * segment_width
        cv2.line(img, (x_position, 0), (x_position, img.shape[0]), color, thickness)

    for i in range(1, num_segments):
        y_position = i * segment_height
        cv2.line(img, (0, y_position), (img.shape[1], y_position), color, thickness)

    return img


def detect_objects(masked_image):  # This function works regardless of the color, since it takes a binary img as input
    num_segments = 3

    # Define the segments
    segments = []
    segment_width = masked_image.shape[1] // num_segments
    segment_height = masked_image.shape[0] // num_segments
    segment_names = ["Top Left", "Middle Left", "Bottom Left", "Top Center", "Middle Center", "Bottom Center",
                     "Top Right", "Middle Right", "Bottom Right"]

    # A cleaner war to define each segment thanks to ChatGPT
    for i in range(num_segments):
        for j in range(num_segments):
            start_x = i * segment_width
            end_x = (i + 1) * segment_width
            start_y = j * segment_height
            end_y = (j + 1) * segment_height
            segments.append((start_x, end_x, start_y, end_y))

    # Count pixels in each segment and form output
    segment_pixel_counts = [0] * len(segments)
    for idx, (start_x, end_x, start_y, end_y) in enumerate(segments):
        segment = masked_image[start_y:end_y, start_x:end_x]
        segment_pixel_counts[idx] = cv2.countNonZero(segment)
        segment_name = segment_names[idx]
        # print(f"Pixel Count for {segment_name} segment: {segment_pixel_counts[idx]}")

    return segment_pixel_counts










