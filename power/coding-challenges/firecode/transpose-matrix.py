def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("transpose_matrix():", transpose_matrix(matrix))
matrix = [[1, 0, 1], [1, 0, 1], [1, 0, 1]]
print("transpose_matrix():", transpose_matrix(matrix))
matrix = [[1]]
print("transpose_matrix():", transpose_matrix(matrix))

"""
transpose_matrix(): [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
transpose_matrix(): [[1, 1, 1], [0, 0, 0], [1, 1, 1]]
transpose_matrix(): [[1]]
"""

"""
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    temp = 0

    for i in range(0, rows):
        for j in range(i+1,cols):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
"""