def row_sums(matrix):
    sums = []
    if len([x for x in matrix if len(x) == len(max(matrix, key = len))]) == len(matrix):
        for element in matrix:
            sums.append(sum(element))
        return sums
    else:
        return "ValueError"
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
