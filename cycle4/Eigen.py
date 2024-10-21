#Experiment4.2:= Compute the eigenvalues and right eigenvectors of a given square array using NumPy
import numpy as np
val , vec = np.linalg.eig(np.array([1,2,4,7]).reshape(2,2))
print("Eigen value of array : ",val,"\nEigen vector is :\n",vec)
