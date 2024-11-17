# Experiment 3.1 := Plot a graph y = f(x)
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
plt.plot(x, x**3, "g")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
