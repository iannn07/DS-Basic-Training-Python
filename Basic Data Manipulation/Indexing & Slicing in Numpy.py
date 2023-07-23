# Basic Dataset
import numpy as np
heights = [155, 180, 169, 150, 190, 155, 182, 161, 185, 151]
ages = [63, 39, 49, 52, 71, 31, 32, 36, 48, 30]
num = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

# Indexing an array
print("Indexing")
print("Heights (1D):", heights[2])
print("Num (2D):", num[1][2])
# If we use Numpy to access an array, we may obtain
num_arr = np.array(num)
print("Num (Numpy):", num_arr[1,1])

# Slicing an array
# This will slice an array from the bottom index up to the n-1 of the end index
print("Slicing")
print("Num (Normal):", num[0][1:3])
print("Num (Numpy):", num_arr[1, 0:3])
print("Num (Second row):", num_arr[1, :])
print("Num (All row):\n", num_arr[:, :3])
print("Num (Start Value):", num_arr[0, 1:])

# NOTE: The indexing in Py and R is different. Py starts from 0, R starts from 1.
