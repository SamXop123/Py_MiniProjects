
# Initialize the two 3x3 matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Create a result matrix initialized with zeros
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Perform the matrix multiplication
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# Print the result matrix
print("Result of 3x3 matrix multiplication:")
for row in result:
    print(row)
