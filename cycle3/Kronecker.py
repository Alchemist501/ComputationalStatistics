import numpy as np

def kronecker_product(A, B):
    return np.kron(A, B)

# Example usage
A = np.array([[1, 2], [3, 4]])  # 2x2 matrix
B = np.array([[0, 5], [6, 7]])  # 2x2 matrix

C = kronecker_product(A, B)
print("Kronecker product of A and B is:")
print(C)
