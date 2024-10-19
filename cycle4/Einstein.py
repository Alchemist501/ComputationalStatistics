import numpy as np

def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    print("Enter the matrix row by row (space-separated values):")
    for _ in range(rows):
        row = list(map(float, input().split()))
        if len(row) != cols:
            print("Please enter exactly "+str(cols)+" values.")
            return None
        matrix.append(row)
    return np.array(matrix)

A = input_matrix()
B = input_matrix()

result = np.einsum('ik,kj->ij', A, B)
print("Result of the Einstein summation:")
print(result)

