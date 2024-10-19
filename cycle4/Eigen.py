import numpy as np
def input_matrix():
	size = int(input("Enter the size of the matrix(n x n): "))
	matrix = []
	print("Enter the matrix row by row:")
	for _ in range(size):
		row = list(map(float, input().split()))
		if len(row) != size:
			print("Enter exactly "+ str(size)+" values.")
			return None
		matrix.append(row)
	return np.array(matrix)
A = input_matrix()
if A is not None:
	egVal, egVec = np.linalg.eig(A)
	print("\nEigen Values :")
	print(egVal)
	print("\nEigen Vectors :")
	print(egVec)
