
import matplotlib.pyplot as plt
import numpy as np

y=[1,2,3,4]
abc = ["one", "two", "three", "four"]

plt.bar(np.arange(len(y)), y,tick_label=abc, widht=0.4)

plt.show()