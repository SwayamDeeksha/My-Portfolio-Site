def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))