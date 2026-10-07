import numpy as np


# ============================================================
# Exercise 1
# ============================================================

data = np.arange(1, 13)

# 1. Print the original array and its shape.
# 2. Reshape the array into 3 rows and 4 columns.
# 3. Store the result in a new variable called data_reshaped.
# 4. Print data_reshaped and its shape.
# 5. Reshape data_reshaped into 2 rows and 6 columns.
# 6. Print the final array and its shape.

print(data, data.shape, data.dtype)

data_reshaped = np.reshape(data, (3, 4))
print(data_reshaped, data_reshaped.shape)

data_reshaped = np.reshape(data_reshaped, (2, 6))
print(data_reshaped, data_reshaped.shape)

# ============================================================
# Exercise 2
# ============================================================

sales = np.array([
    [120, 150, 180, 200],
    [100, 130, 160, 190],
    [ 90, 140, 170, 210]
])

# Rows represent stores.
# Columns represent months.

# 1. Print the original array and its shape.
# 2. Transpose the array.
# 3. Store the result in a variable called sales_transposed.
# 4. Print sales_transposed and its shape.
# 5. Verify that the rows of sales_transposed correspond to the
#    columns of the original sales array.

print(sales, sales.shape)

sales_transposed = sales.T
print(sales_transposed, sales_transposed.shape)

verify = np.all(sales_transposed.T == sales)
print(verify)

# ============================================================
# Exercise 3
# ============================================================

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 1. Create a flattened copy of the array using one of the
#    available flattening methods.
# 2. Store the result in a variable called matrix_flat.
# 3. Print matrix_flat and its shape.
# 4. Change the first element of matrix_flat to 999.
# 5. Print matrix_flat.
# 6. Print matrix and check whether the original matrix changed.

matrix_flat = matrix.flatten()
print(matrix_flat, matrix_flat.shape)

matrix_flat[:1] = 999
print(matrix_flat)

print(matrix)
verify = matrix[:1, :1] == matrix_flat[:1]
print(verify)
#wartość nie zmieniła się w oryginalnej tablicy

# ============================================================
# Exercise 4
# ============================================================

data = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 1. Create a flattened version of data using a different
#    flattening method than in Exercise 3.
# 2. Store the result in a variable called data_flat.
# 3. Print data_flat.
# 4. Change the first element of data_flat to 999.
# 5. Print data.
# 6. Compare the result with Exercise 3 and observe whether
#    modifying the flattened array affected the original array.

data_flat = np.ravel(data)
print(data_flat, data_flat.shape)

data_flat[:1] = 999
print(data_flat, data)

verify = data[:1, :1] == data_flat[:1]
print(verify)
#wartość zmieniła się w oryginalnej tablicy

# ============================================================
# Exercise 5
# ============================================================

q1_sales = np.array([
    [100, 120],
    [150, 180]
])

q2_sales = np.array([
    [130, 140],
    [170, 200]
])

# 1. Concatenate q1_sales and q2_sales along the first axis.
# 2. Store the result in a variable called sales_rows.
# 3. Print sales_rows and its shape.
# 4. Concatenate q1_sales and q2_sales along the second axis.
# 5. Store the result in a variable called sales_columns.
# 6. Print sales_columns and its shape.
# 7. Compare the two results and explain what changed.

sales_rows = np.concatenate((q1_sales, q2_sales), axis=0)
print(sales_rows, sales_rows.shape)

sales_columns = np.concatenate((q1_sales, q2_sales), axis=1)
print(sales_columns, sales_columns.shape)

#przy łączeniu wzdłuż axis=0 dodałem wiersze a axis=1 dodałem kolumny

# ============================================================
# Exercise 6
# ============================================================

north = np.array([120, 150, 180, 200])
south = np.array([100, 130, 160, 190])

# 1. Combine north and south into one 1D array.
# 2. Store the result in a variable called total_sales.
# 3. Create a 2D array where north and south are separate columns.
# 4. Store the result in a variable called sales_by_region.
# 5. Print both arrays and their shapes.
# 6. Compare the two results and explain how their structures differ.

total_sales = np.concatenate((north, south))
print(total_sales, total_sales.shape)

