# Experiment 3.4:= Compute fibanocci numbers efficiently using binet formula with Numpy

import numpy as np
def fibanocci(n):
	phi = (1 + np.sqrt(5))/2
	return int((phi**n - (-phi ** -n))/np.sqrt(5))
print("Fibanocci numbers are : ",[fibanocci(n) for n in range(int(input("Enter the number of terms : ")))])
