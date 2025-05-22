def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    return [list(row) for row in zip(*matrix)]

# Example usage:
if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    transposed = transpose_matrix(mat)
    print("Original matrix:")
    for row in mat:
        print(row)
    print("\nTransposed matrix:")
    for row in transposed:
        print(row)