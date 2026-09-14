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