import numpy as np

numeric_data = np.load("../datasets/online_retail_numeric.npy")

print(numeric_data.shape)
print(numeric_data[:5])

np.set_printoptions(suppress=True)

# ============================================================
# ONLINE RETAIL - NUMPY PRACTICE
# ============================================================


# EXERCISE 1
#
# Analyze the Quantity column.
#
# 1. Print the minimum and maximum quantity.
# 2. Print the mean quantity.
# 3. Count how many transactions have Quantity greater than 10.
# 4. Count how many transactions have negative Quantity.
# 5. Create a new array containing only transactions with Quantity
#    greater than 10.
# 6. Print the shape of the new array.

print('Minimum Quantitive:', np.min(numeric_data[:, 0]))
print('Maximum Quantitive:', np.max(numeric_data[:, 0]))
print('Transactions with Quantity greater than 10:', np.sum(numeric_data[:, 0] > 10))
print('Transactions with negative Quantity:', np.sum(numeric_data[:, 0] < 0))
arr_1 = numeric_data[numeric_data[:, 0] > 10]
print(arr_1[0:5, :], arr_1.shape)

# EXERCISE 2
#
# Analyze UnitPrice.
#
# 1. Print the minimum and maximum UnitPrice.
# 2. Create a new array containing transactions with UnitPrice
#    greater than 10.
# 3. Print how many transactions meet this condition.
# 4. Calculate the mean UnitPrice of these transactions.
# 5. Sort these UnitPrice values in descending order.
# 6. Print the first 10 values after sorting.

print('Minimum Unitprice:', np.min(numeric_data[:, 1]))
print('Maximum Unitprice:', np.max(numeric_data[:, 1]))
arr_2_filter = numeric_data[numeric_data[:, 1] > 10]
print(arr_2_filter.shape)
print('Transactions with Unitprice greater than 10:', np.sum(numeric_data[:, 1] > 10))
print('Transactions with Unitprice greater than 10 mean:', np.mean(arr_2_filter[:, 1]))
arr_2_filter_sort = np.sort(arr_2_filter[:, 1])
print(arr_2_filter_sort.shape)
arr_2_filter_sort_sort_desc = np.flip(arr_2_filter_sort)
print(arr_2_filter_sort_sort_desc[:10])

# EXERCISE 3
#
# Analyze Revenue.
#
# 1. Print the minimum, maximum and mean Revenue.
# 2. Create a new array containing transactions with Revenue
#    greater than 500.
# 3. Print how many transactions meet this condition.
# 4. Find the index of the transaction with the highest Revenue.
# 5. Use this index to retrieve the Quantity, UnitPrice and Revenue
#    of that transaction.
# 6. Print these three values.

print('Minimum Revenue:', np.min(numeric_data[:, 2]))
print('Maximum Revenue:', np.max(numeric_data[:, 2]))
arr_3 = numeric_data[numeric_data[:, 2] > 500]
print(arr_3[:5], arr_3.shape)
print('Transactions with Revenue greater than 500:', np.sum(numeric_data[:, 2] > 500))
highest_revenue_index = np.argmax(numeric_data[:, 2])
print('Index of the argument with the highest Revenue:', highest_revenue_index)
print('Quantity, UnitPrice and Revenue of that transaction:', numeric_data[highest_revenue_index])

# EXERCISE 4 
#
# Create a new analysis array containing:
#
# Quantity | UnitPrice | Revenue
#
# 1. Keep only transactions where Quantity is greater than 5
#    AND UnitPrice is greater than 2.
# 2. From this filtered array, calculate the mean of each column.
# 3. Print the three resulting means.
# 4. Sort the filtered array by Revenue in ascending order.
# 5. Print the last 10 rows of the sorted array.

arr_4 = numeric_data.copy()
print(arr_4[:5], arr_4.shape)
arr_4_filter = arr_4[((arr_4[:, 0] > 5) & (arr_4[:, 1] > 2))]
print(arr_4_filter[:5], arr_4_filter.shape)
print('Mean of each column:', np.mean(arr_4_filter, axis=0))
arr_4_filter_argsort = np.argsort(arr_4_filter[:, 2])
print(arr_4_filter_argsort, arr_4_filter_argsort.shape)
arr_4_final = arr_4_filter[arr_4_filter_argsort]
print(arr_4_final[-10:, ::])

# EXERCISE 5
#
# Perform a small revenue analysis. 
#
# 1. Create a copy of the full Quantity / UnitPrice / Revenue array.
# 2. For every transaction where Quantity is negative,
#    replace Quantity with 0.
# 3. Recalculate Revenue using:
#
#    Quantity * UnitPrice
#
# 4. Replace the Revenue column with the recalculated values.
# 5. Find the 10 transactions with the highest Revenue.
# 6. Print these 10 transactions.
# 7. Calculate the mean Revenue of these 10 transactions.
#
# Important:
# The operations in points 2-5 should be performed on your
# modified copy, not on the original numeric_data array.

arr_5 = numeric_data.copy()
print(arr_5, arr_5.shape)
arr_5[:, 0] = np.where(arr_5[:, 0] < 0, 0, arr_5[:, 0])
print(arr_5, arr_5.shape)
quantity = arr_5[:, 0]
unitprice = arr_5[:, 1]
arr_5[:, 2] = quantity * unitprice
print(arr_5, arr_5.shape)
arr_5_argsort = np.argsort(arr_5[:, 2])
print(arr_5_argsort, arr_5_argsort.shape)
arr_5_sort = arr_5[arr_5_argsort]
arr_5_final = arr_5_sort[-10:, :]
print('Mean Revenue of these 10 transactions:', np.mean(arr_5_final[:, 2]))


