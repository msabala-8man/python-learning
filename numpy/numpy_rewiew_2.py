import numpy as np

np.set_printoptions(suppress=True)

# EXERCISE 1:
#
# Use the following dataset:
#
# Columns:
# 0 = Price
# 1 = Quantity
# 2 = Revenue
# 3 = Discount
#
# Complete the following tasks:
#
# 1. Select rows 3 through 9 and columns 1 through 3.
# 2. Calculate the mean of each selected column.
# 3. Find all transactions with Revenue greater than 800.
# 4. Print the maximum Quantity among these transactions.
# 5. Print the index of the transaction with the highest Revenue.

sales = np.array([
    [120,  5,  600, 0.05],
    [250,  3,  750, 0.10],
    [80,  10, 800, 0.15],
    [300,  2,  600, 0.05],
    [150,  7, 1050, 0.20],
    [90,   8, 720, 0.10],
    [200,  4, 800, 0.05],
    [350,  1, 350, 0.00],
    [175,  6, 1050, 0.15],
    [110,  9, 990, 0.20]
])

sales_modified = sales[2:9, 0:3]
print(sales_modified)
print(np.mean(sales_modified, axis=0))
revenue_greater_than_800 = sales[sales[:, 2] > 800]
print(revenue_greater_than_800)
print(np.max(revenue_greater_than_800[:, 1]))
print(np.argmax(sales[:, 2]))

# EXERCISE 2:
#
# Use the following array:
#
# 1. Find all unique values.
# 2. Find how many times each value occurs.
# 3. Print how many times the value 3 occurs.
# 4. Keep only values greater than 2.
# 5. Find the unique values in the filtered array.
# 6. Find how many times each of these values occurs.
#
arr = np.array([
    1, 3, 2, 1, 4, 3, 2, 5,
    1, 4, 3, 3, 5, 2, 4
])

arr_unique, arr_counts = np.unique(arr, return_counts=True)
print(arr_unique, arr_counts)
print(arr_counts[arr_unique==3][0])
arr_filtered = arr[arr > 2]
print(np.unique(arr_filtered, return_counts=True))

# EXERCISE 3:
#
# Use the following dataset:
#
# 1. Select rows 2 through 6.
# 2. Select columns 2 through 6, taking every second column.
# 3. Convert the selected values into:
#    1 if the value is >= 1
#    0 if the value is >= 0
#   -1 if the value is < 0
# 4. Print the resulting array.
# 5. Calculate the mean of each row of the resulting array.
# 6. Count how many negative values exist in the original dataset.
# 7. Calculate the total value of each row in the original dataset.
# 8. Print the index of the row with the highest total.

returns = np.array([
    [ 0.8, -0.4,  1.2,  0.3, -0.7,  1.5],
    [ 1.5,  0.2, -0.8,  0.9,  1.1, -0.3],
    [-0.3,  0.7,  1.8, -1.2,  0.4,  0.9],
    [ 2.1, -0.9,  0.5,  1.3, -0.2,  1.7],
    [-1.1,  0.6,  0.9, -0.5,  1.7,  0.2],
    [ 0.4,  1.2, -0.6,  2.0, -0.8,  1.4]
])

print(returns[1:6, :])
returns_modified = returns[:, 1:6:2]
returns_modified_where = np.where(returns_modified >= 1, 1, np.where(returns_modified < 0, -1, 0))
print(returns_modified_where)
print(np.mean(returns_modified_where, axis=1))
print(np.sum(returns < 0))
print(np.sum(returns, axis=1))
print(np.argmax(np.sum(returns, axis=1)))

# EXERCISE 4:
#
# Use the following dataset:
#
# 1. Select rows 2 through 5 and columns 1 through 5.
# 2. Calculate the mean of each row.
# 3. Calculate the mean of each column.
# 4. Calculate the range of each row.
# 5. Transpose the selected array.
# 6. Flatten the transposed array.
# 7. Split the flattened array into 2 equal parts.
# 8. Print the shapes of the original and selected arrays.

data = np.array([
    [12, 25, 38, 41, 56, 63],
    [18, 31, 27, 49, 52, 70],
    [22, 14, 35, 58, 61, 77],
    [9,  28, 44, 36, 68, 55],
    [16, 33, 29, 47, 73, 81],
    [21, 19, 42, 53, 65, 74]
])

data_modified = data[1:5:, 0:5:]
print(data_modified)
print(np.mean(data_modified, axis=1))
print(np.mean(data_modified, axis=0))
print(np.max(data_modified, axis=1) - np.min(data_modified, axis=1))
data_modified_transpose = data_modified.T
print(data_modified_transpose)
data_modified_transpose_flatten = data_modified_transpose.flatten()
print(data_modified_transpose_flatten)
data_modified_transpose_flatten_split = np.split(data_modified_transpose_flatten, 2)
print(data)
print(data_modified_transpose_flatten_split)

# EXERCISE 5:
#
# Use the sales dataset.
#
# 1. Create a copy of the dataset.
# 2. Increase Price by 10 in the copy.
# 3. Keep the original dataset unchanged.
# 4. Keep only transactions where Quantity > 5
#    and Discount >= 0.10.
# 5. Classify these transactions based on Revenue:
#    Revenue >= 1000 -> "top"
#    Revenue >= 800  -> "good"
#    otherwise       -> "normal"
# 6. Calculate the mean Revenue of these transactions.
# 7. Find the maximum Price.
# 8. Find all unique Discount values in the original dataset.
# 9. Count how many times each Discount value occurs.
# 10. Print the original Price column and the modified Price column.

# Columns:
# 0 = Price
# 1 = Quantity
# 2 = Revenue
# 3 = Discount

sales_copy = sales.copy()
sales_copy[:, 0] += 10
print(sales)
print(sales_copy)
sales_copy_filtered = sales_copy[((sales_copy[:, 1] > 5) & (sales_copy[:, 3] >= 0.10))]
sales_copy_filtered_where = np.where(sales_copy_filtered[:, 2] >= 1000, 'top', np.where(sales_copy_filtered[:, 2] < 800, 'normal', 'good'))
print(sales_copy_filtered_where)
print(np.mean(sales_copy_filtered[:, 2]))
print(np.max(sales_copy_filtered[:, 0]))
print(np.unique(sales[:, 3], return_counts=True))
print(sales[:, 0])
print(sales_copy[:, 0])