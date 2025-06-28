
"""
Create dataset of your life at VIT Bhopal campus in the span of
24hrs for 2 days.
"""

import matplotlib.pyplot as plt

categories = ['Sleep', 'Classes', 'Eating', 'Exercise', 'Studying', 'Free Time']
hours = [14, 9, 4, 2, 13, 6]

plt.bar(categories, hours, color=['blue', 'green', 'orange', 'red', 'purple', 'brown'])
plt.title('Time Spent in Different Activities Over 2 Days')
plt.xlabel('Categories')
plt.ylabel('Hours')
plt.show()

