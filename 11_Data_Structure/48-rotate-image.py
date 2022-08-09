def rotate(matrix):
    temp = 0
    n = len(matrix) - 1
    for i in range(int(n / 2) + 1):
        for j in range(i, n - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-j][i]
            matrix[n-j][i] = matrix[n-i][n-j]
            matrix[n-i][n-j] = matrix[j][n-i]
            matrix[j][n-i]  =temp

    return matrix


# Test
print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
# Output: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
