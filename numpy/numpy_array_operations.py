import numpy as np

np.set_printoptions(suppress=True)
# 
# EXERCISE 1/5:
#
# Create a 1D array containing numbers from 1 to 12.
# Reshape it into a 3x4 matrix.
# Print the matrix and its shape.

arr = np.array([1, 2, 3, 4, 5, 6, 7 ,8 ,9 , 10, 11, 12])
arr_reshaped = arr.reshape(3, 4)
print(arr_reshaped, arr_reshaped.shape)


# EXERCISE 2/5:
#
# Create the following matrix:
#
# [[10, 20, 30],
#  [40, 50, 60]]
#
# Transpose the matrix.
# Print the result and its shape.

matrix = np.array([[10, 20, 30],
                   [40, 50, 60]])


matrix_transposition = matrix.T
print(matrix_transposition, matrix_transposition.shape)

# EXERCISE 3/5:
#
# Create the following matrix:
#
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
#
# Convert the matrix into a 1D array using flatten().
# Print the result and its shape.

matrix2 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix_flatten = matrix2.flatten()
print(matrix_flatten, matrix_flatten.shape)

# EXERCISE 4/5:
#
# Create two 1D arrays:
#
# first = [10, 20, 30]
# second = [40, 50, 60]
#
# Concatenate them into one array.
# Print the result and its shape.

arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50 ,60])

arr_concatenate = np.concatenate((arr1, arr2))
print(arr_concatenate, arr_concatenate.shape)

# EXERCISE 5/5:
#
# Create a 1D array containing numbers from 1 to 12.
# Split it into 4 equal parts.
# Print each part separately.

arr5 = np.array([1, 2, 3, 4, 5, 6, 7 ,8 ,9 , 10, 11, 12])
arr_split = np.split(arr5, 4)
print(arr_split[0], arr_split[1], arr_split[2], arr_split[3])


# EXERCISE 6/10:
#
# Create a 1D NumPy array containing numbers from 1 to 24.
# Reshape it into a 4x6 matrix.
# Print the matrix and its shape.
# Then calculate the mean of each row.

