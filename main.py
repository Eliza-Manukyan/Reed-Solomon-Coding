from block_visualization import visualize_blocks
from visualization import plot_performance
from rs_encoder import RSEncoder
from rs_decoder import RSDecoder
from error_simulator import corrupt_block

encoder = RSEncoder()
decoder = RSDecoder()

# Example block
data = [10,20,30,40,50,60,70,80,90,100,110]
print("Original:", data)

encoded = encoder.encode(data)
print("Encoded:", encoded)

damaged = corrupt_block(encoded, 0.2)
print("Damaged:", damaged)

decoded, ok = decoder.decode(damaged)
print("Recovered:", decoded)
print("Success:", ok)

# Block-level visualization
visualize_blocks(data, encoded, damaged, decoded)

# Performance visualization
plot_performance()
import matplotlib.pyplot as plt
plt.show()