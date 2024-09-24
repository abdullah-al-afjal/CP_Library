def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


# Example usage:
matrix = [[1, 2], [3, 4], [5, 6]]
transposed = transpose_matrix(matrix)
print(transposed)
