import numpy as np

matrix = []
nums = input()
while nums != 'end':
    matrix.append([int(item) for item in nums.split()])
    nums = input()
new_matrix = list(np.zeros_like(matrix))
for row in range(len(matrix)):
    for column in range(len(matrix[0])):
        if row == len(matrix) - 1 and column == len(matrix[0]) - 1:
            sum_numbers = matrix[row][column - 1] + matrix[row - 1][column] + matrix[row][0] + matrix[0][column]
            new_matrix[row][column] = sum_numbers
        elif column == len(matrix[0]) - 1:
            sum_numbers = matrix[row][column - 1] + matrix[row - 1][column] + matrix[row][0] + matrix[row + 1][column]
            new_matrix[row][column] = sum_numbers
        elif row == len(matrix) - 1:
            sum_numbers = matrix[row][column - 1] + matrix[row - 1][column] + matrix[row][column + 1] + matrix[0][column]
            new_matrix[row][column] = sum_numbers
        else:
            sum_numbers = matrix[row][column - 1] + matrix[row - 1][column] + matrix[row][column + 1] + matrix[row + 1][column]
            new_matrix[row][column] = sum_numbers
for i in new_matrix:
    print(*i, sep=' ')
