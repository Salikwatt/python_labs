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
