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

def nth_order_difference(arr, n, axis=0):
    if n == 0:
        return arr
    else:
        diff = np.diff(arr, axis=axis)
        if diff.size == 0:
            return diff
        return nth_order_difference(diff, n - 1, axis)

def print_matrix(matrix):
    if matrix.size == 0:
        print("Empty array.")
    else:
        print('\n'.join(' '.join(map(str, row)) for row in matrix))

array = input_matrix()
if array is not None:
    n = int(input("Enter the order of difference: "))
    result = nth_order_difference(array, n, axis=0)
    print("\nOriginal array:")
    print_matrix(array)
    print("\n"+str(n)+"-th order difference along axis 0:")
    print_matrix(result)
else:
    print("Invalid input matrix.")

