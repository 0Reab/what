import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('data.txt', "r") as f:
    data = f.readlines()
#print(data)
values = []
dates = []
dict = {}
key_value_pairs = []

for item in data:
    float_value = float(item.split()[-1].rstrip(',\n'))
    date = item.split()[0] + " " + item.split()[1]

    values.append(float_value)
    dates.append(date)
    key_value_pairs.append((date, float_value))

for key, value in key_value_pairs:
    dict[key] = value
#print(clean)
#print(dates)
#print(dict)
print((sum(values)/len(values)))
#plt.plot(values, linestyle = 'dotted')


#plt.show()