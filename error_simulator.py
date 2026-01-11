import random

def corrupt_block(block, error_rate=0.1):
    corrupted = block.copy()
    for i in range(len(corrupted)):
        if random.random() < error_rate:
            corrupted[i] = random.randint(0, 255)
    return corrupted