# ДЗ (lab03)

### Задание A normalize

```py
def normalize(text, casefold, repe):
    new_text = text.replace(r'\n',' ').replace(r'\t', ' ').replace(r'\r', ' ')
    if casefold == True:
        new_text = new_text.casefold()
    if repe == True:
        new_text = new_text.replace('Ё','Е').replace('ё', 'е')
    new_text = ' '.join(new_text.split())
    return new_text
```

![Код и демонстрация работы](/src/images/lab03/img01.png)

---

### Задание A token

```py
def token(text):
    lst = [x for x in text]
    for index in range(len(lst)):
        if (lst[index].isdigit() or lst[index].islower() or lst[index] in [' ','-','_']) == 0:
            lst[index] = ' '
    answer = [x.strip('-') for x in ''.join(lst).split() if x != '-']
    return answer
```
![Код и демонстрация работы](src/images/lab03/img02.png)

### Задание A count_freq

```py
def count_freq(tokens):
    counts = dict()
    for i in set(tokens):
        counts[i] = tokens.count(i)
    return counts
```

![Код и демонстрация работы](/src/images/lab03/img03.png)

---

### Задание A  top_freq

```py
def top_freq(counts, kol):
    direct = counts.items()
    maxi = max(list(counts.values()))
    answer = []
    if kol > len(direct):
        kol = len(direct)
    while kol > 0:
        answer = answer + sorted([x for x in direct if x[1] == maxi])[0: kol]
        kol = kol - len(sorted([x[0] for x in direct if x[1] == maxi])[0: kol])
        maxi -= 1
    return answer
```

![Код и демонстрация работы](/src/images/lab03/img04.png)

---

### Задание B
```py
import ex301 
text = ex301.normalize(input(), 1, 1)
print(f'Всего слов: {len(ex301.token(text))}')
print(f'Уникальных слов: {len(set(ex301.token(text)))}')
print('Топ-5:')
for i in ex301.top_freq(ex301.count_freq(ex301.token(text)), 3):
    print(i)
```

![Код и демонстрация работы](/src/images/lab03/img05.png)
