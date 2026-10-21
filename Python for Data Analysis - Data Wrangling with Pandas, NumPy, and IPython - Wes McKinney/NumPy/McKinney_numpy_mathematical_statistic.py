import numpy as np

sales = np.array([
    [120, 150, 135, 170, 160],
    [90, 110, 105, 130, 125],
    [200, 180, 220, 210, 190],
    [75, 85, 80, 95, 100]
])

# Exercise 1
# Calculate the total and mean sales across the entire array.
# Find the minimum and maximum sales values.

total_sales = np.sum(sales)
print(total_sales)

mean_sales = np.mean(sales)
print(mean_sales)

max_sale = np.max(sales)
min_sale = np.min(sales)
print(max_sale, min_sale) 

# Exercise 2
# Calculate the mean sales for each row.
# Calculate the total sales for each column.

mean_sales_rows = np.mean(sales, axis=1)
total_sales_columns = np.sum(sales, axis=0)
print(mean_sales_rows)
print(total_sales_columns)

# Exercise 3
# Find the index of the maximum value in the entire array.
# Find the index of the minimum value in each row.

sales_arg_max = np.argmax(sales)
sales_arg_min = np.argmin(sales, axis=1)
print(sales_arg_max)
print(sales_arg_min)

# Exercise 4
# Calculate the standard deviation of sales for each row.
# Identify the row with the highest standard deviation.

stand_dev = np.std(sales, axis=1)
stand_dev_max_row = np.argmax(stand_dev)
print(stand_dev, stand_dev_max_row)

# Exercise 5
# Calculate the cumulative sum of the second row.
# Calculate the cumulative product of the fourth row.

cum_sum_second_row = np.cumsum(sales[1, :])
cum_prod_fourth_row = np.cumprod(sales[3, :])
print(cum_sum_second_row)
print(cum_prod_fourth_row)

sales = np.array([
    [120, 150, 135, 170, 160, 180],
    [90, 110, 105, 130, 125, 140],
    [200, 180, 220, 210, 190, 230],
    [75, 85, 80, 95, 100, 115],
    [310, 290, 330, 280, 350, 320],
    [160, 155, 170, 145, 180, 165]
])

# Exercise 6
# Find the maximum sales value in each region and the month index
# in which it occurs.
# Find the minimum sales value in each month and the region index
# in which it occurs.
# Verify that every region has at least one month with sales >= 300.

reg_max_sale = np.max(sales, axis=1)
month_max_sale_index = np.argmax(sales, axis=1)
print(reg_max_sale, month_max_sale_index, sep='\n')

month_min_sale = np.min(sales, axis=0)
reg_min_sale_index = np.argmin(sales, axis=0)
print(month_min_sale, reg_min_sale_index,  sep='\n')

verif_mask = sales >= 300
print(verif_mask)
verif_mask_row_sum = np.sum(verif_mask, axis=1)
print(verif_mask_row_sum)
verif = np.all(verif_mask_row_sum > 0)
print(verif)

# Exercise 7
# Calculate the cumulative sum of sales across months for each region.
# Identify regions whose cumulative sales in the final month
# exceed 1000.
# Return the cumulative sales values for those regions.

sales_cum_sum_reg = np.cumsum(sales, axis=1)
print(sales_cum_sum_reg)

sales_cum_sum_final_month = sales[sales_cum_sum_reg[:, -1] > 1000] 
print(sales_cum_sum_final_month)

final_month_cum_sum = np.cumsum(sales_cum_sum_final_month, axis=1)
print(final_month_cum_sum)

# Exercise 8
# Create a mask identifying sales values >= 200.
# Calculate the mean of all sales values satisfying this condition.
# Calculate the mean of all sales values below 200.
# Determine whether the mean of the values >= 200 is greater
# than twice the mean of the values below 200.

mask = sales >= 200
print(mask)

mask_mean = np.mean(sales[mask])
print(mask_mean)
else_mean = np.mean(sales[~mask])
print(else_mean)

deter = mask_mean > (2 * else_mean)
print(deter)

# Exercise 9
# Create a copy of the sales array.
# Replace values below the overall mean with the overall mean
# in the copy, leaving the original array unchanged.
# Verify that every value in the copy is >= the overall mean.
# Verify that the original array remains unchanged.

sales_original = sales.copy()

sales_copy = sales.copy()
print(sales_copy)

sales_mean = np.mean(sales)
print(sales_mean)

sales_copy_modif = np.where(sales_copy < sales_mean, sales_mean, sales_copy)
print(sales_copy_modif)

verif = np.all(sales_copy_modif >= sales_mean)
print(verif)

print(np.array_equal(sales, sales_original))

# Exercise 10
# Identify regions that satisfy both conditions:
# - Their total sales are above the overall mean of regional totals.
# - They have at least two months with sales >= 300.
# For the selected regions, calculate the cumulative product
# of their first three monthly sales values.
# Count the number of regions that satisfy both conditions.
# Verify that all selected regions have a maximum monthly sale >= 300.

region_totals = np.sum(sales, axis=1)
print(region_totals)

region_totals_mean = np.mean(region_totals)
print(region_totals_mean)

mask1 = (region_totals > region_totals_mean)
mask2 = (np.sum((sales >= 300), axis=1) >= 2)
regions_filtered = sales[(mask1 & mask2)]
print(regions_filtered)

reg_fil_cumprod_3_months = np.cumprod(regions_filtered[:, :3], axis=1)
print(reg_fil_cumprod_3_months)

print(np.sum(mask1 & mask2))

verif = np.all(np.max(regions_filtered, axis=1) >= 300)
print(verif)