import cv2
import numpy as np
import random

def process(frame):
    h, w = frame.shape[:2]

    # Horizontal slice shifting
    for _ in range(10):
        y = random.randint(0, h - 1)
        height = random.randint(1, 5)
        offset = random.randint(-20, 20)
        frame[y:y+height] = np.roll(frame[y:y+height], offset, axis=1)

    # Color channel offset
    b, g, r = cv2.split(frame)
    r = np.roll(r, 2, axis=1)
    b = np.roll(b, -2, axis=0)
    frame = cv2.merge((b, g, r))

    # Add scanlines
    for y in range(0, h, 2):
        frame[y] = frame[y] * 0.8

    # Random noise specks
    noise = np.random.randint(0, 50, (h, w, 1), dtype='uint8')
    frame = cv2.add(frame, np.repeat(noise, 3, axis=2))

    return frame