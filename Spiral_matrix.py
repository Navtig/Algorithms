number = int(input())
matrix_0 = [[0 for i in range(number)] for j in range(number)]
elem = 1
iteration = 0
while elem <= number ** 2:
    for upper_item in range(iteration, number - iteration):
        matrix_0[iteration][upper_item] = elem
        elem += 1
    for right_item in range(iteration + 1, number - iteration):
        matrix_0[right_item][number - iteration - 1] = elem
        elem += 1
    for down_item in range(number - iteration - 2, iteration - 1, -1):
        matrix_0[number - iteration - 1][down_item] = elem
        elem += 1
    for left_item in range(number - 2 - (1 * iteration), iteration, -1):
        matrix_0[left_item][iteration] = elem
        elem += 1
    iteration += 1
for item in range(number):
    print(*matrix_0[item])