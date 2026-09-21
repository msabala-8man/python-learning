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
arr_5[:, 2] = arr_5[:, 0] * arr_5[:, 1]
print(arr_5, arr_5.shape)
arr_5_argsort = np.argsort(arr_5[:, 2])
print(arr_5_argsort, arr_5_argsort.shape)
arr_5_sort = arr_5[arr_5_argsort]
arr_5_final = arr_5_sort[-10:, :]
print('Mean Revenue of these 10 transactions:', np.mean(arr_5_final[:, 2]))

# EXERCISE 6
#
# Analyze transactions with unusually high Quantity.
#
# 1. Create a new array containing only transactions where Quantity
#    is greater than 50.
# 2. Print the shape of the new array.
# 3. Calculate the mean Quantity of these transactions.
# 4. Calculate the mean Revenue of these transactions.
# 5. Find the transaction with the highest Quantity.
# 6. Print its Quantity, UnitPrice and Revenue.

arr_6 = numeric_data[numeric_data[:, 0] > 50]
print(arr_6, arr_6.shape)
print('Mean Quantity:', np.mean(arr_6[:, 0]))
print('Mean Revenue:', np.mean(arr_6[:, 2]))
highest_quantity_index = np.argmax(arr_6[:, 0])
print('Transaction with the highest Quantity:', arr_6[highest_quantity_index])

# EXERCISE 7
#
# Analyze high-value transactions.
#
# 1. Create a new array containing only transactions where Revenue
#    is greater than 1000.
# 2. Calculate the mean Quantity, UnitPrice and Revenue
#    for these transactions.
# 3. Sort the filtered transactions by Revenue in descending order.
# 4. Print the first 10 rows after sorting.
# 5. From these 10 transactions, calculate the mean Quantity.
#
# Important:
# After filtering, the operations in points 2-5 should use
# the filtered array.

arr_7 = numeric_data[numeric_data[:, 2] > 1000]
print(arr_7, arr_7.shape)
print('Mean Quantity:', np.mean(arr_7[:, 0]))
print('Mean UnitPrice:', np.mean(arr_7[:, 1]))
print('Mean Revenue:', np.mean(arr_7[:, 2]))
arr_7_revenue_argsort_desc = np.argsort(arr_7[:, 2])[::-1]
print(arr_7_revenue_argsort_desc, arr_7_revenue_argsort_desc.shape)
arr_7_revenue_desc_order = arr_7[arr_7_revenue_argsort_desc]
print(arr_7_revenue_desc_order[:10, :])
print('Mean Quantity of the top 10 highest Revenue:', np.mean(arr_7_revenue_desc_order[:, 0]))

# EXERCISE 8
#
# Create a modified copy of the dataset.
#
# 1. Create a copy of numeric_data.
# 2. Replace every negative Quantity with 0.
# 3. In the modified array, replace every Revenue value below 0
#    with 0.
# 4. Calculate the mean Revenue of the modified array.
# 5. Find the 10 transactions with the highest modified Revenue.
# 6. Print these 10 transactions.
#
# Important:
# Do not modify numeric_data itself.
# All modifications must be performed on the copy.

arr_8 = numeric_data.copy()
arr_8[:, 0] = np.where(arr_8[:, 0] < 0, 0, arr_8[:, 0])
arr_8[:, 2] = np.where(arr_8[:, 2] < 0, 0, arr_8[:, 2])
print('Mean Revenue:', np.mean(arr_8[:, 2]))
arr_8_argsort_revenue_desc = np.argsort(arr_8[:, 2])[::-1]
print(arr_8_argsort_revenue_desc, arr_8_argsort_revenue_desc.shape)
arr_8_revenue_desc_order = arr_8[arr_8_argsort_revenue_desc]
print(arr_8_revenue_desc_order, arr_8_revenue_desc_order.shape)
print('Top 10 Revenue transactions:', arr_8_revenue_desc_order[:10, :])

# EXERCISE 9
#
# Analyze transactions with both high Quantity and high Revenue.
#
# 1. Create a new array containing only transactions where Quantity
#    is greater than 20 AND Revenue is greater than 500.
# 2. Print the shape of the filtered array.
# 3. Calculate the mean of each column.
# 4. Find the transaction with the highest Revenue.
# 5. Print its Quantity, UnitPrice and Revenue.
# 6. Sort the filtered array by Revenue in ascending order.
# 7. Print the last 5 rows of the sorted array.
#
# Important:
# Points 3-7 should operate on the filtered array created in point 1.

arr_9 = numeric_data[((numeric_data[:, 0] > 20) & (numeric_data[:, 2] > 500))]
print(arr_9, arr_9.shape)
print('Mean of each column:', np.mean(arr_9, axis=0))
arr_9_highest_revenue_index = np.argmax(arr_9[:, 2])
print(arr_9_highest_revenue_index)
arr_9_highest_revenue_trans = arr_9[arr_9_highest_revenue_index]
print('Transaction with the highest Revenue:', arr_9_highest_revenue_trans)
arr_9_revenue_argsort = np.argsort(arr_9[:, 2])
arr_9_revenue_order  = arr_9[arr_9_revenue_argsort]
print(arr_9_revenue_order[-5:, :])

# EXERCISE 10
#
# Perform a final transaction ranking analysis.
#
# 1. Create a copy of numeric_data.
# 2. Replace negative Quantity values with 0.
# 3. Recalculate Revenue using the modified Quantity
#    and the original UnitPrice.
# 4. Replace the Revenue column with the recalculated values.
# 5. Keep only transactions where the modified Revenue
#    is greater than 1000.
# 6. Sort these transactions by Revenue in descending order.
# 7. Print the first 10 transactions.
# 8. Calculate the mean Quantity and mean Revenue
#    of these 10 transactions.
#
# Important:
# The filtering, sorting and calculations in points 5-8
# must use the modified data.
#
# Do not modify numeric_data itself.

arr_10 = numeric_data.copy()
arr_10[:, 0] = np.where(arr_10[:, 0] < 0, 0, arr_10[:, 0])
arr_10[:, 2] = arr_10[:, 0] * arr_10[:, 1]
arr_10_filter = arr_10[arr_10[:, 2] > 1000]
print(arr_10_filter, arr_10_filter.shape)
arr_10_filter_revenue_argsort_desc = np.argsort(arr_10_filter[:, 2])[::-1]
arr_10_filter_revenue_argsort_desc_order = arr_10_filter[arr_10_filter_revenue_argsort_desc]
arr_10_top_10_revenue = arr_10_filter_revenue_argsort_desc_order[:10, :]
print(arr_10_top_10_revenue)
print('Mean Quantity of Top 10 Revenue:', np.mean(arr_10_top_10_revenue[:, 0]))
print('Mean Revenue of Top 10 Revenue:', np.mean(arr_10_top_10_revenue[:, 2]))