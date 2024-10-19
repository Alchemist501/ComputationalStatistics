import numpy as np

def invert_matrix(matrix):
    # Check if the matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square.")
    
    # Check if the determinant is non-zero
    if np.linalg.det(matrix) == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    
    # Compute the inverse of the matrix
    inverse_matrix = np.linalg.inv(matrix)
    return inverse_matrix

# Example Usage
if __name__ == "__main__":
    # Define a square matrix
    A = np.array([[4, 7],
                  [2, 6]])
    
    try:
        A_inv = invert_matrix(A)
        print("Original Matrix:\n", A)
        print("Inverse Matrix:\n", A_inv)
    except ValueError as e:
        print(e)
