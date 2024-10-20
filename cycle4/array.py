# Experiment4.8:= Convert a NumPy array into a csv file
import numpy as np

filename = "output.csv"
np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(2, 5).tofile(filename, sep=" ")
print("array is saved to " + filename)
