# Luis Fernando Koh Avila
# Data 2 B

import pandas as pd
import numpy as np

# Manipulation of an excel using Pandas

# Step 1: First it is necessary to open the files with the grades as a data frame
df = pd.read_excel('grades.xlsx')

# Step 2: The teacher wants to calificate in order to put the score of the first in list
print("\nFirst students in list:")
print(df.head())

# Step 3: The teacher wants to calificate in order to put the score of the last in list
print("\nLast students in list:")
print(df.tail())

# Step 4: The teacher noticed that he wrote wrong the Dianas's score from Unit I 
# so he decided to change it
df.iat[5,1] = '9'
print("\nList correcting Diana's score:")
print(df)

# Step 5: Teacher decided to add the scores of the Unit III in his list
df.insert(3, "Unit III", [10, 9, 9, 10, 6, 8, 10, 9, 10], True)
print("\nScores with Unit 3 added:")
print(df)

# Step 6: Then teacher wants to know what are the means for each score in the unit and the absences
mean = df.mean(axis = 0)
print("\nThe mean for each category: ")
print(mean)

# Step 7: The teacher saw that Luis and Isabel have had a good performance
# so he decided to give them an extra points in another list
print(f"\nExtra points:{pd.DataFrame([2,1],index = ['Luis Koh','Isabel Camara'])}")

# Step 8: Teacher noticed that Maio Solorzano drop off from school so he decided
# to delete him from the list
df = df.drop(df.index[4])
print("\nUpdated list: ")
print(df)

# Output
"""
First students in list:
           Students  Unit I  Unit II  Absences
0          Luis Koh      10       10         0
1      Saul Barrera       8        9         2
2  Matthew Esquivel       9        9         1
3     Juan Balanzar       8        9         4
4   Mario Solorzano       8        8         2

Last students in list:
          Students  Unit I  Unit II  Absences
4  Mario Solorzano       8        8         2
5     Diana Rivero       7        7         5
6    Osiris Camara       9       10         1
7     Victor Uribe       9        9         1
8    Isabel Camara      10        9         0

List correcting Diana's score:
           Students  Unit I  Unit II  Absences
0          Luis Koh      10       10         0
1      Saul Barrera       8        9         2
2  Matthew Esquivel       9        9         1
3     Juan Balanzar       8        9         4
4   Mario Solorzano       8        8         2
5      Diana Rivero       9        7         5
6     Osiris Camara       9       10         1
7      Victor Uribe       9        9         1
8     Isabel Camara      10        9         0

Scores with Unit 3 added:
           Students  Unit I  Unit II  Unit III  Absences
0          Luis Koh      10       10        10         0
1      Saul Barrera       8        9         9         2
2  Matthew Esquivel       9        9         9         1
3     Juan Balanzar       8        9        10         4
4   Mario Solorzano       8        8         6         2
5      Diana Rivero       9        7         8         5
6     Osiris Camara       9       10        10         1
7      Victor Uribe       9        9         9         1
8     Isabel Camara      10        9        10         0

The mean for each category: 
Unit I      8.888889
Unit II     8.888889
Unit III    9.000000
Absences    1.777778
dtype: float64

Extra points:               0
Luis Koh       2
Isabel Camara  1

Updated list: 
           Students  Unit I  Unit II  Unit III  Absences
0          Luis Koh      10       10        10         0
1      Saul Barrera       8        9         9         2
2  Matthew Esquivel       9        9         9         1
3     Juan Balanzar       8        9        10         4
5      Diana Rivero       9        7         8         5
6     Osiris Camara       9       10        10         1
7      Victor Uribe       9        9         9         1
8     Isabel Camara      10        9        10         0
"""