sales_by_region = np.concatenate((np.reshape(total_sales[::2], (4, 1)), 
                                 np.reshape(total_sales[1::2], (4, 1))), axis=1)
print(sales_by_region, sales_by_region.shape, total_sales, total_sales.shape)
#w total_sales mamy tablice 1d a sales_by_region 2d

north_column = np.vstack(north)
south_column = np.vstack(south)
sales_by_region = np.concatenate((north_column, south_column), axis=1)
print(sales_by_region, sales_by_region.shape, total_sales, total_sales.shape)
#tu 2 sposobem z vstack

# ============================================================
# Exercise 7
# ============================================================

sales = np.array([
    [100, 120, 140, 160, 180, 200],
    [ 90, 110, 130, 150, 170, 190],
    [ 80, 100, 120, 140, 160, 180]
])

# Columns represent six consecutive months.
# Rows represent three stores.

# 1. Split the array into three equal parts along the columns.
# 2. Store the three resulting arrays in separate variables.
# 3. Print each resulting array and its shape.
# 4. Split the original array into three parts along the rows.
# 5. Store the resulting arrays in separate variables.
# 6. Print each resulting array and its shape.
# 7. Compare splitting along rows and splitting along columns.

months_1_2, months_3_4, months_5_6 = np.split(sales, (3), axis=1)
print(months_1_2, months_1_2.shape)
print(months_3_4, months_3_4.shape)
print(months_5_6, months_5_6.shape)

shop_1, shop_2, shop_3 = np.split(sales, (3))
print(shop_1, shop_1.shape)
print(shop_2, shop_2.shape)
print(shop_3, shop_3.shape)
#spliting wzdłuż kolumn rozdziela wzdłuż kolumn a wzdłuż wierszy wzdłuż wierszy

# ============================================================
# Exercise 8
# ============================================================

prices = np.array([
    [100, 120, 140, 160],
    [110, 130, 150, 170],
    [ 90, 115, 135, 155]
])

# Columns represent four products.
# Rows represent three stores.

# 1. Remove the second column from the array.
# 2. Store the result in a variable called prices_without_second.
# 3. Print the result and its shape.
# 4. Insert a new column at index 1 containing the values
#    [125, 135, 120].
# 5. Store the result in a variable called prices_with_new.
# 6. Print the result and its shape.
# 7. Verify that the new column was inserted at index 1.

print(prices, prices.shape)

prices_without_second = np.delete(prices, [1], axis=1)
print(prices_without_second, prices_without_second.shape)

new_column = np.array([[125], [135], [120]])
print(new_column, new_column.shape)

prices_with_new = np.insert(prices_without_second, [1], new_column, axis=1)
print(prices_with_new, prices_with_new.shape)

verify = np.all(new_column == prices_with_new[:, 1:2])
print(verify)

# ============================================================
# Exercise 9
# ============================================================

data = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# 1. Flip the array along the first axis.
# 2. Store the result in a variable called flipped_rows.
# 3. Flip the original array along the second axis.
# 4. Store the result in a variable called flipped_columns.
# 5. Flip the original array along both axes.
# 6. Store the result in a variable called flipped_both.
# 7. Print all three results and their shapes.
# 8. Explain what changed in each case.

flipped_rows = np.flip(data, axis=0)
flipped_columns = np.flip(data, axis=1)
flipped_both = np.flip(data, (0, 1))
print(flipped_rows, flipped_rows.shape)
print(flipped_columns, flipped_columns.shape)
print(flipped_both, flipped_both.shape)
#najpierw odwracamy wiersza, odwracamy kolumny, odwracamy wiersze i kolumny

# ============================================================
# Exercise 10
# ============================================================

monthly_sales = np.array([100, 120, 140, 160])

# 1. Print the original array and its shape.
# 2. Add a new axis so that monthly_sales becomes a column vector.
# 3. Store the result in a variable called sales_column.
# 4. Add a new axis so that monthly_sales becomes a row vector.
# 5. Store the result in a variable called sales_row.
# 6. Print both arrays and their shapes.
# 7. Compare the shapes (4,), (4, 1) and (1, 4).
# 8. Explain why these three arrays have different dimensionality.

print(monthly_sales, monthly_sales.shape)

