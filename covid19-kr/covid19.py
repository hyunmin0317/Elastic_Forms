import matplotlib.pyplot as plt
import numpy as np

x = np.arange(3)
years = ['2017', '2018', '2019']
values = [100, 400, 900]

plt.bar(x, values)
plt.xticks(x, years)
plt.savefig('covid19.png')