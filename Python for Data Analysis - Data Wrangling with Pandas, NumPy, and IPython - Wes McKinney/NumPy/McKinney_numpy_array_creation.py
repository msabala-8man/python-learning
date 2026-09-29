# TOPIC:
# NumPy array creation
#
# SOURCE:
# Wes McKinney - Python for Data Analysis
#
# METHODS:
# np.array()
# np.zeros()
# np.ones()
# np.empty()
# np.full()
# np.arange()
# *_like()
# dtype


import numpy as np


# EXERCISE 1
# Create a NumPy array from the following Python list of monthly sales:
# 1250, 1480, 1320, 1710, 1590, 1840
#
# 1. Store the list in a variable called monthly_sales.
# 2. Convert it into a NumPy array called sales_array.
# 3. Print the array, its shape, its ndim, and its dtype.
# 4. Create a second array containing the same values as floating-point numbers.
# 5. Print the dtype of the second array.

monthly_sales = [1250, 1480, 1320, 1710, 1590, 1840]

sales_array = np.array(monthly_sales)
print(sales_array, sales_array.shape, sales_array.ndim, sales_array.dtype)

sales_array_float = sales_array.astype(np.float64)
print(sales_array_float, sales_array_float.dtype)

# EXERCISE 2
# Create a 4x5 NumPy array representing an empty sales forecast table.
#
# 1. The table should initially contain zeros.
# 2. Print the array and its shape.
# 3. Replace all values with the following forecast values:
#    120, 135, 150, 165, 180,
#    125, 140, 155, 170, 185,
#    130, 145, 160, 175, 190,
#    135, 150, 165, 180, 195
# 4. Print the final array.
# 5. Print its dtype.

sales = np.zeros((4, 5))
print(sales, sales.shape)

forecast = [120, 135, 150, 165, 180,
   125, 140, 155, 170, 185,
   130, 145, 160, 175, 190,
   135, 150, 165, 180, 195]

forecast_array = np.reshape(forecast, (4, 5))
print(forecast_array, forecast_array.shape)

sales[:] = forecast_array
print(sales, sales.dtype)


# EXERCISE 3
# Create an array containing transaction IDs from 1001 through 1020.
#
# 1. Create the array.
# 2. Print the first five transaction IDs.
# 3. Print the last five transaction IDs.
# 4. Print every second transaction ID starting with the first one.
# 5. Print the dtype of the array.

transactions_id = np.arange(1001, 1021)

print(transactions_id[:5])
print(transactions_id[-5:])
print(transactions_id[::2])
print(transactions_id.dtype)

# EXERCISE 4
# Create a 3x4 array representing a matrix of discount rates.
#
# 1. Fill the entire array with the value 0.10.
# 2. Create another 3x4 array containing only ones.
# 3. Create another 3x4 array containing only zeros.
# 4. Create another array with the same shape as the discount-rate array,
#    but filled with the value 0.05.
# 5. Print all four arrays.
# 6. Print the shape and dtype of the final array.

discounts = np.empty((3, 4))

rate_01 = np.full((3,4), 0.1)

discounts[:] = rate_01

rate_1 = np.ones((3, 4))

rate_0 = np.zeros((3, 4))

rate_05 = np.full_like(discounts, 0.05)

print(discounts, discounts.dtype)
print(rate_01, rate_01.dtype)
print(rate_1, rate_1.dtype)
print(rate_0, rate_0.dtype)
print(rate_05, rate_05.dtype)

# EXERCISE 5
# Create a 5x4 NumPy array representing monthly revenue data.
#
# 1. Create an array containing values from 1000 to 2900 with a step of 100.
# 2. Reshape it into 5 rows and 4 columns.
# 3. Create a new array with the same shape as the revenue array,
#    containing only ones.
# 4. Create another array with the same shape as the revenue array,
#    containing only zeros.
# 5. Create another array with the same shape as the revenue array,
#    filled with the value 500.
# 6. Print the revenue array and all three additional arrays.
# 7. Print the shape, ndim, and dtype of the revenue array.

monthly_revenue = np.arange(1000, 2901, 100)
print(monthly_revenue, monthly_revenue.shape, monthly_revenue.ndim, monthly_revenue.dtype)

monthly_revenue_reshaped = np.reshape(monthly_revenue, (5, 4))
print(monthly_revenue_reshaped, monthly_revenue_reshaped.shape, monthly_revenue_reshaped.ndim,
       monthly_revenue_reshaped.dtype)

rate_1 = np.ones_like(monthly_revenue_reshaped) 
print(rate_1, rate_1.shape, rate_1.ndim, rate_1.dtype)

rate_0 = np.zeros_like(monthly_revenue_reshaped)
print(rate_0, rate_0.shape, rate_0.ndim, rate_0.dtype)

rate_500 = np.full_like(monthly_revenue_reshaped, 500)
print(rate_500, rate_500.shape, rate_500.ndim, rate_500.dtype)

# EXERCISE 6
# Create a NumPy array representing monthly revenue for 12 months.
#
# 1. Create an array containing values from 1200 to 6700 with a step of 500.
# 2. Reshape it into 4 rows and 3 columns, where each row represents one quarter.
# 3. Print the array and its shape.
# 4. Using slicing, select the second and third quarters.
# 5. From the selected quarters, keep only the last two months of each quarter.
# 6. Print the resulting array and its shape.
# 7. Create a new array with the same shape as the selected data,
#    filled with the value 100.
# 8. Print the new array.

monthly_revenue = np.arange(1200, 6701, 500)
print(monthly_revenue, monthly_revenue.shape)

monthly_revenue_reshaped = np.reshape(monthly_revenue, (4, 3))
print(monthly_revenue_reshaped, monthly_revenue_reshaped.shape)
      
