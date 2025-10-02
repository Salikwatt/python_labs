def transpose(matrix):
    inermatrix = []
    if len([x for x in matrix if len(x) == len(max(matrix, key = len))]) == len(matrix):
        if len(matrix) == 1:
            for element in matrix[0]:
                inermatrix.append([element])
            return inermatrix
        elif len(matrix) == 0:
            return matrix
        else:
            for index in range(len(matrix[0])):
                inermatrix.append([element[index] for element in matrix])
            return inermatrix   
    else:
        return "ValueError"

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2],[3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))