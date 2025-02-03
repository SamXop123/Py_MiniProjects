
import matplotlib.pyplot as plt

activities = ['eat', 'sleep', 'work', 'play']
slices=[3,7,8,6]
colors=['r','y','g','b']
plt.pie(slices, labels=activities, colors=colors)
plt.show()

