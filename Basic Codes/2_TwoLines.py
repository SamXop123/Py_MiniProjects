
import matplotlib.pyplot as plt

x1 = [1,2,3,4]
y1 = [1,2,3,4]
plt.plot(x1, y1, label="line 1")

x2 = [1,2,3,4]
y2 = [4,3,2,1]
plt.plot(x2, y2, label="line 2")

plt.xlabel('x-axis', fontsize=16)
plt.ylabel('y-axis', fontsize=16)
plt.title('Two lines on same graph')
plt.legend()

plt.show()

