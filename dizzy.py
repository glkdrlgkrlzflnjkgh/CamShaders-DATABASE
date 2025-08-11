import numpy as np

def process(frame):
    h, w, _ = frame.shape

    # Create a random grid of blocks
    block_size = 40
    num_blocks_x = w // block_size
    num_blocks_y = h // block_size

    # Shuffle block positions
    indices = [(i, j) for i in range(num_blocks_y) for j in range(num_blocks_x)]
    np.random.shuffle(indices)

    scrambled = np.zeros_like(frame)

    for idx, (i, j) in enumerate(indices):
        src_y = (idx // num_blocks_x) * block_size
        src_x = (idx % num_blocks_x) * block_size
        dst_y = i * block_size
        dst_x = j * block_size

        # Clip bounds to avoid overflow
        src_block = frame[src_y:src_y+block_size, src_x:src_x+block_size]
        scrambled[dst_y:dst_y+block_size, dst_x:dst_x+block_size] = src_block

    return scrambled
