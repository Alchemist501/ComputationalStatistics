#Experiment 3.6 := Calculate inner, outer and cross products of matrices and vectors using Numpy

import numpy as np
A = np.array([1,2,3])
B = np.array([4,5,6])
print(
	"Inner Product is : ",np.inner(A,B),
	"\nOuter Product is : \n",np.outer(A,B),
	"\nCross Product is : ",np.cross(A,B)
)
