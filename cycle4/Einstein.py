#Experiment4.4:= 4. Evaluate Einstein’s summation convention of two multidimensional NumPy arrays
import numpy as np
print("Einstein Summation Convention of 2 arrays : ",np.einsum('ij,jk->ik',np.array([1,2,3,4]).reshape(2,2),(np.array([5,6,7,8]).reshape(2,2))))