sales_columns = monthly_sales[:, np.newaxis]
print(sales_columns, sales_columns.shape)

sales_row = monthly_sales[np.newaxis, :]
print(sales_row, sales_row.shape)

#tablica 1d, tablica 2d kolumny i tablica 2d wiersze

# ============================================================
# Exercise 11 — Regional sales analysis
# ============================================================

north = np.array([
    [120, 150, 180, 210],
    [100, 130, 160, 190],
    [140, 170, 200, 230]
])

south = np.array([
    [110, 140, 170, 200],
    [ 90, 120, 150, 180],
    [130, 160, 190, 220]
])

# Rows represent stores.
# Columns represent four consecutive months.
#
# 1. Combine north and south into one array representing
#    all six stores.
# 2. Create a boolean mask identifying stores whose
#    total sales across all four months exceed 650.
# 3. Use the mask to create a new array containing only
#    those stores.
# 4. Calculate the total sales for each selected store.
# 5. Add a new column containing the total sales of each
#    selected store.
# 6. Reverse the order of the selected stores.
# 7. Reverse the order of the month columns.
# 8. Print the final array and its shape.
# 9. Print the mask and the store totals.
# 10. Make sure the original north and south arrays are
#     not modified.

stores_combined = np.vstack((north, south))
print(stores_combined, stores_combined.shape)

total_sales = np.sum(stores_combined, axis=1)
print(total_sales, total_sales.shape)

mask = total_sales > 650
print(mask, mask.shape)

stores_high_total = stores_combined[mask]
print(stores_high_total, stores_high_total.shape)

total_sales_high = np.sum(stores_high_total, axis=1)
print(total_sales_high, total_sales_high.shape)

stores_combined_totals = np.column_stack((stores_high_total, total_sales_high))
print(stores_combined_totals, stores_combined_totals.shape)

stores_reversed = np.flip(stores_combined_totals, axis=0)
print(stores_reversed, stores_reversed.shape)

stores_months_reversed = stores_reversed[:, [3, 2, 1, 0, -1]]
print(stores_months_reversed, stores_months_reversed.shape)

print(mask, total_sales)
print(north, south)

# ============================================================
# Exercise 12 — Product inventory cleanup
# ============================================================

inventory = np.array([
    [101, 25, 40, 120],
    [102, 10, 35,  90],
    [103, 50, 20, 150],
    [104,  8, 60,  80],
    [105, 30, 45, 110],
    [106,  5, 15,  70]
])

# Columns:
# 0 → product ID
# 1 → warehouse A stock
# 2 → warehouse B stock
# 3 → price
#
# 1. Create a mask identifying products where:
#    - warehouse A stock is below 10
#      OR
#    - warehouse B stock is below 20.
# 2. Create a new array containing those products.
# 3. For those products, increase warehouse A stock
#    by 20%.
# 4. Create another mask identifying products where
#    total stock across both warehouses is greater than 60.
# 5. Create a new array containing only those products.
# 6. Calculate total stock for every remaining product.
# 7. Add total stock as a new column.
# 8. Sort the final result by total stock in descending order.
# 9. Print the final array and its shape.
# 10. Do not modify the original inventory array.

mask_1 = ((inventory[:, 1] < 10) | (inventory[:, 2] < 20))
print(mask_1, mask_1.shape)

mask_1_inventory = inventory[mask_1]
print(mask_1_inventory, mask_1_inventory.shape, mask_1_inventory.dtype)

mask_1_inventory[:, 1] = mask_1_inventory[:, 1] + (mask_1_inventory[:, 1] * 0.2)
print(mask_1_inventory)
# tu można zmienić dtype, żeby zachować wartość po przecinku
#mask_1_inventory = inventory[mask_1].astype(float)

total_stock_a_b = np.sum((mask_1_inventory[:, 1:3]), axis=1)
print(total_stock_a_b)

mask_2 = total_stock_a_b > 60
print(mask_2)

mask_2_inventory = mask_1_inventory[mask_2]
print(mask_2_inventory)

total_stock_a_b_2 = np.sum((mask_2_inventory[:, 1:3]), axis=1)
print(total_stock_a_b_2)

