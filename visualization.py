import matplotlib.pyplot as plt
from simulation import run_simulation
import numpy as np

def plot_performance():
    error_levels = np.linspace(0,0.4,10)
    results = []

    for e in error_levels:
        rate = run_simulation(e)
        results.append(rate)

    plt.figure()
    plt.plot(error_levels, results)
    plt.xlabel("Noise Level")
    plt.ylabel("Recovery Rate")
    plt.title("Reed–Solomon Error Recovery")
    plt.savefig("rs_performance.png")
    plt.show(block=False)
