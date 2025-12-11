# ДЗ (lab08)

### A. models.py
```py
from datetime import *
from dataclasses import dataclass

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        if isinstance(self.gpa, float) == 0:
            raise ValueError('Неправильный формат среднего балла')
        try:
            datetime.strptime(self.birthdate, "%Y/%m/%d")
        except ValueError:
            raise ValueError('Неправильный формат времени')
        
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 10")

    def age(self) -> int:
        b = datetime.strptime(self.birthdate, "%Y/%m/%d")
        today = date.today()
        if b.month > today.month or b.month == today.month and b.day > today.day:
            return today.year - b.year - 1
        return today.year - b.year

    def to_dict(self) -> dict:
        if len(self.birthdate) == 0 or len(self.group) == 0 or len(self.fio) == 0:
            raise ValueError('Пустое поле')
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            fio = d["fio"],
            birthdate = d["birthdate"],
            group = d["group"],
            gpa= d ["gpa"]
        )
    def __str__(self):
        return f"{self.fio}, {self.group}, GPA: {self.gpa:.2f}, возраст: {self.age()} лет"
```

![Код и демонстрация работы](/src/images/lab08/img8_01.png)
![Код и демонстрация работы](/src/images/lab08/img8_02.png)
---

### Задание B. serialize.py
```py
import json
from models import Student
def students_to_json(students, path):
    with open(path, 'w', encoding='utf-8') as json_file:
        data = [s.to_dict() for s in students]
        json.dump(data, json_file, ensure_ascii=False, indent=2)
def students_from_json(path) -> dict:
    try:
        with open(path, 'r', encoding = 'utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {path} не найден")
    except json.JSONDecodeError:
        raise ValueError(f"Файл {path} содержит некорректный JSON")
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать массив объектов")
    with open(path, 'r', encoding='utf-8') as file:
        return list(json.load(file))
```
![Код и демонстрация работы](/src/images/lab08/img8_03.png)
![Код и демонстрация работы](/src/images/lab08/img8_04.png)
![Код и демонстрация работы](/src/images/lab08/img8_05.png)
![Код и демонстрация работы](/src/images/lab08/img8_06.png)

# ДЗ (lab07)

### A. Тесты для src/lib/text.py
```py
import sys
sys.path.append(r'src\lib')
from text import normalize, tokenize, count_freq, top_freq
import pytest

@pytest.mark.parametrize("input, expected", [('HelLo WoRld', 'hello world'), ('Mr    Smit', 'mr smit'),
                                              ('co\tde\n\r', 'co de'), ('Ёлка', 'елка'),
                                              ('HЁllo   w\noRld!!!!', 'hеllo w orld!!!!'), ('' , '')])
def test_normalize(input, expected):
    assert normalize(input) == expected

@pytest.mark.parametrize("input, expected", [("hello,world!!!", ["hello", "world"]), ("emoji 😀 не слово", ["emoji", "не", "слово"])])
def test_tokenize(input, expected):
    assert tokenize(input) == expected

@pytest.mark.parametrize("input, expected", [(["a","b","a","c","b","a"], {"a":3,"b":2,"c":1}), (["bb","aa","bb","aa","cc"], {"aa":2,"bb":2,"cc":1})])
def test_count_freq(input, expected):
    assert count_freq(input) == expected

@pytest.mark.parametrize("input, expected", [({"a":3,"b":2,"c":1}, [("a",3), ("b",2)]), ({"aa":2,"bb":2,"cc":1}, [("aa",2), ("bb",2)])])
def test_top_freq(input, expected):
    assert top_freq(input, 2) == expected
```

![Код и демонстрация работы](/src/images/lab07/im001.png)
---

### Задание B. Тесты для src/lab05/json_csv.py
```py
import sys
import json
sys.path.append(r'src\lab05')
from json_csv import json_to_csv, csv_to_json
sys.path.append(r'src\lab04')
from io_txt_csv import read_text
import pytest

@pytest.mark.parametrize('json_path, expected', [(r'date\lab05\input.json', 'ValueError'),
                                                 ('', 'FileNotFoundError'),
                                                 (r'date\lab05\kirillica.json', 'ValueError')])
def test_json_to_csv(json_path, expected):
    try:
        json_to_csv(json_path, r'date\lab05\check.csv')
    except ValueError:
        assert 'ValueError' == expected
    except FileNotFoundError:
        assert 'FileNotFoundError' == expected
    else:
        with open(json_path, "r", encoding = 'UTF-8') as file:
            data = json.load(file)
        data = [x for x in data.items()]
        csv_data = read_text(r'date\lab05\check.csv').strip('\n').split('\n')
        csv_data = [tuple(x.split(',')) for x in csv_data]
        assert csv_data == data

@pytest.mark.parametrize('csv_path, expected',[('', 'FileNotFoundError')])
def test_csv_to_json(csv_path, expected):
    try:
        csv_to_json(csv_path, r'data\test.json')
    except FileNotFoundError:
        assert 'FileNotFoundError' == expected
    else:
        with open(r'data\test.json', "r", encoding = 'UTF-8') as file:
            data = json.load(file)
        data = [x for x in data.items()]
        csv_data = read_text(r'date\lab05\check.csv').strip('\n').split('\n')
        csv_data = [tuple(x.split(',')) for x in csv_data]
        assert csv_data == data
```
![Код и демонстрация работы](/src/images/lab07/im002.png)
![Код и демонстрация работы](/src/images/lab07/im003.png)
![Код и демонстрация работы](/src/images/lab07/im004.png)
![Код и демонстрация работы](/src/images/lab07/im005.png)

