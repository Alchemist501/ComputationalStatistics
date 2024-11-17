# Experiment 3.2 := Get all the diagonals of a 3D numpy array
import numpy as np

arr = np.arange(27).reshape(3, 3, 3)
print("Diagonals of axis 1 and 2 are : \n", np.diagonal(arr, axis1=0, axis2=1))
print("Diagonals of axis 1 and 3 are : \n", np.diagonal(arr, axis1=0, axis2=2))
print("Diagonals of axis 2 and 3 are : \n", np.diagonal(arr, axis1=1, axis2=2))
