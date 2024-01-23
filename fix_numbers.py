import pandas as pd
import os



numbers_csv = pd.read_csv('numbers.csv')
numbers = numbers_csv['Numbers'][0] + numbers_csv['Numbers'][1]
numbers_fix = []
numbers = numbers.replace(" ","").replace("-","").replace("+972","0").replace("\u2066","").replace('\u2069',"")
numbers = numbers.split(',')
for i in numbers:
    if(i[0:2] == '05'):
        numbers_fix.append(i)

print(numbers_fix)
print(len(numbers_fix))
