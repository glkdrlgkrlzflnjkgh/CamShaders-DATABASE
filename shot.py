import numpy as np
import cv2

def process(frame):
    h, w, _ = frame.shape

    # --- Red flash overlay ---
    overlay = frame.copy()
    red_tint = np.zeros_like(frame)
    red_tint[:, :, 0] = 255  # Red channel maxed
    alpha = 0.4 + 0.2 * np.random.rand()  # Randomized intensity
    cv2.addWeighted(red_tint, alpha, overlay, 1 - alpha, 0, overlay)

    # --- Screen shake ---
    max_offset = 10
    dx = np.random.randint(-max_offset, max_offset)
    dy = np.random.randint(-max_offset, max_offset)
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    shaken = cv2.warpAffine(overlay, M, (w, h))

    # --- Glitch lines ---
    for _ in range(5):
        y = np.random.randint(0, h)
        height = np.random.randint(2, 6)
        glitch = np.random.randint(0, 255, (height, w, 3), dtype=np.uint8)
        shaken[y:y+height] = glitch

    return shaken
