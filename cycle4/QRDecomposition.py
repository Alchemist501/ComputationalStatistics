import numpy as np
def input_matrix():
	rows = int(input("Enter the number of rows: "))
	cols = int(input("Enter the number of columns: "))
	matrix = []
	print("Enter the matrix row by row:")
	for _ in range(rows):
		row = list(map(float, input().split()))
		if len(row) != cols:
			print("Enter exactly "+ str(cols)+" values.")
			return None
		matrix.append(row)
	return np.array(matrix)
A = input_matrix()
def print_matrix(matrix):
	print('\n'.join(' '.join(map(str, row)) for row in matrix))
if A is not None:
	Q, R = np.linalg.qr(A)
	print("\nMatrix A:")
	print_matrix(A)
	print("\nMatrix Q:")
	print_matrix(Q)
	print("\nMatrix R:")
	print_matrix(R)
	print("\nReconstructed A(Q @ R): ")
	print_matrix(np.dot(Q, R))