second_third_quarter = monthly_revenue_reshaped[1:3, :]
print(second_third_quarter, second_third_quarter.shape)

second_third_month = second_third_quarter[:, 1:3]
print(second_third_month, second_third_month.shape)

rate_100 = np.full_like(second_third_month, 100)
print(rate_100, rate_100.shape)

# EXERCISE 7
# Create a 4x5 NumPy array representing daily sales quantities.
#
# 1. Create the array using integer values from 10 to 29.
# 2. Reshape it into 4 rows and 5 columns.
# 3. Print the array, its shape, and its dtype.
# 4. Using slicing, select the first three rows and the last three columns.
# 5. Create another array with the same shape as the selected data,
#    containing only zeros.
# 6. Create another array with the same shape as the selected data,
#    filled with the value 5.
# 7. Print all three arrays.
# 8. Print the shape and dtype of the final array.

sales_quantities = np.arange(10, 30)
print(sales_quantities, sales_quantities.shape, sales_quantities.dtype)

sales_quantities_reshaped = np.reshape(sales_quantities, (4, 5))
print(sales_quantities_reshaped, sales_quantities_reshaped.shape, sales_quantities_reshaped.dtype)

sales_quantities_reshaped_selected = sales_quantities_reshaped[:3, -3:]
print(sales_quantities_reshaped_selected, sales_quantities_reshaped_selected.shape, sales_quantities_reshaped_selected.dtype)

rate_zeros = np.zeros_like(sales_quantities_reshaped_selected)
print(rate_zeros, rate_zeros.shape, rate_zeros.dtype)

rate_fives = np.full_like(sales_quantities_reshaped_selected, 5)
print(rate_fives, rate_fives.shape, rate_fives.dtype)


# EXERCISE 8
# Create a 5x4 NumPy array representing product prices.
#
# 1. Create an array containing the values:
#    10, 20, 30, 40,
#    50, 60, 70, 80,
#    90, 100, 110, 120,
#    130, 140, 150, 160,
#    170, 180, 190, 200
# 2. Create the array using integer dtype.
# 3. Using slicing, select rows 2 through 5 and columns 2 through 4.
# 4. Create a new array with the same shape as the selected data,
#    but using floating-point dtype and filled with 0.5.
# 5. Print the selected data and the new array.
# 6. Print the dtype of both arrays.
#
# Note:
# The new array should have the same shape as the selected data,
# but its dtype should be different.

prices = np.array([[10, 20, 30, 40],
   [50, 60, 70, 80],
   [90, 100, 110, 120],
   [130, 140, 150, 160],
   [170, 180, 190, 200]]).astype(np.int64)
print(prices, prices.shape, prices.dtype)

prices_selected = prices[1:, 1:]
print(prices_selected, prices_selected.shape, prices_selected.dtype)

rate_05 = np.full_like(prices_selected, 0.05).astype(np.float64)
print(rate_05, rate_05.shape, rate_05.dtype)

# EXERCISE 9
# Create a 6x4 NumPy array representing monthly sales for different regions.
#
# 1. Create an array containing integers from 100 to 330 with a step of 10.
# 2. Reshape it into 6 rows and 4 columns.
# 3. Using slicing, select every second row starting with the first row.
# 4. From the resulting array, select the first and third columns.
# 5. Print the resulting array and its shape.
# 6. Create another array with the same shape as the resulting array,
#    filled with the value 1.0.
# 7. Print its dtype.
# 8. Add the two arrays together and print the result.

sales_regions = np.arange(100, 331, 10)
print(sales_regions, sales_regions.shape)

sales_regions_reshaped = np.reshape(sales_regions, (6, 4))
print(sales_regions_reshaped, sales_regions_reshaped.shape)

sales_regions_reshaped_rows = sales_regions_reshaped[::2, :]
print(sales_regions_reshaped_rows, sales_regions_reshaped_rows.shape)

sales_regions_selected = sales_regions_reshaped_rows[:, [0, 2]]
print(sales_regions_selected, sales_regions_selected.shape)

rate_ones = np.ones_like(sales_regions_selected)
print(rate_ones, rate_ones.shape, rate_ones.dtype)

arrays_added = sales_regions_selected + rate_ones
print(arrays_added, arrays_added.shape, arrays_added.dtype)

# EXERCISE 10
# Create a 4x6 NumPy array representing monthly sales data.
#
# 1. Create an array containing values from 100 to 330 with a step of 10.
# 2. Reshape it into 4 rows and 6 columns.
# 3. Print the array and its shape.
# 4. Using slicing, select the last three rows.
# 5. From those rows, select every second column starting with the first column.
# 6. Create a new array with the same shape as the selected data,
#    filled with the value 10.
# 7. Add the new array to the selected data.
# 8. Print the final array, its shape, and its dtype.
# 9. Create another array with the same shape as the final array,
#    containing only ones.
# 10. Print the final array and the ones array.

monthly_sales = np.arange(100, 331, 10)
print(monthly_sales, monthly_sales.shape)

monthly_sales_reshaped = np.reshape(monthly_sales, (4, 6))
print(monthly_sales_reshaped, monthly_sales_reshaped.shape)

monthly_sales_rows = monthly_sales_reshaped[-3:, :]
print(monthly_sales_rows, monthly_sales_rows.shape)

monthly_sales_selected = monthly_sales_rows[:, ::2]
print(monthly_sales_selected, monthly_sales_selected.shape)

rate_tens = np.full_like(monthly_sales_selected, 10)
print(rate_tens, rate_tens.shape, rate_tens.dtype)

arrays_added = monthly_sales_selected + rate_tens
print(arrays_added, arrays_added.shape, arrays_added.dtype)

rate_ones = np.ones_like(arrays_added)
print(rate_ones, rate_ones.shape, rate_ones.dtype)


