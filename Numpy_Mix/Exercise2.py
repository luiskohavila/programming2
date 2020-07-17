# Luis Fernando Koh Avila
# Data 2 B

# Exercise 2. Matrix Operations using Numpy Functions

import numpy as np

# Matrix Addition Function
def sum_matrix(m1,m2,m3):
  for i in range (len(m1)):  # Pass through the number of rows in A
        for j in range(len(m2)):  # Pass through the number of Columns in B
          m3[i][j] += m1[i][j] + m2[i][j] # Sum and save the values
  return m3

# Matrix Multiplication Function
def matrix_multiplication(m1,m2,m3):   
    for i in range (len(m1)): # Pass through the number of rows in A
        for j in range(len(m2[0])): # Pass through the number of Columns in B
            for k in range(len(m1[0])): # Pass through the index of A and  B
                m3[i][j] += m1[i][k] * m2[k][j] # Multiply and save the value        
    return m3

# Ask for the size
size = int(input("What square matrixes do you want?: "))

# Creating identity matrix with the size and numpy's function .identity
matrixa = np.identity(size)
matrixb = np.identity(size)

# Creating matrixes to do the operations and fill them with 0s
#  with numpy's function .full
matrixcsum = np.full((size,size), 0)
matrixcmult = np.full((size,size), 0)

# Printing matrixes
print(f"\nThe matrix A: \n{matrixa}")
print(f"\nThe matrix B: \n{matrixb}")

# Trasposing matrixes with numpy's function .T
matrixa = matrixa.T
print(f"\nTransposed matrix A: \n{matrixa}")
matrixb = matrixb.T
print(f"\nTransposed matrix B: \n{matrixb}")

# Calling function to sum matrixes and display the result
matrixcsum = sum_matrix(matrixa,matrixb,matrixcsum)
print(f"\nThe matrix sum of the matrixes is: \n {matrixcsum}")

# Calling function to multiply matrixes and display the result
matrixcmult = matrix_multiplication(matrixa,matrixb,matrixcmult)
print(f"\nThe matrix multiplication of the matrixes is: \n {matrixcmult}")

# Merge the matrixes sum and mult with numpy's function .r_
matrixc3 = (np.r_[matrixcsum, matrixcmult])
print(f"\nMerged matrixes: \n{matrixc3}")

# Output:
"""
What square matrixes do you want?: 3

The matrix A: 
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

The matrix B: 
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

Transposed matrix A: 
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

Transposed matrix B: 
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

The matrix sum of the matrixes is: 
 [[2 0 0]
 [0 2 0]
 [0 0 2]]

The matrix multiplication of the matrixes is: 
 [[1 0 0]
 [0 1 0]
 [0 0 1]]

Merged matrixes: 
[[2 0 0]
 [0 2 0]
 [0 0 2]
 [1 0 0]
 [0 1 0]
 [0 0 1]]
"""
