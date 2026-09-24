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