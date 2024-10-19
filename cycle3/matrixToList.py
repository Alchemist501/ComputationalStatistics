def matrix_to_list(matrix):
    result = []
    for row in matrix:
        for element in row:
            result.append(element)
    return result

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

converted_list = matrix_to_list(matrix)
print(converted_list)
