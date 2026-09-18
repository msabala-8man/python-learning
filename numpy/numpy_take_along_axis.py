import numpy as np


# EXERCISE 1:
# Create the following array:
#
# [[10, 30, 20],
#  [60, 40, 50]]
#
# Create the following index array:
#
# [[2, 0, 1],
#  [1, 2, 0]]
#
# Use np.take_along_axis() to create a new array
# using the indices from the index array along axis=1.
# Print the result.

arr_1 = np.array([[10, 30, 20],
                  [60, 40, 50]])
arr_1_index = np.array([[2, 0, 1],
                        [1, 2, 0]])
arr_1_take_along_axis = np.take_along_axis(arr_1, arr_1_index, axis=1)
print(arr_1_take_along_axis)

# EXERCISE 2:
# Create the following array:
#
# [[15, 40, 25, 30],
#  [80, 50, 70, 60]]
#
# Create the following index array:
#
# [[0, 2, 3, 1],
#  [1, 3, 2, 0]]
#
# Use np.take_along_axis() with axis=1.
# Print the result.

arr_2 = np.array([[15, 40, 25, 30],
                  [80, 50, 70, 60]])
arr_2_index = np.array([[0, 2, 3, 1],
                        [1, 3, 2, 0]])
print(np.take_along_axis(arr_2, arr_2_index, axis=1))

# EXERCISE 3:
# Create the following array:
#
# [[11, 22, 33],
#  [44, 55, 66],
#  [77, 88, 99]]
#
# Create the following index array:
#
# [[2, 1, 0],
#  [0, 2, 1],
#  [1, 0, 2]]
#
# Use np.take_along_axis() with axis=1.
# Print the result.

arr_3 = np.array([[11, 22, 33],
                  [44, 55, 66],
                  [77, 88, 99]])
arr_3_index = np.array([[2, 1, 0],
                       [0, 2, 1],
                       [1, 0, 2]])
print(np.take_along_axis(arr_3, arr_3_index, axis=1))

# EXERCISE 4:
# Create the following array:
#
# [[100, 200, 300, 400],
#  [500, 600, 700, 800]]
#
# Create an index array that reverses the columns of each row.
#
# Use np.take_along_axis() with axis=1.
# Print the result.

arr_4 = np.array([[100, 200, 300, 400],
                  [500, 600, 700, 800]])
arr_4_column_reverse_index = np.array([[3, 2, 1, 0],
                                       [3, 2, 1, 0]])
print(np.take_along_axis(arr_4, arr_4_column_reverse_index, axis=1))


# EXERCISE 5:
# Create the following array:
#
# [[45, 12, 78, 34],
#  [91, 23, 56, 67],
#  [38, 84, 15, 72]]
#
# First create an index array using np.argsort()
# that sorts each row in ascending order.
#
# Then, use np.take_along_axis() to create a new array
# in which each row is sorted in ascending order.
#
# Print the index array and the final sorted array.

arr_5 = np.array([[45, 12, 78, 34],
                  [91, 23, 56, 67],
                  [38, 84, 15, 72]])
arr_5_argsort = np.argsort(arr_5, axis=1)
print(arr_5_argsort)
print(np.take_along_axis(arr_5, arr_5_argsort, axis=1))

###########################################################################

import numpy as np


# EXERCISE 6:
# Create a 4x6 array of random integers from 10 to 50.
#
# Select rows 2 through 4 and columns 2 through 5.
#
# Print the selected part of the array.

arr_6 = np.random.randint(10, 51, (4, 6))
print(arr_6)
arr_6_modified = arr_6[1:4:, 1:5:]
print(arr_6_modified)

# EXERCISE 7:
# Create a 3x5 array of random integers from 1 to 100.
#
# Select every second column, starting from the first column.
#
# Then reverse the order of the selected columns.
#
# Print the final array.

arr_7 = np.random.randint(1, 101, (3, 5))
print(arr_7)
arr_7_modified = arr_7[::, 0::2]
print(arr_7_modified)
arr_7_modified_reverse = arr_7_modified[::, -1::-1]
print(arr_7_modified_reverse)

# EXERCISE 8:
# Create the following array:
#
# [[15, 40, 25, 60],
#  [80, 30, 50, 10],
#  [45, 70, 20, 90]]
#
# Create an index array that rearranges the columns of each row
# in the following order:
#
# third column, first column, fourth column, second column
#
# Use np.take_along_axis() to create the new array.
#
# Print the result.

arr_8 = np.array([[15, 40, 25, 60],
                  [80, 30, 50, 10],
                  [45, 70, 20, 90]])
print(arr_8)
arr_8_index = np.array([[2, 0, 3, 1],
                        [2, 0, 3, 1],
                        [2, 0, 3, 1]])
print(arr_8_index)
arr_8_take_along_axis = np.take_along_axis(arr_8, arr_8_index, axis=1)
print(arr_8_take_along_axis) 

# EXERCISE 9:
# Create a 5x5 array of random integers from 1 to 100.
#
# Select the last three rows.
#
# From this new array, select the first, third and fifth columns.
#
# Then reverse the order of the columns.
#
# Print the final array.

arr_9 = np.random.randint(1, 101, (5, 5))
print(arr_9)
arr_9_modified_1 = arr_9[-3::, ::]
print(arr_9_modified_1)
arr_9_modified_2 = arr_9_modified_1[::, [0, 2, 4]]
print(arr_9_modified_2)
arr_9_modified_2_reverse = arr_9_modified_2[::, -1::-1]
print(arr_9_modified_2_reverse)

# EXERCISE 10:
# Create a 4x6 array of random integers from 1 to 100.
#
# First select rows 1 through 4 and every second column,
# starting from the second column.
#
# Then create an index array using np.argsort()
# that sorts each row of this new array in ascending order.
#
# Use np.take_along_axis() to create a sorted version of the new array.
#
# Print the index array and the final sorted array.

arr_10 = np.random.randint(1, 101, (4, 6))
print(arr_10)
arr_10_modified_1 = arr_10[0:4:, 1::2]
print(arr_10_modified_1)
arr_10_argsort = np.argsort(arr_10_modified_1, axis=1)
print(arr_10_argsort)
arr_10_take_along_axis = np.take_along_axis(arr_10_modified_1, arr_10_argsort, axis=1)
print(arr_10_take_along_axis)
