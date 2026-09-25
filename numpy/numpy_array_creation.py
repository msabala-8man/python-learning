import numpy as np


# EXERCISE 1
# Create a Python list containing the values:
# 10, 20, 30, 40, 50
# 1. Store the list in a variable called data.
# 2. Convert data into a NumPy array called arr.
# 3. Print arr.
# 4. Print the type of arr.
# 5. Print the dtype of arr.

data = [10, 20, 30, 40, 50]
arr = np.array(data)
print(arr, type(arr), arr.dtype)

# EXERCISE 2
# Create a NumPy array containing five zeros.
# 1. Print the array.
# 2. Print its shape.
# 3. Print its dtype.
# 4. Replace all elements with:
#    5, 10, 15, 20, 25
# 5. Print the modified array.

data_2 = np.zeros(5)
print(data_2, data_2.shape, data_2.dtype)
rep_data_2 = [5, 10, 15, 20, 25]
data_2[:] = rep_data_2
print(data_2)


# EXERCISE 3
# Create a NumPy array with five allocated elements.
# 1. Create the array without explicitly assigning initial values.
# 2. Replace all elements with:
#    100, 200, 300, 400, 500
# 3. Print the final array.
# 4. Print its type and dtype.

arr_3 = np.empty(5)
rep_data_3 = [100, 200, 300, 400, 500]
arr_3[:] = rep_data_3
print(arr_3, type(arr_3), arr_3.dtype)
#mimo, że dane są nadpisane dalej ich dtype to float

# EXERCISE 4
# Create an array containing the integers from 1 to 20.
# 1. Print the array.
# 2. Print every second element, starting with the first element.
# 3. Print the last five elements.
# 4. Print the elements from index 5 through index 14.

arr_4 = np.arange(1, 21)
print(arr_4)
print(arr_4[0::2])
print(arr_4[-5::])
print(arr_4[5:15])

# EXERCISE 5
# Create an array containing the even numbers from 2 to 20.
# 1. Print the array.
# 2. Reshape it into a 2D array with 2 rows and 5 columns.
# 3. Print the new array.
# 4. Print its shape and ndim.
# 5. Print the dtype.

arr_5 = np.arange(2, 21, 2)
print(arr_5)
arr_5_reshape = np.reshape(arr_5, (2, 5))
print(arr_5_reshape, arr_5_reshape.shape, arr_5_reshape.ndim, arr_5_reshape.dtype)

# EXERCISE 6
# Create a 3x4 NumPy array using a single value of your choice.
# 1. Print the array.
# 2. Create another 3x4 array containing only ones.
# 3. Create another 3x4 array containing only zeros.
# 4. Create another 3x4 array with the same shape as the first array,
#    but filled with the value 5.
# 5. Print all four arrays.

arr_6_full = np.full((3, 4), 69)
arr_6_ones = np.ones((3, 4))
arr_6_zeros = np.zeros((3, 4))
arr_6_fives = np.full(arr_6_full.shape, 5)
print(arr_6_full)
print(arr_6_ones)
print(arr_6_zeros)
print(arr_6_fives)

# EXERCISE 7
# Create a NumPy array containing the integers from 1 to 12.
#
# 1. Reshape it into a 3x4 array.
# 2. Create a 3x4 array containing only zeros.
# 3. Add the two arrays element by element.
# 4. Print the final array.
# 5. Print its shape and dtype.

arr_7 = np.arange(1,13)
print(arr_7)
arr_7_reshape = np.reshape(arr_7, (3, 4))
print(arr_7_reshape, arr_7_reshape.shape)
arr_7_zeros = np.zeros((3, 4))
print(arr_7_zeros)
arr_7_add = np.add(arr_7_reshape, arr_7_zeros)
print(arr_7_add, arr_7_add.shape, arr_7_add.dtype)


# EXERCISE 8
# Create two 2D NumPy arrays with shape 2x3:
#
# prices = [
#     [100, 200, 150],
#     [300, 250, 400]
# ]
#
# discounts = [
#     [10, 20, 15],
#     [30, 25, 40]
# ]
#
# 1. Subtract discounts from prices element by element.
# 2. Find the larger value at each position between prices and discounts.
# 3. Find the smaller value at each position between prices and discounts.
# 4. Print all three results.

arr_8_prices = np.array([
    [100, 200, 150],
    [300, 250, 400]])

arr_8_discounts = np.array([
    [10, 20, 15],
    [30, 25, 40]])

arr_8_subtract = np.subtract(arr_8_prices, arr_8_discounts)
arr_8_maximum = np.maximum(arr_8_prices, arr_8_discounts)
arr_8_minimum = np.minimum(arr_8_prices, arr_8_discounts)
print(arr_8_subtract)
print(arr_8_maximum)
print(arr_8_minimum)

# EXERCISE 9
# Create a NumPy array with five allocated elements without
# explicitly assigning initial values.
#
# 1. Print its dtype.
# 2. Replace all elements with:
#    10, 20, 30, 40, 50
# 3. Calculate the square root of every element.
# 4. Calculate the absolute value of the difference between
#    the original values and 35.
# 5. Print the final results.

arr_9 = np.empty(5)
print(arr_9.dtype)
arr_9_replace = [10, 20, 30, 40, 50]
arr_9[:] = np.array(arr_9_replace)
arr_9_sqrt = np.sqrt(arr_9)
arr_9_abs = np.abs(arr_9 - 35)
print(arr_9)
print(arr_9_sqrt)
print(arr_9_abs)

# EXERCISE 10
# Create a NumPy array containing the even numbers from 2 to 20.
#
# 1. Reshape it into a 2x5 array.
# 2. Create a 2x5 array filled with the value 5.
# 3. Multiply the two arrays element by element.
# 4. Create a new 2x5 array containing only ones.
# 5. Add the array of ones to the multiplication result.
# 6. Print the final array.

arr_10 = np.arange(2, 21, 2)
print(arr_10)
arr_10_reshape = np.reshape(arr_10, (2, 5))
print(arr_10_reshape)
arr_10_fives = np.full((2, 5), 5)
print(arr_10_fives)
arr_10_multi = np.multiply(arr_10_reshape, arr_10_fives)
print(arr_10_multi)
arr_10_ones = np.ones((2, 5))
print(arr_10_ones)
arr_10_add = np.add(arr_10_multi, arr_10_ones)
print(arr_10_add)


# EXERCISE 11
# Create a NumPy array containing:
# -10, -5, 0, 5, 10
#
# 1. Calculate the absolute value of every element.
# 2. Calculate the square of every element.
# 3. Create a new array containing the larger value at each position
#    between the absolute values and the squared values.
# 4. Create a new array containing the smaller value at each position
#    between the absolute values and the squared values.
# 5. Print both final arrays.
# 6. Print their shape and dtype.

arr_11 = np.array([-10, -5, 0, 5, 10])
arr_11_abs = np.abs(arr_11)
print(arr_11_abs)
arr_11_square = np.square(arr_11)
print(arr_11_square)
arr_11_maximum = np.maximum(arr_11_abs, arr_11_square)
arr_11_minimum = np.minimum(arr_11_abs, arr_11_square)
print(arr_11_maximum, arr_11_maximum.shape, arr_11_maximum.dtype)
print(arr_11_minimum, arr_11_minimum.shape, arr_11_minimum.dtype)
