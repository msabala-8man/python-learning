import numpy as np


# EXERCISE 1
# Create the following 2D NumPy array:
#
# [[10, 20, 30],
#  [40, 50, 60]]
#
# Add 5 to every value using broadcasting.
# Print the original array and the result.

arr_1 = np.array([[10, 20, 30],
                 [40, 50, 60]])

arr_1_modified = arr_1 + 5
print(arr_1)
print(arr_1_modified)

# EXERCISE 2
# Create the following 2D NumPy array:
#
# [[100, 200, 300],
#  [150, 250, 350]]
#
# Create the following 1D NumPy array:
#
# [10, 20, 30]
#
# Subtract the 1D array from every row of the 2D array using broadcasting.
# Print the result.

arr_2_1 = np.array([[100, 200, 300],
                  [150, 250, 350]])
arr_2_2 = np.array([10, 20, 30])
arr_2_1_modified = arr_2_1 - arr_2_2
print(arr_2_1)
print(arr_2_2)
print(arr_2_1_modified)

# EXERCISE 3
# Create the following 2D NumPy array:
#
# [[10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]]
#
# Create the following 1D NumPy array:
#
# [2, 4, 6]
#
# Multiply every row of the 2D array by the 1D array using broadcasting.
# Print the result.

arr_3_1 = np.array([[10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90]])
print(arr_3_1)
arr_3_2 = np.array([2, 4, 6])
print(arr_3_2)
arr_3_1_modified = arr_3_1 * arr_3_2
print(arr_3_1_modified)

# EXERCISE 4
# Create the following 2D NumPy array:
#
# [[100, 200, 300],
#  [150, 250, 350],
#  [120, 220, 320]]
#
# Create the following 1D NumPy array:
#
# [0.9, 0.8, 0.7]
#
# Multiply every row by the corresponding values in the 1D array
# using broadcasting.
# Print the result.

arr_4_1 = np.array([[100, 200, 300],
                    [150, 250, 350],
                    [120, 220, 320]])
print(arr_4_1)
arr_4_2 = np.array([0.9, 0.8, 0.7])
print(arr_4_2)
arr_4_1_modified = arr_4_1 * arr_4_2
print(arr_4_1_modified)

# EXERCISE 5
# Create the following 2D NumPy array:
#
# [[100, 200, 300, 400],
#  [150, 250, 350, 450],
#  [120, 220, 320, 420]]
#
# Create the following 1D NumPy array:
#
# [10, 20, 30, 40]
#
# First subtract the 1D array from every row using broadcasting.
# Then multiply the resulting array by 1.1 using a vectorized operation.
#
# Print the original array and the final result.

arr_5_1 = np.array([[100, 200, 300, 400],
                    [150, 250, 350, 450],
                    [120, 220, 320, 420]])
print(arr_5_1)
arr_5_2 = np.array([10, 20, 30, 40])
print(arr_5_2)
arr_5_1_substract = arr_5_1 - arr_5_2
print(arr_5_1_substract)
arr_5_1_substract_multiply = arr_5_1_substract * 1.1
print(arr_5_1)
print(arr_5_1_substract_multiply)

# EXERCISE 6
# Create a 5x6 NumPy array of random integers from 10 to 100.
#
# Select the last 4 rows and the first 5 columns.
# From this new array, select every second column starting with the first column.
# Increase all selected values by 10 and then multiply them by 1.5.
#
# Print the original array and the final array.
# Then print the mean of the final array for each row.

arr_6 = np.random.randint(10, 101, (5, 6))
print(arr_6)
arr_6_modified = arr_6[-4::, 0:5:]
print(arr_6_modified)
arr_6_modified_2 = arr_6_modified[::, ::2]
print(arr_6_modified_2)
arr_6_modified_2_increase_multiply = (arr_6_modified_2 + 10) * 1.5
print(arr_6)
print(arr_6_modified_2_increase_multiply)
print(np.mean(arr_6_modified_2_increase_multiply, axis=1))

# EXERCISE 7
# Create the following NumPy array:
#
# [12, 45, 12, 78, 34, 45, 12, 90, 34, 56, 78, 12]
#
# Find the unique values and their counts.
# Then find how many times the value 12 appears.
#
# Create a new array containing only values greater than 40.
# Sort the new array in descending order.
#
# Print the unique values, their counts, the count of 12,
# and the final sorted array.

