import numpy as np
import cv2

def process(frame):
    ascii_chars = "/.:-=+*#%@"
    char_len = len(ascii_chars)
    font_scale = 0.4
    block_size = 8

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    h, w = gray.shape
    ascii_frame = np.ones_like(frame) * 0

    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            block = gray[y:y+block_size, x:x+block_size]
            if block.size == 0:
                continue
            avg = int(np.mean(block))
            char = ascii_chars[int((avg / 255) * (char_len - 1))]
            cv2.putText(ascii_frame, char, (x, y + block_size), cv2.FONT_HERSHEY_SIMPLEX,
                        font_scale, (200, 255, 200), 1, cv2.LINE_AA)
    return ascii_frame