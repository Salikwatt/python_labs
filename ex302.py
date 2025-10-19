import ex301 
text = ex301.normalize(input(), 1, 1)
print(f'Всего слов: {len(ex301.token(text))}')
print(f'Уникальных слов: {len(set(ex301.token(text)))}')
print('Топ-5:')
for i in ex301.top_freq(ex301.count_freq(ex301.token(text)), 3):
    print(i)