arr_7 = np.array([12, 45, 12, 78, 34, 45, 12, 90, 34, 56, 78, 12])
print(arr_7)
arr_7_unique, arr_7_count = np.unique(arr_7, return_counts=True)
print(arr_7_unique, arr_7_count)
print(arr_7_count[arr_7_unique==12][0])
arr_7_filtered = arr_7[arr_7 > 40]
print(arr_7_filtered)
arr_7_filtered_sort_desc = np.sort(arr_7_filtered)[-1::-1]
print(arr_7_filtered_sort_desc)
print(arr_7_unique, arr_7_count)
print(arr_7_count[arr_7_unique==12][0])
print(arr_7_filtered_sort_desc)

# EXERCISE 8
# Create the following 4x5 NumPy array:
#
# [[45, 12, 78, 34, 91],
#  [63, 27, 84, 15, 52],
#  [39, 96, 21, 73, 58],
#  [81, 44, 67, 29, 88]]
#
# Select the last 3 columns.
# Sort each row in descending order.
#
# Then create a new 1D NumPy array:
#
# [1.0, 0.9, 1.1]
#
# Multiply every row of the sorted array by the corresponding
# value from the 1D array.
#
# Print the sorted array and the final result.
# Then print the mean of each row of the final result.

arr_8 = np.array([[45, 12, 78, 34, 91],
                  [63, 27, 84, 15, 52],   
                  [39, 96, 21, 73, 58],
                  [81, 44, 67, 29, 88]])
print(arr_8)
arr_8_modified = arr_8[::, -3::]
arr_8_modified_sort_desc = np.sort(arr_8_modified, axis=1)[::, -1::-1]
print(arr_8_modified_sort_desc)
arr_8_2 = np.array([1.0, 0.9, 1.1])
print(arr_8_2)
arr_8_modified_sort_desc_multiply = arr_8_modified_sort_desc * arr_8_2
print(arr_8_modified_sort_desc)
print(arr_8_modified_sort_desc_multiply)
print(np.mean(arr_8_modified_sort_desc_multiply, axis=1))

# EXERCISE 9
# Create a 6x5 NumPy array of random integers from 1 to 100.
#
# Select rows 2 through 6 and columns 1, 3, and 5.
# Reverse the order of the selected columns.
#
# Create a new array where:
# - values greater than or equal to 80 become 100
# - values between 40 and 79 stay unchanged
# - values below 40 become 0
#
# Then print:
# - the original array
# - the final array
# - the sum of each row in the final array
# - the index of the row with the largest sum

arr_9 = np.random.randint(1, 101, (6, 5))
print(arr_9)
arr_9_modified_reverse = arr_9[1:6:, [0, 2, 4]][::, -1::-1]
print(arr_9_modified_reverse)
arr_9_modified_reverse_where = np.where(arr_9_modified_reverse >= 80, 100, np.where(arr_9_modified_reverse < 40, 0, arr_9_modified_reverse))
print(arr_9_modified_reverse_where)
total_row = np.sum(arr_9_modified_reverse_where, axis=1)
print(total_row)
print(np.argmax(total_row))

# EXERCISE 10
# # Create a 5x5 NumPy array of random integers from 1 to 100.
#
# Select the first 4 columns.
# Create an index array that sorts each row in ascending order.
# Use the index array to create a sorted version of the selected array.
#
# From the sorted array, select the 2 smallest values from each row.
# Add the following 1D array to these values using broadcasting:
#
# [5, 10]
#
# Then calculate the mean of the resulting array for each row.
#
# Print the original array, the sorted array,
# the final array, and the row means.

arr_10 = np.random.randint(1, 101, (5, 5))
print(arr_10)
arr_10_modified = arr_10[::, 0:4:]
print(arr_10_modified)
arr_10_sort_index = np.argsort(arr_10_modified, axis=1)
print(arr_10_sort_index)
arr_10_take_along_axis = np.take_along_axis(arr_10_modified, arr_10_sort_index, axis=1)
print(arr_10_take_along_axis)
arr_10_2_smallest_values = arr_10_take_along_axis[::, :2:]
print(arr_10_2_smallest_values)
arr_10_2 = np.array([5, 10])
arr_10_2_smallest_values_added = arr_10_2_smallest_values + arr_10_2
print(arr_10_2_smallest_values_added)
print(np.mean(arr_10_2_smallest_values_added, axis=1))
print(arr_10)
print(arr_10_take_along_axis)
print(arr_10_2_smallest_values_added)
print(np.mean(arr_10_2_smallest_values_added, axis=1))