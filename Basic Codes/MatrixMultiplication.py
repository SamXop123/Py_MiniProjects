
#This program multiplies any two 3x3 matrix without any physical calculation

#! 3x3 MATRIX MULTIPLICATION:

# Function to input a 3x3 matrix
def input_matrix(matrix_number):
    matrix = []
    print()
    print(f"Enter the elements for Matrix {matrix_number} (3x3):")
    print()
    for i in range(3):
        row = []
        for j in range(3):
            value = int(input(f"Enter element at row {i + 1}, column {j + 1}: "))
            row.append(value)
        matrix.append(row)
    return matrix

print()

# Function to display a 3x3 matrix
def display_matrix(matrix, matrix_number):
    print(f"Matrix {matrix_number}:")
    for row in matrix:
        print(row)
    print()  # Add an empty line for better readability

# Input matrices from the user
matrix1 = input_matrix(1)
matrix2 = input_matrix(2)

# Display the entered matrices
display_matrix(matrix1, 1)
display_matrix(matrix2, 2)

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

print()
