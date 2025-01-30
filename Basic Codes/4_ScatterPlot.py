
# Data plotting

import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8,9,10]
y=[2,4,5,7,6,8,9,11,12,12]
plt.scatter(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter plot')
plt.xticks(np.arange(min(x), max(x),1.0))
plt.show()

