import numpy as np


# EXERCISE 1:
#
# Create the following NumPy array:
# [45, 12, 78, 23, 56, 9, 34]
#
# 1. Print the original array.
# 2. Create a new array with the values sorted in ascending order.
# 3. Print the sorted array.
# 4. Print the original array again.

arr_1 = np.array([45, 12, 78, 23, 56, 9, 34])
print(arr_1)
arr_1_sort = np.sort(arr_1)
print(arr_1_sort)
print(arr_1)

# EXERCISE 2:
#
# Create the following NumPy array:
# [15, 82, 34, 67, 29, 91, 43]
#
# 1. Create a new array with the values sorted in descending order.
# 2. Print the result.
# 3. Print the maximum value of the sorted array.
# 4. Print the minimum value of the sorted array.

arr_2 = np.array([15, 82, 34, 67, 29, 91, 43])
print(arr_2)
arr_2_sort_desc = np.sort(arr_2)[::-1]
print(arr_2_sort_desc)
print(np.max(arr_2_sort_desc))
print(np.min(arr_2_sort_desc))

# EXERCISE 3:
#
# Create the following 2D array:
#
# [
#     [45, 12, 78],
#     [23, 56, 9],
#     [34, 67, 21]
# ]
#
# 1. Sort each row in ascending order.
# 2. Print the resulting array.
# 3. Sort each column in ascending order using the original array.
# 4. Print the resulting array.

arr_3 = np.array([ [45, 12, 78],
                   [23, 56, 9],    
                   [34, 67, 21]])
arr_3_sort_row = np.sort(arr_3, axis=1)
print(arr_3_sort_row)
arr_3_sort_column = np.sort(arr_3, axis=0)
print(arr_3_sort_column)

# EXERCISE 4:
#
# Create the following NumPy array:
# [80, 25, 60, 10, 95, 40, 70]
#
# 1. Find the indices that would arrange the values in ascending order.
# 2. Print those indices.
# 3. Use those indices to create a new array containing the values
#    in ascending order.
# 4. Print the new array.
# 5. Use the same indices to identify the original position
#    of the smallest value.

arr_4 = np.array([80, 25, 60, 10, 95, 40, 70])
arr_4_argsort = np.argsort(arr_4)
print(arr_4_argsort)
arr_4_arg_order = arr_4[arr_4_argsort]
print(arr_4_arg_order)
print(np.argmin(arr_4))
smallest_value = arr_4[arr_4_argsort[0]]
print(smallest_value)

# EXERCISE 5:
#
# Create the following array of sales values:
# [1200, 800, 1500, 600, 1100, 950, 1750]
#
# 1. Create a new array containing the sales values in ascending order.
# 2. Create a new array containing the sales values in descending order.
# 3. Find the indices that would arrange the original sales values
#    from smallest to largest.
# 4. Use those indices to create the sorted sales array.
# 5. Print the original sales array again to confirm that it has not changed.

sales = np.array([1200, 800, 1500, 600, 1100, 950, 1750])

sales_sort = np.sort(sales)
print(sales_sort)
sales_sort_desc = np.sort(sales)[::-1]
print(sales_sort_desc)
sales_argsort = np.argsort(sales)
print(sales_argsort)
sales_arg_order = sales[sales_argsort]
print(sales, sales_arg_order)


# EXERCISE 6:
# Create the following NumPy array:
# [72, 15, 91, 38, 64, 27, 83, 49]
#
# 1. Sort the array in ascending order.
# 2. Sort the array in descending order.
# 3. Use np.argsort() to get the indices that would sort the original array.
# 4. Using those indices, create the sorted version of the original array.
# 5. Print the original array and verify that it has not changed.

arr_6 = np.array([72, 15, 91, 38, 64, 27, 83, 49])
arr_6_sort = np.sort(arr_6)
print(arr_6_sort)
arr_6_sort_desc = np.sort(arr_6)[::-1]
print(arr_6_sort_desc)
arr_6_argsort = np.argsort(arr_6)
print(arr_6_argsort)
arr_6_argsort_order = arr_6[arr_6_argsort]
print(arr_6_argsort_order)
print(arr_6)

# EXERCISE 7:
# Create the following NumPy array:
# [450, 120, 780, 230, 910, 340, 670, 560]
#
# 1. Use np.argsort() to obtain the indices that sort the array in ascending order.
# 2. Use those indices to identify the position of the smallest value in the original array.
# 3. Use the same indices to identify the position of the largest value in the original array.
# 4. Use those positions to retrieve both values from the original array.
# 5. Print the smallest value, its original index, the largest value, and its original index.

arr_7 = np.array([450, 120, 780, 230, 910, 340, 670, 560])
arr_7_argsort = np.argsort(arr_7)
print(arr_7_argsort)
smallest_index_arr_7 = arr_7_argsort[0]
smallest_value_arr_7 = arr_7[smallest_index_arr_7]
largest_index_arr_7 = arr_7_argsort[-1]
largest_value_arr_7 = arr_7[largest_index_arr_7]
print(smallest_value_arr_7, smallest_index_arr_7)
print(largest_value_arr_7, largest_index_arr_7)

