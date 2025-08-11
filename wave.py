import numpy as np
import cv2
import time

start_time = time.time()

def process(frame):
    rows, cols, _ = frame.shape
    t = time.time() - start_time * 40
    wave = np.zeros_like(frame)

    # Adjust these for wave strength and frequency
    amplitude = 20
    frequency = 0.01

    for y in range(rows):
        offset_x = int(amplitude * np.sin(2 * np.pi * frequency * y + t))
        offset_y = int(amplitude * np.sin(2 * np.pi * frequency * y + t))
        wave[y, :] = np.roll(frame[y, :], offset_x, axis=0)
        
        

    return wave
