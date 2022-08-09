def search_matrix(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    
    n = len(matrix[0])

    i = 0
    j = n - 1

    while i < m and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j = j - 1
        else:
            i = i + 1
    
    return False


# Test
print(search_matrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
# Output: True
print(search_matrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20))
# Output: False
