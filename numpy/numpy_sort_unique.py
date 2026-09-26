import numpy as np

np.set_printoptions(suppress=True)

# EXERCISE 1
# Create the following NumPy array:
#
# sales = [120, 80, 120, 250, 80, 300, 150, 250, 120, 400, 150, 80]
#
# 1. Print all unique values.
# 2. Print each unique value together with the number of times it appears.
# 3. Sort the unique values in ascending order.
# 4. Sort the unique values in descending order.
# 5. Find the most frequently occurring value.
# 6. Print all intermediate and final results.

sales = np.array([120, 80, 120, 250, 80, 300, 150, 250, 120, 400, 150, 80])
unique, values = np.unique(sales, return_counts=True)
print(unique, values)
sorted_unique = np.sort(unique)
print(sorted_unique)
sorted_desc_unique = np.sort(unique)[::-1]
print(sorted_desc_unique)
most_freq_index = np.argmax(values)
most_freq_value = unique[most_freq_index]
print(most_freq_value)

# EXERCISE 2
# Create the following 2D NumPy array:
#
# data = [
#     [120, 10, 500],
#     [150, 20, 700],
#     [120, 10, 500],
#     [200, 15, 900],
#     [150, 20, 700],
#     [300, 25, 1200]
# ]
#
# 1. Find all unique values in the entire array.
# 2. Find all unique rows.
# 3. Sort the unique rows according to their first column in ascending order.
# 4. From the sorted result, select the last two rows.
# 5. Print all intermediate and final results.

data = np.array([
    [120, 10, 500],
    [150, 20, 700],
    [120, 10, 500],
    [200, 15, 900],
    [150, 20, 700],
    [300, 25, 1200]
])

unique, values = np.unique(data, return_counts=True)
print(unique, values)
unique_rows = np.unique(data, axis=0)
print(unique_rows)
argsort_unique_rows = np.argsort(unique_rows[:, 0])
sorted_unique_rows = unique_rows[argsort_unique_rows]
print(sorted_unique_rows)
sorted_unique_rows_filtered = sorted_unique_rows[-2:, :]
print(sorted_unique_rows_filtered)

# EXERCISE 3
# Create the following NumPy array:
#
# transactions = [
#     [101, 500],
#     [102, 300],
#     [103, 500],
#     [104, 800],
#     [105, 300],
#     [106, 1000],
#     [107, 500],
#     [108, 800]
# ]
#
# The first column contains transaction IDs.
# The second column contains transaction Revenue.
#
# 1. Find all unique Revenue values.
# 2. Count how many times each Revenue value appears.
# 3. Sort the Revenue values from highest to lowest.
# 4. Select the three highest unique Revenue values.
# 5. Create a new array containing only transactions whose Revenue
#    belongs to those three highest unique values.
# 6. Sort these transactions by Revenue in descending order.
# 7. Print the final result.

transactions = np.array([
    [101, 500],
    [102, 300],
    [103, 500],
    [104, 800],
    [105, 300],
    [106, 1000],
    [107, 500],
    [108, 800]
])

unique_revenue, revenue_counts = np.unique(transactions[:, 1], return_counts=True)
print(unique_revenue, revenue_counts)
sorted_unique_revenue = np.sort(unique_revenue)[-1::-1]
print(sorted_unique_revenue)
top_3_revenue = sorted_unique_revenue[:3]
print(top_3_revenue, top_3_revenue.shape)
top_transactions = transactions[((transactions[:, 1] == top_3_revenue[0])
                                | (transactions[:, 1] == top_3_revenue[1])
                                | (transactions[:, 1] == top_3_revenue[2]))]
# nwm jak zrobic to inaczej, bo (8, ) a (3, )
print(top_transactions)
argsort_desc_top_transactions = np.argsort(top_transactions[:, 1])[-1::-1]
print(argsort_desc_top_transactions)
sorted_desc_top_transactions = top_transactions[argsort_desc_top_transactions]
print(sorted_desc_top_transactions)

# EXERCISE 4
# Create the following 2D NumPy array:
#
# scores = [
#     [80, 75, 90, 80],
#     [65, 80, 70, 90],
#     [90, 75, 80, 65],
#     [70, 90, 65, 80],
#     [80, 65, 90, 75]
# ]
#
# 1. Find all unique values in the array.
# 2. Count how many times each value appears.
# 3. Sort the unique values in ascending order.
# 4. Create a new array containing only values greater than 70.
# 5. Find the unique values in this filtered array.
# 6. Sort these unique values in descending order.
# 7. Print all intermediate and final results.

scores = np.array([
    [80, 75, 90, 80],
    [65, 80, 70, 90],
    [90, 75, 80, 65],
    [70, 90, 65, 80],
    [80, 65, 90, 75]
])

unique, counts = np.unique(scores, return_counts=True)
print(unique, counts)
sorted_unique = np.sort(unique)
print(sorted_unique)
scores_above_70 = scores[scores > 70]
print(scores_above_70)
unique_70, counts_70 = np.unique(scores_above_70, return_counts=True)
sorted_desc_unique_70 = np.sort(unique_70)[::-1]
print(sorted_desc_unique_70)

# EXERCISE 5
# Create the following NumPy array:
#
# sales = [
#     [100, 5, 500],
#     [200, 3, 600],
#     [100, 5, 500],
#     [150, 4, 600],
#     [300, 2, 900],
#     [200, 3, 600],
#     [400, 1, 900]
# ]
#
# 1. Find all unique rows.
# 2. Find how many times each unique row occurs.
# 3. Sort the unique rows by the Revenue column in ascending order.
# 4. From the sorted unique rows, select the rows with the two highest
#    unique Revenue values.
# 5. Create a new array containing all original rows whose Revenue
#    belongs to these two Revenue values.
# 6. Sort the final array by Revenue in descending order.
# 7. Calculate the mean Revenue of the final array.
# 8. Print all important intermediate and final results.

sales = np.array([
    [100, 5, 500],
    [200, 3, 600],
    [100, 5, 500],
    [150, 4, 600],
    [300, 2, 900],
    [200, 3, 600],
    [400, 1, 900]
])

sales_unique_rows, unique_rows_count = np.unique(
    sales,
    return_counts=True,
    axis=0
)
print(sales_unique_rows, unique_rows_count)
argsort_sales_unique_rows = np.argsort(sales_unique_rows[:, 2])
sorted_sales_unique_rows = sales_unique_rows[argsort_sales_unique_rows]
print(sorted_sales_unique_rows)
highest_revenue_sales = sorted_sales_unique_rows[-2:]
print(highest_revenue_sales, highest_revenue_sales.shape)
highest_revenue = highest_revenue_sales[:, 2]
top_2_sales = sales[
    (sales[:, 2] == highest_revenue[0]) |
    (sales[:, 2] == highest_revenue[1])
]
print(top_2_sales)
top_2_desc_argsort = np.argsort(top_2_sales[:, 2])[::-1]
sorted_top_2 = top_2_sales[top_2_desc_argsort]
print(sorted_top_2)
print(np.mean(sorted_top_2[:, 2]))