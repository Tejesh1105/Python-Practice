# Create a python program capable of greeting you with Good Morning, Good Afternoon and
# Good Evening. Your program should use time module to get the current hour.

import time

current_time = time.localtime()
hour = current_time.tm_hour  
# gets the hour (0-23)

if 5 <= hour < 12:
    print("Good Morning Sir")
elif 12 <= hour < 17:
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")
