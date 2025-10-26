def normalize(text):
    new_text = text.replace(r'\n',' ').replace(r'\t', ' ').replace(r'\r', ' ')
    new_text = new_text.casefold()
    new_text = new_text.replace('Ё','Е').replace('ё', 'е')
    new_text = ' '.join(new_text.split())
    return new_text

def token(text):
    lst = [x for x in text]
    for index in range(len(lst)):
        if (lst[index].isdigit() or lst[index].islower() or lst[index] in [' ','-','_']) == 0:
            lst[index] = ' '
    answer = [x.strip('-') for x in ''.join(lst).split() if x != '-']
    return answer
def count_freq(tokens):
    counts = dict()
    for i in set(tokens):
        counts[i] = tokens.count(i)
    return counts
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
