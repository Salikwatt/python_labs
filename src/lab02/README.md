# ДЗ (lab02)

### Задание A

```py
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
```

![Код и демонстрация работы](/misc/img/lab01/im2A.png)

---

### Задание B transpose()

```py
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
```
![Код и демонстрация работы](/misc/img/lab01/im2B1.png)



### Задание B row_sums()

```py
def row_sums(matrix):
    sums = []
    if len([x for x in matrix if len(x) == len(max(matrix, key = len))]) == len(matrix):
        for element in matrix:
            sums.append(sum(element))
        return sums
    else:
        return "ValueError"
```

![Код и демонстрация работы](/misc/img/lab01/IM2B2.png)

---

### Задание B  col_sums()

```py
def col_sums(matrix):
    if len([x for x in matrix if len(x) == len(max(matrix, key = len))]) == len(matrix):
        sums = []
        for index in range(len(matrix[0])):
            sums.append(sum([element[index] for element in matrix]))
        return sums
    else:
        return 'ValueError'
```

![Код и демонстрация работы](misc/img/lab01/In2B3.png)

---

### Задание C
```py
def format_record(write):
    answer = ''
    if len(write[0]) == 0:
        return "ValueError"
    else:
        newfio = write[0].split()
        answer += newfio[0][0].upper() + newfio[0][1: ] + ' '
        for initial in newfio[1:]:
            answer += initial[0].upper() + '.'
    answer += ', гр. '
    if len(write[1]) == 0:
        return "ValueError"
    else:
        answer += write[1] + ', '
    if 0 <= write[2] <= 5.0:
        answer += f'GPA {format(write[2], '.2f')}'
    else:
        return "ValueError"
    return answer
```

![Код и демонстрация работы](/misc/img/lab01/im2c.png)

---



