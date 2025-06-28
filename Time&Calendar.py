import calendar
import time

Cal = calendar.month(1945, 4)   # (year, month)
print(Cal)

Ticks = time.time()
Time = time.ctime(Ticks)
print(Time) 
