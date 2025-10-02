def col_sums(matrix):
    if len([x for x in matrix if len(x) == len(max(matrix, key = len))]) == len(matrix):
        sums = []
        for index in range(len(matrix[0])):
            sums.append(sum([element[index] for element in matrix]))
        return sums
    else:
        return 'ValueError'
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))