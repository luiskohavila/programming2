# Luis Fernando Koh Avila
# Data 2 B

# Exercise 1. We want to know the statistic information of profits from a
# company the last year, to to this we have the current information
# for the earned money each month

import numpy as np
from scipy import stats

# Use the np.array function to define a list and passing the values
earnings = np.array([1500, 2100, 3000, 2500, 2100, 4000, 3200, 2000, 3500, 4000, 2700, 1900])
print(f"The earning for the 2019 are: {earnings}")

# Displayin a list of the earning vertically
vertically = earnings.reshape(12,-1)
print(f"\nThe earning per month ordered: \n{vertically}")

# Calculating the average of sales in the year
average = np.mean(earnings)
print(f"\nThe average of sales for the 2019 are: {average} dollars")

# Calculating the median of sales in the year
median = np.median(earnings)
print(f"\nThe median of sales for the 2019 are: {median} dollars")

# Calculating the mode of sales in the year
mode = stats.mode(earnings)
print(f"\nThe mode of sales for the 2019 are: {mode} dollars")

# Calculating the variance of sales in the year
variance = np.var(earnings, dtype=np.float64)
print(f"\nThe variance of sales for the 2019 is: {variance}")

# Calculating the standard deviation of sales in the year
standard_deviation = np.std(earnings, dtype=np.float64)
print(f"\nThe standard deviation of sales for the 2019 is: {standard_deviation}")


# Output:
"""
The earning for the 2019 are: [1500 2100 3000 2500 2100 4000 3200 2000 3500 4000 2700 1900]

The earning per month ordered: 
[[1500]
 [2100]
 [3000]
 [2500]
 [2100]
 [4000]
 [3200]
 [2000]
 [3500]
 [4000]
 [2700]
 [1900]]

The average of sales for the 2019 are: 2708.3333333333335 dollars

The median of sales for the 2019 are: 2600.0 dollars

The mode of sales for the 2019 are: ModeResult(mode=array([2100]), count=array([2])) dollars

The variance of sales for the 2019 is: 640763.8888888889

The standard deviation of sales for the 2019 is: 800.4772881780525
"""
