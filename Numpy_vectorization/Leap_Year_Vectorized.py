# Luis Fernando Koh Avila
# Data 2 B

import numpy as np
from datetime import datetime

start_time = datetime.now() # Starting counting time while running the code

# Leap Year
"""
# Leap Year using for loop

counter = 0

for year in range(1500,2100):
  if (year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
    print(f"{year}\n")
    counter += 1
print(f"The total of leap year is: {counter}")

# Duration: 0:00:00.002503
"""

# Leap Year Vectorized

year = np.arange(start=1500, stop=2101) # Definin an array from 1500 to 2100

# Print the years that follows the leap condition
print(year[((year%400 == 0) | (year%4==0) & (year%100 != 0))])

# Count all the values that follows the condition with np.sum
print(f"\nThe total of leap years are: {np.sum((year%4==0) & (year%100 != 0) | (year%400 == 0))}")

# Duration: 0:00:00.000984

end_time = datetime.now() # Taking the current time

# Subtract the time at the beginning mnus the end time in order to find how many time
# the operation took
print("\nDuration: {}".format(end_time - start_time))
