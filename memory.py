import numpy as np
import cv2

def process(frame):
    h, w, _ = frame.shape

    # --- Sepia Tone ---
    sepia = np.array([[0.272, 0.534, 0.131],
                      [0.349, 0.686, 0.168],
                      [0.393, 0.769, 0.189]])
    frame = cv2.transform(frame, sepia)
    frame = np.clip(frame, 0, 255).astype(np.uint8)

    # --- Vignette Effect ---
    X = cv2.getGaussianKernel(w, w // 2)
    Y = cv2.getGaussianKernel(h, h // 2)
    vignette = Y @ X.T
    vignette = vignette / vignette.max()
    vignette = cv2.merge([vignette] * 3)
    frame = (frame * vignette).astype(np.uint8)

    # --- Fade Overlay ---
    fade_strength = 0.2 + 0.1 * np.sin(pygame.time.get_ticks() / 500.0)
    fade = np.full_like(frame, 230)  # Light beige overlay
    frame = cv2.addWeighted(fade, fade_strength, frame, 1 - fade_strength, 0)

    return frame
