
import matplotlib.pyplot as plt

categories = ['Sleep', 'Classes', 'Eating', 'Studying', 'Free Time']
hours = [14, 9, 4, 13, 6]

plt.bar(categories, hours, color=['blue', 'green', 'orange', 'red', 'purple', 'brown'])
plt.title('Time Spent in Different Activities Over 2 Days')
plt.xlabel('Categories')
plt.ylabel('Hours')
plt.show()

