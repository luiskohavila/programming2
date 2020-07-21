# Luis Fernando Koh Avila
# Data 2 B
import numpy as np
from datetime import datetime

start_time = datetime.now() # Starting counting time while running the code

# Matrix addition
"""
# Matriz addition using for loops

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[9,8,7],[6,5,4],[3,2,1]]

c = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(a)):
  for j in range(len(a[0])):
    c[i][j] = a[i][j] + b[i][j]

for i in c:
  print(i)

# Duration: 0:00:00.000080
"""

# Matriz addition vectorized

# Creating the numpy arrays with np and put the values
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[9,8,7],[6,5,4],[3,2,1]])

# Being these ones numpy arrays we are capable to sum their respectives
# values in with its same positions
print(a + b)

# Duration: 0:00:00.000042

end_time = datetime.now() # Taking the current time

# Subtract the time at the beginning mnus the end time in order to find how many time
# the operation took
print("\nDuration: {}".format(end_time - start_time))
