# Basic Dataset
import numpy as np

heights = [155, 180, 169, 150, 190, 155, 182, 161, 185, 151]
ages = [63, 39, 49, 52, 71, 31, 32, 36, 48, 30]
num = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

# Assigning values in an array
# The origin value of row 1 and col 3 is 3, let's change it manually and using numpy


def assign_value():
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
    print("Before:\n", ha_arr, "\n")
    new_ha = np.array([[200, 100, 150], [20, 30, 25]])
    ha_arr[:, 7:] = new_ha
    print("After:\n", ha_arr, "\n")


heights_arr = np.array(heights)
ages_arr = np.array(ages)


def stacks():
    # Why (10, 1) not (2, 1) or others? This occurs since we want to transpose the array from row to be column
    # heights_arr = heights_arr.reshape(10, 1)
    # ages_arr = ages_arr.reshape(10, 1)
    print("HSTACK")
    h_stack_ha_arr = np.hstack((heights_arr, ages_arr))
    print(h_stack_ha_arr.shape)
    print(h_stack_ha_arr, "\n")

    # Meanwhile if you want to make it vertically, use vstack
    print("VSTACK")
    v_stack_ha_arr = np.vstack((heights_arr, ages_arr))
    print(v_stack_ha_arr.shape)
    print(v_stack_ha_arr, "\n")

    # And by using stack, we may obtain
    print("STACK")
    s_stack_ha_arr = np.stack((heights_arr, ages_arr))
    print(s_stack_ha_arr.shape)
    print(s_stack_ha_arr, "\n")

    # Using axis = 1, it adjust the array to be 2 column
    s_stack_ha_arr = np.stack((heights_arr, ages_arr), axis=1)
    print(s_stack_ha_arr.shape)
    print(s_stack_ha_arr[:3], "\n")


def concatenate():
    # Concatenate
    # Axis = 0 is equals with y and Axis = 1 is equals with x
    print("CONCATENATE")
    # concat_ha = np.concatenate((heights_arr, ages_arr), axis=0)
    # print(concat_ha.shape)
    # print(concat_ha, "\n")

    # WARNING! THIS CONCATENATE IS STILL IN DEVELOPMENT SINCE I ONLY USED 1D ARRAY
    # Debug
    new_heights_arr = heights_arr.reshape(1, 10)
    print(new_heights_arr[:3])
    new_ages_arr = ages_arr.reshape(1, 10)
    print(new_ages_arr[:3], "\n")

    # Concat using axis = 1
    concat_ha = np.concatenate((new_heights_arr, new_ages_arr), axis=0)
    print("Axis 0 =>", concat_ha.shape)
    print(concat_ha[:3], "\n")

    # Debug
    new_heights_arr = heights_arr.reshape(10, 1)
    print(new_heights_arr[:3])
    new_ages_arr = ages_arr.reshape(10, 1)
    print(new_ages_arr[:3], "\n")

    # Concat using axis = 1
    concat_ha = np.concatenate((new_heights_arr, new_ages_arr), axis=1)
    print("Axis 1 =>", concat_ha.shape)
    print(concat_ha[:3], "\n")


def operations():
    print("MATH")
    add_ha = heights_arr + ages_arr
    print("Heights + Ages =", add_ha[:3])
    print("Convert to feet =", heights_arr[:3]*0.0328084)
    print("Sum of Height =", heights_arr.sum())

    # We also can calculate combined data separately to obtain the sum
    new_heights_arr = heights_arr.reshape(10, 1)
    new_ages_arr = ages_arr.reshape(10, 1)
    concat_ha = np.hstack((new_heights_arr, new_ages_arr))
    # Remember, column sums using axis=0 and row sums using axis=1
    print("Sum of Height & Ages Separately (Col)=", concat_ha.sum(axis=0))
    print("Sum of Height & Ages Separately (Row)=", concat_ha.sum(axis=1))

    # Other operations such as max, min, mean works just like sum

    print("COMPARISON")
    # Shows the boolean
    print("Height < 175 =\n", concat_ha[:, 0] < 175)
    # Shows the details & mask variable used for masking/subset
    mask = concat_ha[:, 0] < 175
    count = []
    for i in range(len(concat_ha[:, 0])):
        if mask[i]:
            count.append(i)
    print("Details =", concat_ha[count, 0], "\n")

    # Multiple Selection
    print("Height < 175 && Ages < 40 =\n", (concat_ha[:, 0] < 175) & (concat_ha[:, 1] < 40))
    mask_ha = (concat_ha[:, 0] < 175) & (concat_ha[:, 1] < 40)
    count_ha = []
    for i in range(len(concat_ha[:, 0])):
        if mask_ha[i]:
            count_ha.append(i)
    print("Details =\n", np.transpose(concat_ha[count_ha]), "\n")


def main():
    # assign_value()
    # stacks()
    # concatenate()
    operations()


if __name__ == "__main__":
    main()