arr_6 = np.array([1, 2, 3, 4, 5, 6, 7 ,8 , 9, 10, 11, 12, 
                  13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

arr_6_reshape = arr_6.reshape(4, 6)
print(arr_6_reshape, arr_6_reshape.shape)

# EXERCISE 7/10:
#
# Create the following matrix:
#
# [[10, 20, 30, 40],
#  [50, 60, 70, 80],
#  [90, 100, 110, 120]]
#
# Transpose the matrix.
# Then calculate the sum of each row of the transposed matrix.
# Print the transposed matrix and the row sums.

matrix_7 = np.array([[10, 20, 30, 40],
            [50, 60, 70, 80],
            [90, 100, 110, 120]])

matrix_7_transpose = matrix_7.T
print(matrix_7_transpose, np.sum(matrix_7_transpose, axis=1))


# EXERCISE 8/10:
#
# Create the following two arrays:
#
# first = [1, 2, 3, 4, 5]
# second = [6, 7, 8, 9, 10]
#
# Concatenate them into one array.
# Reshape the result into a 2x5 matrix.
# Print the final matrix and its shape.

arr_8_1 = np.array([1, 2, 3, 4, 5])
array_8_2 = np.array([6, 7, 8, 9, 10])

arr_8_concatenate = np.concatenate((arr_8_1, array_8_2))
arr_8_reshape = arr_8_concatenate.reshape(2, 5)
print(arr_8_reshape, arr_8_reshape.shape)

# EXERCISE 9/10:
#
# Create the following matrix:
#
# [[10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90],
#  [100, 110, 120]]
#
# Flatten the matrix into a 1D array.
# Split the resulting array into 4 equal parts.
# Print each part separately.

matrix_9 = np.array([[10, 20, 30],
[40, 50, 60],
[70, 80, 90],
[100, 110, 120]])

matrix_9_flatten = matrix_9.flatten()
matrix_9_split = np.split(matrix_9_flatten, 4)
print(matrix_9_split[0], matrix_9_split[1], matrix_9_split[2], matrix_9_split[3])

# EXERCISE 10/10:
#
# Create a 1D NumPy array containing numbers from 1 to 30.
#
# 1. Reshape it into a 5x6 matrix.
# 2. Transpose the matrix.
# 3. Flatten the transposed matrix.
# 4. Split the resulting 1D array into 3 equal parts.

arr_10= np.array([1, 2, 3, 4, 5, 6, 7 ,8 , 9, 10, 11, 12, 
                  13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

arr_10_reshape = arr_10.reshape(5, 6)
arr_10_transpose = arr_10_reshape.T
arr_10_flatten = arr_10_transpose.flatten()
arr_10_split = np.split(arr_10_flatten, 3)
print(arr_10_split[0], arr_10_split[1], arr_10_split[2])

# Print the final three parts separately.

##########################################################################

# EXERCISE 11
#
# Create a 1D NumPy array containing:
# [120, 250, 180, 300, 90, 420]
#
# 1. Convert it into a 2D array with 2 rows and 3 columns.
# 2. Convert the original 1D array into a column.
# 3. Convert the original 1D array into a row.
# 4. Print all three arrays and their shapes.

arr_11 = np.array([120, 250, 180, 300, 90, 420])
print(arr_11)
arr_11_reshape = arr_11.reshape(2, 3)
print(arr_11_reshape, arr_11_reshape.shape)
arr_11_column = arr_11[:, np.newaxis]
print(arr_11_column, arr_11_column.shape)
arr_11_row = arr_11[np.newaxis, :]
print(arr_11_row, arr_11_row.shape)

# EXERCISE 12
#
# Create the following two arrays:
#
# prices = [100, 200, 150, 300]
# quantities = [2, 3, 4, 1]
#
# 1. Combine them into one 2D array where:
#    - first column = prices
#    - second column = quantities
# 2. Create a third column containing the transaction value
#    (price multiplied by quantity).
# 3. Add this third column to your 2D array.
# 4. Print the final array and its shape.
#
# The final array should have 3 columns.

prices = np.array([100, 200, 150, 300])
print(prices)
quantities = np.array([2, 3, 4, 1])
print(quantities)
arr_12 = np.column_stack((prices, quantities))
print(arr_12, arr_12.shape)
transaction_value = prices * quantities
print(transaction_value, transaction_value.shape)
transaction_value_column = transaction_value[:, np.newaxis]
print(transaction_value_column, transaction_value_column.shape)
arr_12_column_added = np.column_stack((arr_12, transaction_value_column)) 
print(arr_12_column_added, arr_12_column_added.shape)

# EXERCISE 13
#
# Create the following 4x4 array:
#
# data = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120],
#     [130, 140, 150, 160]
# ])
#
# 1. Split the array into two arrays with the same number of rows.
# 2. Print both resulting arrays.
# 3. Reverse the order of the columns in the second array.
# 4. Print the final second array.

data = np.array([
[10, 20, 30, 40],
[50, 60, 70, 80],
[90, 100, 110, 120],
[130, 140, 150, 160]])
print(data)
data_split = np.split(data, 2)
data_split_2_arr_reverse = np.flip(data_split[1], axis=1)
print(data_split_2_arr_reverse)

# EXERCISE 14
#
# Create:
#
# sales = np.array([
#     [120, 5],
#     [250, 3],
#     [180, 4],
#     [300, 2],
#     [90,  8]
# ])
#
# 1. Create a new 1D array containing:
#    [0.10, 0.15, 0.05, 0.20, 0.10]
#
# 2. Add this array to sales as a third column.
# 3. Then create a fourth column containing:
#    Quantity * (1 + Discount)
#
# 4. Add the fourth column to the array.
# 5. Print the final array and its shape.

sales = np.array([
[120, 5],
[250, 3],
[180, 4],
[300, 2],
[90,  8]])
print(sales)
arr_14 = np.array([0.10, 0.15, 0.05, 0.20, 0.10])
arr_14_column_added = np.column_stack((sales, arr_14))
print(arr_14_column_added, arr_14_column_added.shape)
arr_14_4_column = arr_14_column_added[::, 1:2:] * (1 + arr_14_column_added[::, -1::])
print(arr_14_4_column, arr_14_4_column.shape)
arr_14_4_column_added = np.column_stack((arr_14_column_added, arr_14_4_column))
print(arr_14_4_column_added, arr_14_4_column_added.shape)

# EXERCISE 15
#
# Create the following array:
#
# data = np.array([
#     [15, 25, 35],
#     [45, 55, 65],
#     [75, 85, 95]
# ])
#
# 1. Add a new row:
#    [105, 115, 125]
#
# 2. Add a new column:
#    [135, 145, 155, 165]
#
# 3. Delete the second row from the resulting array.
# 4. Reverse the order of the columns.
# 5. Print the final array and its shape.

data = np.array([
[15, 25, 35],
[45, 55, 65],
[75, 85, 95]])
print(data)
#funkcja row_stack mi nie działa
arr_15_row = np.array([105, 115, 125])
arr_15_row_2d = arr_15_row[np.newaxis, :]
print(arr_15_row_2d, arr_15_row_2d.shape)
arr_15_column = np.array([135, 145, 155, 165])
print(arr_15_column, arr_15_column.shape)
arr_15_row_added = np.concatenate((data, arr_15_row_2d), axis=0)
print(arr_15_row_added, arr_15_row_added.shape)
arr_15_row_added_column_added = np.column_stack((arr_15_row_added, arr_15_column))
print(arr_15_row_added_column_added, arr_15_row_added_column_added.shape)
arr_15_row_added_column_added_substracted = np.delete(arr_15_row_added_column_added, 1, axis=0)
print(arr_15_row_added_column_added_substracted, arr_15_row_added_column_added_substracted.shape)
arr_15_row_added_column_added_substracted_reversed = np.flip(arr_15_row_added_column_added_substracted, axis=1)
print(arr_15_row_added_column_added_substracted_reversed, arr_15_row_added_column_added_substracted_reversed.shape)