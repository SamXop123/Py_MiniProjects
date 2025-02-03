
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

plt.axes(projection='3d')

x = [1,2,3,4,5]
y = [3,5,2,1,4]
z = [5,2,1,4,3]

plt.plot(x,y,z)
plt.show()