### Задание C Black

```py
import sys

sys.path.append(r"src\lib")
from text import normalize, tokenize, count_freq, top_freq
import pytest

@pytest.mark.parametrize(
    "input, expected",
    [
        ("HelLo WoRld", "hello world"),
        ("Mr    Smit", "mr smit"),
        ("co\tde\n\r", "co de"),
        ("Ёлка", "елка"),
        ("HЁllo   w\noRld!!!!", "hеllo w orld!!!!"),
        ("", ""),
    ],
)
def test_normalize(input, expected):
    assert normalize(input) == expected

@pytest.mark.parametrize(
    "input, expected",
    [
        ("hello,world!!!", ["hello", "world"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ],
)
def test_tokenize(input, expected):
    assert tokenize(input) == expected

@pytest.mark.parametrize(
    "input, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        (["bb", "aa", "bb", "aa", "cc"], {"aa": 2, "bb": 2, "cc": 1}),
    ],
)
def test_count_freq(input, expected):
    assert count_freq(input) == expected

@pytest.mark.parametrize(
    "input, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, [("a", 3), ("b", 2)]),
        ({"aa": 2, "bb": 2, "cc": 1}, [("aa", 2), ("bb", 2)]),
    ],
)
def test_top_freq(input, expected):
    assert top_freq(input, 2) == expected
```
```py
import sys
import json

sys.path.append(r"src\lab05")
from json_csv import json_to_csv, csv_to_json

sys.path.append(r"src\lab04")
from io_txt_csv import read_text
import pytest

@pytest.mark.parametrize(
    "json_path, expected",
    [
        (r"date\lab05\input.json", "ValueError"),
        ("", "FileNotFoundError"),
        (r"date\lab05\kirillica.json", "ValueError"),
    ],
)
def test_json_to_csv(json_path, expected):
    try:
        json_to_csv(json_path, r"date\lab05\check.csv")
    except ValueError:
        assert "ValueError" == expected
    except FileNotFoundError:
        assert "FileNotFoundError" == expected
    else:
        with open(json_path, "r", encoding="UTF-8") as file:
            data = json.load(file)
        data = [x for x in data.items()]
        csv_data = read_text(r"date\lab05\check.csv").strip("\n").split("\n")
        csv_data = [tuple(x.split(",")) for x in csv_data]
        assert csv_data == data

@pytest.mark.parametrize("csv_path, expected", [("", "FileNotFoundError")])
def test_csv_to_json(csv_path, expected):
    try:
        csv_to_json(csv_path, r"data\test.json")
    except FileNotFoundError:
        assert "FileNotFoundError" == expected
    else:
        with open(r"data\test.json", "r", encoding="UTF-8") as file:
            data = json.load(file)
        data = [x for x in data.items()]
        csv_data = read_text(r"date\lab05\check.csv").strip("\n").split("\n")
        csv_data = [tuple(x.split(",")) for x in csv_data]
        assert csv_data == data

```
# ДЗ (lab06)

### Задание A — модуль src/lab06/cli_text.py
```py
import argparse
import sys 
from pathlib import Path
sys.path.append(r'src\lib')
from text1 import *
parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
subparsers = parser.add_subparsers(dest="command")

# подкоманда cat
cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
cat_parser.add_argument("--input", required=True)
cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

# подкоманда stats
stats_parser = subparsers.add_parser("stats", help="Частоты слов")
stats_parser.add_argument("--input", required=True)
stats_parser.add_argument("--top", type=int, default=5)

args = parser.parse_args()

if args.command == "stats":
    p = Path(args.input)
    with open(p, "r", encoding="utf-8") as file:
        text = file.read()
        for i in top_freq(count_freq(tokenize(normalize(text))), 5):
            print(i[0], i[1])
elif args.command == "cat":
    p = Path(args.input)
    with open(p, "r", encoding="utf-8") as file:
        text = file.readlines()
        if not args.n:
            for i in text:
                print(i.replace("\n", ""))
        else:
            text = enumerate(text, start = 1)
            for i in text:
                print(i[0], i[1].replace("\n", ""))
```

![Код и демонстрация работы](/src/images/lab06/img01.png)

![Код и демонстрация работы](/src/images/lab06/img02.png)

![Код и демонстрация работы](/src/images/lab06/img03.png)

![Код и демонстрация работы](/src/images/lab06/img04.png)

---

### Задание B – src/lab06/cli_convert.py

