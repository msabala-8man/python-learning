import numpy as np
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