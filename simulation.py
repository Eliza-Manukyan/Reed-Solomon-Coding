import random
from rs_encoder import RSEncoder
from rs_decoder import RSDecoder
from error_simulator import corrupt_block

def run_simulation(error_rate, trials=500):
    encoder = RSEncoder()
    decoder = RSDecoder()
    success = 0

    for _ in range(trials):
        data = [random.randint(0,255) for _ in range(11)]
        encoded = encoder.encode(data)
        damaged = corrupt_block(encoded, error_rate)

        decoded, ok = decoder.decode(damaged)
        if ok and decoded == data:
            success += 1

    return success / trials