```py
import argparse
import sys
sys.path.append(r'src\lab05')
from csv_xlsx import csv_to_xlsx
from json_csv import json_to_csv, csv_to_json


parser = argparse.ArgumentParser(description="Конвертеры данных")
sub = parser.add_subparsers(dest="command")

p1 = sub.add_parser("json2csv")
p1.add_argument("--in", dest="input", required=True)
p1.add_argument("--out", dest="output", required=True)

p2 = sub.add_parser("csv2json")
p2.add_argument("--in", dest="input", required=True)
p2.add_argument("--out", dest="output", required=True)

p3 = sub.add_parser("csv2xlsx")
p3.add_argument("--in", dest="input", required=True)
p3.add_argument("--out", dest="output", required=True)

args = parser.parse_args()
if args.command == "json2csv":
    json_to_csv(args.input , args.output)
if args.command == "csv2json":
    csv_to_json(args.input , args.output)
if args.command == "csv2xlsx":
    csv_to_xlsx(args.input , args.output)
```

![Код и демонстрация работы](/src/images/lab06/img05.png)

![Код и демонстрация работы](/src/images/lab06/img06.png)

![Код и демонстрация работы](/src/images/lab06/img07.png)

![Код и демонстрация работы](/src/images/lab06/img08.png)

![Код и демонстрация работы](/src/images/lab06/img09.png)

![Код и демонстрация работы](/src/images/lab06/img10.png)

![Код и демонстрация работы](/src/images/lab06/img11.png)

![Код и демонстрация работы](/src/images/lab06/img12.png)

![Код и демонстрация работы](/src/images/lab06/img13.png)

# ДЗ (lab05)

### Задание A — модуль src/lab05/csv_json.py
![Код и демонстрация работы](/src/images/lab05/image1.png)

![Код и демонстрация работы](/src/images/lab05/imag3.png)

![Код и демонстрация работы](/src/images/lab05/imag4.png)

![Код и демонстрация работы](/src/images/lab05/imag7.png)

![Код и демонстрация работы](/src/images/lab05/imag6.png)

![Код и демонстрация работы](/src/images/lab05/imag8.png)

---
### Задание B – src/lab05/csv_xlsx.py

![Код и демонстрация работы](/src/images/lab05/imag10.png)

![Код и демонстрация работы](/src/images/lab05/imag5.png)

![Код и демонстрация работы](/src/images/lab05/imag11.png)

# ДЗ (lab04)

### Задание A — модуль src/lab04/io_txt_csv.py
![Код и демонстрация работы](/src/images/lab04/image_3.png)

![Код и демонстрация работы](/src/images/lab04/image02.png)

![Код и демонстрация работы](/src/images/lab04/image04.png)

![Код и демонстрация работы](/src/images/lab04/image03.png)

---

### Задание B – src/lab04/text_report.py

![Код и демонстрация работы](/src/images/lab04/image06.png)

![Код и демонстрация работы](/src/images/lab04/image05.png)

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

![Код и демонстрация работы](/src/images/lab02/img01.png)

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
![Код и демонстрация работы](/src/images/lab02/img02.png)



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

![Код и демонстрация работы](/src/images/lab02/img03.png)

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

![Код и демонстрация работы](/src/images/lab02/img04.png)

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

![Код и демонстрация работы](/src/images/lab02/img05.png)

# ДЗ за 10.09.2025 (lab01)

### Задание 1 — Привет и возраст

```py
name = input()
age = int(input())
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```

![Код и демонстрация работы](/src/images/lab01/img01.png)

---

### Задание 2 — Сумма и среднее

```py
a = float(input())
b = float(input())
print(f"sum={a + b}", f"avg={format((a + b) / 2, '.2f')}")
```
![Код и демонстрация работы](/src/images/lab01/img02.png)



### Задание 3 — Чек: скидка и НДС

```py
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {format(base,'.2f')} ₽" ,f"НДС:               {format(vat_amount,'.2f')} ₽", \
      f"Итого к оплате:    {format(total,'.2f')} ₽", sep='\n')
```

![Код и демонстрация работы](/src/images/lab01/img03.png)

---

### Задание 4 — Минуты → ЧЧ:ММ

```py
minute = int(input())
print(f"{minute // 60 % 24}:{minute % 60}")
```

![Код и демонстрация работы](/src/images/lab01/img04.png)

---

### Задание 5 — Инициалы и длина строки
```py
s = input().strip()
fio = s.split()
while '  ' in s:
    s = s.replace('  ','')
print(fio[0][0], fio[1][0], fio[2][0], '.', sep='')
print(f'Длина строки: {len(s)}')
```

![Код и демонстрация работы](/src/images/lab01/img05.png)

---

### Задание 6
```py
kol = int(input())
k1 = 0
k2 = 0
for _ in range(kol):
    data = input().split()
    if data[3] == "True":
        k1 += 1
    else:
        k2 += 1
print(k1, k2)
```

![Код и демонстрация работы](/src/images/lab01/img06.png)

---



