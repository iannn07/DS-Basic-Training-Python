# Welcome to Data Science!

# Numerical Data using Numpy
# Basic Dataset
import numpy as np
heights = [155, 180, 169, 150, 190, 155, 182, 161, 185, 151]
ages = [63, 39, 49, 52, 71, 31, 32, 36, 48, 30]
num = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

# Using Numpy vs Don't w/ expected result is 3
# No Numpy
print("No Numpy")
no_count = 0
for i in heights:
    if i > 180:
        no_count += 1
print("Number of Height more than 180 =", no_count, "\n")

# Using Numpy
print("Using Numpy")
heights_arr = np.array(heights)
print(heights_arr)
np_count = heights_arr > 180
print("Number of Height more than 180 =", np_count.sum(), "\n")

# Size vs Shape
print("Size vs Shape in Array")
print(heights_arr.size, heights_arr.shape)
# Size is used to determine the size of an array
# Shape is used to determine the dimension of an array
num_arr = np.array(num)
print(num_arr.size, num_arr.shape, "\n")
# The shape of num_arr is (2, 5), represents 2 rows, 5 columns

# Reshape
print("Reshape combined array")
merge = heights + ages
merge_arr = np.array(merge)
print(merge_arr.shape, "\n")
print(merge_arr.reshape(2, 10))
