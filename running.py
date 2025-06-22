import cv2
import numpy as np
import random
import time

start_time = time.time()

def process(frame):
    h, w = frame.shape[:2]

    # Simulate camera shake
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    frame = cv2.warpAffine(frame, M, (w, h))

    # Add motion blur (vertical streaks)
    ksize = 9
    kernel = np.zeros((ksize, ksize))
    kernel[:, ksize // 2] = np.ones(ksize)
    kernel /= ksize
    frame = cv2.filter2D(frame, -1, kernel)

    # Add slight chromatic aberration
    b, g, r = cv2.split(frame)
    shift = 2
    r = np.roll(r, shift, axis=1)
    b = np.roll(b, -shift, axis=1)
    frame = cv2.merge((b, g, r))

    # Add vignette
    Y, X = np.ogrid[:h, :w]
    center_x, center_y = w / 2, h / 2
    dist = np.sqrt((X - center_x)**2 + (Y - center_y)**2)
    max_dist = np.sqrt(center_x**2 + center_y**2)
    vignette = 1 - (dist / max_dist)**2
    vignette = np.clip(vignette, 0.5, 1.0)
    frame = (frame * vignette[..., np.newaxis]).astype(np.uint8)

    return frame