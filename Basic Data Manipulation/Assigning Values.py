# Basic Dataset
import numpy as np
heights = [155, 180, 169, 150, 190, 155, 182, 161, 185, 151]
ages = [63, 39, 49, 52, 71, 31, 32, 36, 48, 30]
num = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

# Assigning values in an array
# The origin value of row 1 and col 3 is 3, let's change it manually and using numpy
print("Assigning Values")
print("Manually:")
num[0][2] = 100
print(num)
print("Numpy")
num_arr = np.array(num)
num_arr[0, 2] = 100
print(num_arr, "\n")

# Let's implement slicing too!
print("Implemented using slicing")
num_arr[:, 2] = 100
print(num_arr, "\n")

# We also can combine them from array to array
print("Merge two array")
heights_ages = heights + ages
ha_arr = np.array(heights_ages)
ha_arr = ha_arr.reshape(2, 10)
print(ha_arr)
new_ha = np.array([[200, 100, 150], [20, 30, 25]])
ha_arr[:, 7:] = new_ha
print(ha_arr)
