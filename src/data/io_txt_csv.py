import csv # библиотека для работы с csv
from pathlib import Path # библиотека для получения правильного пути
from typing import Iterable, Sequence # для типизации
import os # библиотека для работы с системой

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    if os.path.exists(path) == 0: # проверка на существование пути
        return 'FileNotFoundError'
    p = Path(path)
    try:
        p.read_text(encoding=encoding) # проверка на неправильную кодировку
    except UnicodeDecodeError: # except ловит ошибки и выводит
        return "UnicodeDecodeError"
    return p.read_text(encoding=encoding)
# Если пользователя нужно выбрать другую кодировку,то ее нужно написать строкой как второй аргумент функции

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None and rows == []: #записывает тестовые данные, если предан заголовок, но нет строк
            w.writerow(('a','b'))
        if header is not None:
            w.writerow(header)
        if rows:
            const = len(rows[0])
            for r in rows:
                if len(r) != const:
                    raise ValueError("Все строки должны иметь одинаковую длину")  
            for r in rows:    
                w.writerow(r)

txt = read_text(r"C:\Users\user\python_labs\python_labs\date\input1.txt")  # должен вернуть строку
print(txt)
write_csv([('Товар', 'Продано'),('сахар', '10')], r"C:\Users\user\python_labs\python_labs\date\check.csv", None)  # создаст CSV
