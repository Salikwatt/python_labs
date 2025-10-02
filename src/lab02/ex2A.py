def min_max(nums):
    return (min(nums), max(nums)) if len(nums) > 0 else 'ValueError'

def unique_sorted(nums):
    return sorted(list(set(nums)))

def flatten(matrix):
    inermatrix = []
    for element in matrix:
        if isinstance(element, tuple) or isinstance(element, list):
            for num in element:
                inermatrix.append(num)
        else:
            return "TypeError"
    return inermatrix
print("min_max")
print(min_max([ 3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
print("unique_sorted")
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
print("flatten")
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], 'ab']))