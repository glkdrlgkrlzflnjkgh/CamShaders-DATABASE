import cv2
import numpy as np

def process(frame):
    # Convert to grayscale for edge detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    edges = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Laplacian(edges, cv2.CV_8U, ksize=5)
    edges = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY_INV)[1]

    # Posterize (quantize) colors
    div = 128  # smaller = more contrasty blocks
    quant = frame // div * div + div // 2

    # Combine edges with posterized color
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    cel = cv2.bitwise_and(quant, edges_colored)

    return cel