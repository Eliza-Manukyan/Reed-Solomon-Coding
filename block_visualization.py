import matplotlib.pyplot as plt

def visualize_blocks(original, encoded, damaged, recovered):
    plt.figure(figsize=(10,4))

    plt.subplot(4,1,1)
    plt.bar(range(len(original)), original)
    plt.title("Original Block")

    plt.subplot(4,1,2)
    plt.bar(range(len(encoded)), encoded)
    plt.title("Encoded Block (with Parity)")

    plt.subplot(4,1,3)
    plt.bar(range(len(damaged)), damaged)
    plt.title("Damaged Block")

    if recovered is not None:
        plt.subplot(4,1,4)
        plt.bar(range(len(recovered)), recovered)
        plt.title("Recovered Block")

    plt.tight_layout()
    plt.savefig("block_transformation.png")
    plt.show(block=False)