mask_2_inventory_totals = np.column_stack((mask_2_inventory, total_stock_a_b_2))
print(mask_2_inventory_totals)

arg_sort = np.argsort(mask_2_inventory_totals[:, -1])[::-1]
print(arg_sort)

mask_2_inventory_totals_sorted = mask_2_inventory_totals[arg_sort]
print(mask_2_inventory_totals_sorted, mask_2_inventory_totals_sorted.shape)
print(inventory)

# ============================================================
# Exercise 13 — Monthly performance transformation
# ============================================================

performance = np.array([
    [72, 85, 91, 68, 77, 88],
    [90, 81, 75, 92, 95, 89],
    [65, 70, 78, 82, 74, 80],
    [88, 94, 91, 87, 90, 96]
])

# Rows represent four employees.
# Columns represent six months.
# 1. Create a mask identifying employees whose average
#    performance across all months is at least 85.
# 2. Create a new array containing only those employees.
# 3. Calculate the average performance for each selected
#    employee.
# 4. Add the average performance as a new column.
# 5. Reverse the order of the employees.
# 6. Reverse the order of the months in the original
#    performance data.
# 7. Create a second array containing the monthly averages
#    across all employees.
# 8. Convert the monthly averages into a column vector.
# 9. Print:
#    - the employee mask,
#    - the selected employees,
#    - the final employee array,
#    - the monthly averages,
#    - all relevant shapes.
# 10. Keep the original performance array unchanged.

mask = np.mean(performance, axis=1) >= 85
employees = performance[mask]
print(employees, employees.shape)

average = np.mean(employees, axis=1)
print(average, average.shape)

employees_average = np.column_stack((employees, average))
print(employees_average, employees_average.shape)

employees_average_reversed = np.flip(employees_average, axis=0)
print(employees_average_reversed, employees_average_reversed.shape)

performance_reversed_months = np.flip(performance, axis=1)
print(performance_reversed_months, performance_reversed_months.shape)

performance_average = np.mean(performance, axis=1)
print(performance_average, performance_average.shape)

performance_average_column = performance_average[:, np.newaxis]
print(performance_average_column, performance_average_column.shape)

# ============================================================
# Exercise 14 — 3D sales analysis
# ============================================================

sales = np.array([
    [
        [100, 120, 140],
        [110, 130, 150],
        [120, 140, 160],
        [130, 150, 170]
    ],
    [
        [ 90, 110, 130],
        [100, 120, 140],
        [110, 130, 150],
        [120, 140, 160]
    ],
    [
        [ 80, 100, 120],
        [ 90, 110, 130],
        [100, 120, 140],
        [110, 130, 150]
    ]
])

# Shape:
# (3, 4, 3)
#
# Dimensions represent:
# 0 → regions
# 1 → months
# 2 → products
#
# 1. Calculate total sales for each region.
# 2. Calculate average sales for each product across
#    all regions and months.
# 3. Identify the product with the highest average sales.
# 4. Create a mask identifying regions whose total sales
#    are above the average regional total.
# 5. Create a new array containing only those regions.
# 6. From the selected regions, keep only the last two
#    months.
# 7. Reverse the order of the products.
# 8. Transpose the resulting array so that the dimensions
#    become:
#    products × months × regions
# 9. Print:
#    - regional totals,
#    - product averages,
#    - index of the best product,
#    - region mask,
#    - final array,
#    - final shape.
# 10. Do not modify the original sales array.

total_sales_region = np.sum(sales, axis=(1, 2))
print(total_sales_region, total_sales_region.shape)

average_product_sale = np.mean(sales, axis=(0, 1))
print(average_product_sale, average_product_sale.shape)

highest_average_sale_product_arg = np.argmax(average_product_sale)
print(highest_average_sale_product_arg)
#produkt z indeksem 2 ma największa średnią wartość

average_regional_total = np.mean(total_sales_region)
print(average_regional_total)

mask = total_sales_region > average_regional_total
print(mask)

regions_total_above_average = sales[mask]
print(regions_total_above_average, regions_total_above_average.shape)

regions_last_2_months = regions_total_above_average[:, -2:, :]
print(regions_last_2_months, regions_last_2_months.shape)

