import pandas as pd
import numpy as np
import string
import random
import matplotlib.pyplot as plt

m = 28
n = 15

def random_data(m, n):
    return np.cumsum(np.random.randn(m*n)).reshape(m, n)

def id_generator(number, size=6, chars=string.ascii_uppercase + string.digits):
    sequence = []
    for n in range(number):
        sequence.append(''.join(random.choice(chars) for _ in range(size)))
    return sequence

df = pd.DataFrame(random_data(n, m), columns=id_generator(number=m, size=3))
print(df)

fig2, axes = plt.subplots(nrows=4, ncols=7)
for i, ax in enumerate(axes.flatten()):
    df[df.columns[i]].plot(ax=ax)
    ax.set_title(df.columns[i])

plt.show()