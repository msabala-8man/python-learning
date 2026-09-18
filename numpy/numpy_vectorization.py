import numpy as np


# EXERCISE 1
# Create the following NumPy array:
#
# [10, 20, 30, 40, 50]
#
# Multiply every value by 3 using a vectorized operation.
# Print the original array and the new array.

arr_1 = np.array([10, 20, 30, 40, 50])
arr_1_multiply = arr_1 * 3
print(arr_1, arr_1_multiply)

# EXERCISE 2
# Create the following NumPy array of prices:
#
# [100, 250, 80, 300, 150]
#
# Increase every price by 15% using a vectorized operation.
# Print the original prices and the new prices.

arr_2 = np.array([100, 250, 80, 300, 150])
arr_2_modified = arr_2 * 1.15
print(arr_2, arr_2_modified)

# EXERCISE 3
# Create the following two NumPy arrays:
#
# prices    = [100, 200, 150, 300, 250]
# quantities = [  2,   3,   4,   1,   2]
#
# Calculate the revenue for each item using a vectorized operation.
# Print the revenue array.
# Then print the total revenue.

arr_3_prices = np.array([100, 200, 150, 300, 250])
arr_3_quantities = np.array([2, 3, 4, 1, 2])
arr_3_revenu = arr_3_prices * arr_3_quantities
print(arr_3_prices, arr_3_quantities, np.sum(arr_3_revenu))

# EXERCISE 4
# Create the following NumPy array:
#
# [45, 72, 58, 91, 63, 39, 84]
#
# Calculate a new array where every value is increased by 10
# and then multiplied by 2.
#
# Print the original array and the new array.

arr_4 = np.array([45, 72, 58, 91, 63, 39, 84])
arr_4_modified = (arr_4 + 10) * 2
print(arr_4, arr_4_modified)

# EXERCISE 5
# Create the following NumPy array of returns:
#
# [0.8, -0.4, 1.2, -1.1, 0.3, 1.8, -0.7, 0.5]
#
# Create a new array where:
# - positive values are multiplied by 2
# - negative values are multiplied by 3
#
# Use a vectorized solution.
# Print the original array and the new array.

arr_5 = np.array([0.8, -0.4, 1.2, -1.1, 0.3, 1.8, -0.7, 0.5])
arr_5_modified = np.where(arr_5 > 0, arr_5 * 2, np.where(arr_5 < 0, arr_5 * 3, arr_5))
print(arr_5, arr_5_modified)

# EXERCISE 6
# Create a 5x6 NumPy array of random integers from 10 to 100.
#
# Select the last 3 rows of the array.
# From this new array, select every second column starting with the first column.
# Increase every selected value by 5 and then multiply the result by 2.
# Print the original array and the final array.

arr_6 = np.random.randint(10, 101, (5, 6))
print(arr_6)
arr_6_modified_1 = arr_6[-3::, ::]
print(arr_6_modified_1)
arr_6_modified_2 = arr_6_modified_1[::, 0::2]
print(arr_6_modified_2)
arr_6_modified_3 = (arr_6_modified_2 + 5) * 2
print(arr_6)
print(arr_6_modified_3)

# EXERCISE 7
# Create a 4x5 NumPy array of random integers from 1 to 100.
#
# Create a new array where:
# - values greater than 70 are multiplied by 1.2
# - values between 40 and 70 are increased by 5
# - values below 40 are replaced with 40
#
# Print the original array and the modified array.
#
# Then print the mean of the modified array for each row.

arr_7 = np.random.randint(1, 101, (4, 5))
arr_7_modified = np.where(arr_7 > 70, arr_7 * 1.2, np.where(arr_7 < 40, 40, arr_7 + 5))
print(arr_7)
print(arr_7_modified)
print(np.mean(arr_7_modified, axis=1))

# EXERCISE 8
# Create the following 3x5 NumPy array:
#
# [[45, 12, 78, 34, 91],
#  [63, 27, 84, 15, 52],
#  [39, 96, 21, 73, 58]]
#
# First select the last 4 columns.
# Then create an index array that sorts each row in ascending order.
# Use the index array to create a new array with each row sorted.
#
# Print the selected array, the index array, and the final sorted array.
#
# Then print the largest value from each row of the sorted array.

arr_8 = np.array([[45, 12, 78, 34, 91],
                  [63, 27, 84, 15, 52],
                  [39, 96, 21, 73, 58]])

arr_8_modified = arr_8[::, -4::]
print(arr_8_modified)
arr_8_modified_argsort = np.argsort(arr_8_modified, axis=1)
print(arr_8_modified_argsort)
arr_8_modified_argsort_order = np.take_along_axis(arr_8_modified, arr_8_modified_argsort, axis=1)
print(arr_8_modified)
print(arr_8_modified_argsort)
print(arr_8_modified_argsort_order)
print(arr_8_modified_argsort_order[::, -1::])

# EXERCISE 9
# Create a 6x5 NumPy array of random integers from 10 to 100.
#
# Select rows 2 through 6 and columns 1, 3, and 5.
# From this new array, reverse the order of the columns.
#
# Create a new array where:
# - values greater than or equal to 80 become 100
# - values between 50 and 79 stay unchanged
# - values below 50 become 0
#
# Print the original array and the final array.
# Then print the mean of the final array for each row.

arr_9 = np.random.randint(10, 101, (6, 5))
print(arr_9)
arr_9_modified = arr_9[1:6:, [0, 2, 4]]
print(arr_9_modified)
arr_9_modified_reverse = arr_9_modified[::, -1::-1]
print(arr_9_modified_reverse)
arr_9_modified_reverse_filter = np.where(arr_9_modified_reverse < 50, 0, 
                                         np.where(arr_9_modified_reverse >= 80, 100, arr_9_modified_reverse))
print(arr_9)
print(arr_9_modified_reverse_filter)
print(np.mean(arr_9_modified_reverse_filter, axis=1))

# EXERCISE 10
# Create a 5x6 NumPy array of random integers from 1 to 100.
#
# Select the last 4 rows and the first 5 columns.
# Create an index array that sorts each row in descending order.
# Use that index array to create a new array with each row sorted in descending order.
#
# From the sorted array, select the first 3 columns.
# Increase all selected values by 10% using a vectorized operation.
#
# Print:
# - the original array
# - the sorted array
# - the final array
#
# Then print the mean of the final array for each row.

arr_10 = np.random.randint(1, 100, (5, 6))
print(arr_10)
arr_10_modified = arr_10[-4::, 0:5:]
print(arr_10_modified)
arr_10_modified_argsort_desc = np.argsort(arr_10_modified)[::, -1::-1]
print(arr_10_modified_argsort_desc)
arr_10_modified_argsort_desc_order = np.take_along_axis(arr_10_modified, arr_10_modified_argsort_desc, axis=1)
print(arr_10_modified_argsort_desc_order)
arr_10_modified_argsort_desc_order_modified = arr_10_modified_argsort_desc_order[::, 0:3:]
print(arr_10_modified_argsort_desc_order_modified)
arr_10_modified_argsort_desc_order_modified_multiply = arr_10_modified_argsort_desc_order_modified * 1.1
print(arr_10)
print(arr_10_modified_argsort_desc_order)
print(arr_10_modified_argsort_desc_order_modified_multiply)