regions_products_reversed = np.flip(regions_last_2_months, axis=2)
print(regions_products_reversed, regions_products_reversed.shape)

array_transpose = regions_products_reversed.transpose(2, 1, 0)
print(array_transpose, array_transpose.shape)

print(sales, sales.shape)

# ============================================================
# Exercise 15 — Full NumPy mini-project
# ============================================================

transactions = np.array([
    [101,  2,  50, 120],
    [102,  5,  80, 200],
    [103,  1,  40,  90],
    [104,  8,  60, 300],
    [105,  4, 100, 250],
    [106, 10,  30, 180],
    [107,  3,  70, 160],
    [108,  6,  90, 220]
])

# Columns:
# 0 → transaction ID
# 1 → quantity
# 2 → unit price
# 3 → revenue
#
# 1. Create a copy of the transactions array.
# 2. Create a new column containing:
#      quantity × unit price
# 3. Compare this calculated revenue with the existing
#    revenue column.
# 4. Create a boolean mask identifying transactions where
#    the calculated revenue is different from the recorded
#    revenue.
# 5. Create a new array containing only those transactions.
# 6. Correct the revenue values for those transactions.
# 7. Create a second mask identifying transactions where:
#    - quantity is at least 5
#      OR
#    - corrected revenue is above 300.
# 8. Create a new array containing those transactions.
# 9. Calculate:
#    - total revenue,
#    - average revenue,
#    - maximum revenue.
# 10. Find the transaction ID with the highest revenue.
# 11. Add a new column containing the revenue rank
#     of each selected transaction.
# 12. Reverse the order of the transactions.
# 13. Reverse the order of the columns.
# 14. Convert the final 2D array into a column vector
#     using a flattening operation and a new axis.
# 15. Print:
#    - the mismatch mask,
#    - corrected transactions,
#    - selected transactions,
#    - revenue statistics,
#    - ID of the highest-revenue transaction,
#    - final array,
#    - final shape.
# 16. The original transactions array must remain unchanged.

transactions_copy = transactions.copy()
print(transactions_copy, transactions_copy.shape)

trans_rev = np.insert(transactions_copy, 4, (transactions_copy[:, 1] * transactions_copy[:, 2]), axis=1)
print(trans_rev)

mask = ~(trans_rev[:, 3] == trans_rev[:, 4])
print(mask, mask.shape)

transactions_mask = trans_rev[mask]
print(transactions_mask, transactions_mask.shape)

trans_rev_corrected = np.delete(transactions_mask, 3, axis=1)
print(trans_rev_corrected, trans_rev_corrected.shape)

mask_2 = ((trans_rev_corrected[:, 1] >= 5) | (trans_rev_corrected[:, 3] > 300))
print(mask_2, mask_2.shape)

transactions_mask_2 = trans_rev_corrected[mask_2]
print(transactions_mask_2, transactions_mask_2.shape)

total_revenue = np.sum(transactions_mask_2[:, 3])
average_revenue = np.mean(transactions_mask_2[:, 3])
maximum_revenue = np.max(transactions_mask_2[:, 3])
print(total_revenue, average_revenue, maximum_revenue)

highest_revenue_arg = np.argmax(transactions_mask_2[:, 3])
print(highest_revenue_arg)

highest_revenue_id = transactions_mask_2[highest_revenue_arg][0]
print(highest_revenue_id)

revenue_argsort_desc = np.argsort(transactions_mask_2[:, 3])[::-1]
print(revenue_argsort_desc, revenue_argsort_desc.shape)

transactions_mask_2_rev_rank = np.column_stack((transactions_mask_2, revenue_argsort_desc))
print(transactions_mask_2_rev_rank, transactions_mask_2_rev_rank.shape)

transactions_rows_reversed = np.flip(transactions_mask_2_rev_rank, axis=0)
transactions_columns_reversed = np.flip(transactions_rows_reversed, axis=1)
print(transactions_columns_reversed, transactions_columns_reversed.shape)

transactions_flatten = transactions_columns_reversed.flatten()
print(transactions_flatten, transactions_flatten.shape)

transactions_column = transactions_flatten[:, np.newaxis]
print(transactions_column, transactions_column.shape)

print(transactions, transactions.shape)