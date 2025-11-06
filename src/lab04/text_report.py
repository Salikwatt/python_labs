import sys 
sys.path.append(r'C:\Users\user\python_labs\python_labs\src\lib') 
from text1 import normalize, tokenize, count_freq, top_freq
from io_txt_csv import read_text, write_csv 
from stats import statistics 

input_text = read_text(r'C:\Users\user\python_labs\python_labs\date\input2.txt')
statistics(input_text)

print(top_freq(count_freq(tokenize(normalize(input_text))), 5))
write_csv(top_freq(count_freq(tokenize(normalize(input_text))), 5), path = r'C:\Users\user\python_labs\python_labs\date\check2.csv', header= ['word', 'count'])
