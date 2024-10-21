#Experiment4.1:= Calculate the QR decomposition of a given matrix using NumPy
import numpy as np
Q , R = np.linalg.qr(np.array([1,2,3,4,5,6]).reshape(3,2))
print("Q(Orthogonal Matrix):\n",Q,"\nR(Upper Triangular) :\n",R)
