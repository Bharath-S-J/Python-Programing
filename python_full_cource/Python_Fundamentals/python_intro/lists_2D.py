# Define a 2D list (matrix) containing rows of numbers
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Modify an element in the matrix (change the value at row 0, column 1 to 40)
matrix[0][1] = 40

# Print the modified element (should print 40)
print(matrix[0][1])

# Iterate through each row in the matrix
for row in matrix:
    # Iterate through each item in the current row
    for item in row:
        # Print each item in the matrix
        print(item)
