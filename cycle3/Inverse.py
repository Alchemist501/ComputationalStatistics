#Experiment 3.5 := Inverse a matrix using numpy

import numpy as np
mat = np.array([[1,2],[3,4]])
print("Inverse of the matrix is : \n" + str(np.linalg.inv(mat)) if np.linalg.det(mat) != 0 
	else "The martix is singular and it doesn't have any inverse !.")
