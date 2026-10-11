import numpy as np


# ============================================================
# Exercise 1
# ============================================================

values = np.array([-16, -9, -4, 0, 4, 9, 16])

# 1. Calculate the absolute value of every element.
# 2. Calculate the square root of the non-negative values.
# 3. Round the square roots to 2 decimal places.
# 4. Print the original array and all results.
# 5. The original array must remain unchanged.

print(np.abs(values))
values_sqrt = np.sqrt(values[values >= 0])
print(values_sqrt)
print(np.round(values_sqrt, 2))
print(values)

# ============================================================
# Exercise 2
# ============================================================

prices = np.array([12.456, 19.995, 25.499, 31.751, 44.999])

# 1. Round all prices to 2 decimal places.
# 2. Round all prices down to the nearest integer.
# 3. Round all prices up to the nearest integer.
# 4. Print all three results.
# 5. The original prices array must remain unchanged.

print(np.round(prices, 2))
print(np.floor(prices))
print(np.ceil(prices))
print(prices)

# ============================================================
# Exercise 3
# ============================================================

sales = np.array([
    [100, 120, 150],
    [200, 240, 300],
    [80,  100, 140]
])

growth_rates = np.array([0.10, 0.20, 0.15])

# Rows represent different products.
# Columns represent three consecutive periods.
#
# 1. Calculate the expected sales after applying the growth rate
#    to every value in each corresponding row.
# 2. Calculate the difference between the projected sales
#    and the original sales.
# 3. Round the projected sales to 2 decimal places.
# 4. Print the projected sales and the differences.
# 5. Do not modify the original sales array.

sales_growth = np.add(sales, (growth_rates * sales))
print(sales_growth)

sales_subtract = np.subtract(sales_growth, sales)
print(sales_subtract)

sales_growth_round = np.round(sales_growth, 2)
print(sales_growth_round)
print(sales)

# ============================================================
# Exercise 4
# ============================================================

values = np.array([1, 2, 5, 10, 20, 50, 100])

# 1. Calculate the natural logarithm of every value.
# 2. Calculate the base-10 logarithm of every value.
# 3. Calculate the exponential of the natural logarithm.
# 4. Round the exponential results to 5 decimal places.
# 5. Compare the original values with the reconstructed values.
# 6. Create a boolean mask identifying values where the
#    reconstructed value differs from the original by less than 0.001.
# 7. Print all results and the mask.

print(np.log(values))
print(np.log10(values))
print(np.exp(np.log(values)))
print(np.round(np.exp(np.log(values)), 5))

reconstructed = np.exp(np.log(values))
print(reconstructed)
difference = np.abs(reconstructed - values)
print(difference)

mask = difference < 0.001
print(mask)

# ============================================================
# Exercise 5
# ============================================================

temperatures = np.array([
    [-5,  2,  8, 15],
    [ 3, 10, 18, 25],
    [-2,  5, 12, 30]
])

# Rows represent three cities.
# Columns represent four consecutive days.
#
# 1. Calculate the absolute temperature for every measurement.
# 2. Create a mask identifying measurements with an absolute
#    temperature greater than 15.
# 3. Create a new array containing only those measurements.
# 4. Calculate the square of every temperature.
# 5. Calculate the square root of the squared temperatures.
# 6. Round the square-root results to 2 decimal places.
# 7. Verify that the absolute temperature and the square-root
#    results are equal.
# 8. Print the mask, selected measurements, and verification result.
# 9. Do not modify the original temperatures array.

print(np.abs(temperatures))

mask = np.abs(temperatures) > 15
print(mask)

temp_2 = temperatures[mask]
print(temp_2)

values_square = np.square(temperatures)
print(values_square)

values_sqrt = np.sqrt(values_square)
print(values_sqrt)

print(np.round(values_sqrt, 2))

difference = np.abs(np.abs(temperatures) - values_sqrt)
print(difference)

verification = np.all(difference == 0)
print(verification)

print(temperatures)

import numpy as np

# ============================================================
# Exercise 6
# ============================================================

returns = np.array([
    [-0.12,  0.05,  0.08, -0.03],
    [ 0.04, -0.02,  0.11,  0.06],
    [-0.07,  0.09, -0.04,  0.02],
    [ 0.03,  0.01, -0.09,  0.07]
])

# Rows represent four assets.
# Columns represent four consecutive periods.
#
# 1. Calculate the absolute value of every return.
# 2. Calculate the square of every return.
# 3. Calculate the square root of the squared returns.
# 4. Verify that the results from steps 1 and 3 are equal.
# 5. Calculate the mean absolute return for each asset.
# 6. Identify assets whose mean absolute return exceeds 0.06.
# 7. Print the results and the boolean mask.
# 8. Do not modify the original returns array.

returns_abs = np.abs(returns)
print(returns_abs)

returns_square = np.square(returns)
print(returns_square)

returns_square_root = np.sqrt(returns_square)
print(returns_square_root)

difference = np.abs(np.subtract(returns_abs, returns_square_root))
verification = np.all(difference == 0)
print(difference, verification)

mean_abs_asset = np.mean(returns_abs, axis=1)
print(mean_abs_asset)

mask = mean_abs_asset > 0.06
print(mask)

mean_abs_asset_filtered = mean_abs_asset[mask]
print(mean_abs_asset_filtered)

print(returns)

# ============================================================
# Exercise 7
# ============================================================

prices = np.array([
    [19.99, 24.50, 31.75, 42.99],
    [15.25, 28.80, 35.49, 49.95],
    [22.10, 26.40, 39.99, 45.50]
])

# Rows represent three products.
# Columns represent four consecutive months.
#
# 1. Increase every price by 8%.
# 2. Round the projected prices to 2 decimal places.
# 3. Calculate the absolute difference between projected
#    and original prices.
# 4. Calculate the mean projected price for each product.
# 5. Identify products whose mean projected price exceeds 30.
# 6. Select the corresponding rows from the projected array.
# 7. Print the projected prices, differences, means,
#    boolean mask, and selected rows.
# 8. Do not modify the original prices array.

prices_increased = np.add(prices, prices * 0.08)
print(prices_increased)

prices_round = np.round(prices_increased, 2)
print(prices_round)

difference = np.abs(np.subtract(prices_round, prices))
print(difference)

mean_projected_price = np.mean(prices_round, axis=1)
print(mean_projected_price)

mask = mean_projected_price > 30
print(mask)

products_filtered = prices[mask]
print(products_filtered) 
print(prices_increased[mask])
print(prices)

# ============================================================
# Exercise 8
# ============================================================

values = np.array([
    [1,  4,  9,  16],
    [2,  8,  18, 32],
    [3,  12, 27,  48]
])

# Rows represent three groups.
# Columns represent four observations per group.
#
# 1. Calculate the square root of every value.
# 2. Calculate the natural logarithm of every original value.
# 3. Calculate the exponential of the logarithm results.
# 4. Round the reconstructed values to 4 decimal places.
# 5. Calculate the absolute reconstruction error.
# 6. Create a boolean mask identifying errors below 0.001.
# 7. Calculate the maximum reconstruction error for each row.
# 8. Print the transformed arrays, mask, and row-wise errors.
# 9. Do not modify the original values array.

values_sqrt = np.sqrt(values)
print(values_sqrt)

values_ln = np.log(values)
print(values_ln)

exp = np.exp(np.log(values))
print(exp)

exp_round = np.round(exp, 4)
print(exp_round)

abs_error = np.abs(np.subtract(exp_round, values))
verification = np.all(abs_error == 0)
print(abs_error, verification)

error_mask = abs_error < 0.001
print(error_mask)

max_row_error = np.max(abs_error, axis=1)
print(max_row_error)

print(values)

# ============================================================
# Exercise 9
# ============================================================

temperatures = np.array([
    [-8,  3, 12, 19, 24],
    [ 5, -4, 16, 22, 31],
    [-2,  7, 14, 18, 27],
    [ 9, -6, 11, 25, 29]
])

# Rows represent four cities.
# Columns represent five consecutive days.
#
# 1. Calculate the absolute temperature of every measurement.
# 2. Calculate the square of every temperature.
# 3. Calculate the square root of the squared temperatures.
# 4. Round the square-root results to 2 decimal places.
# 5. Calculate the mean absolute temperature for each city.
# 6. Identify cities whose mean absolute temperature exceeds 15.
# 7. Select the corresponding rows from the absolute-temperature array.
# 8. Calculate the difference between the absolute-temperature
#    array and the square-root results.
# 9. Verify that every difference equals zero.
# 10. Print the mask, selected rows, means, and verification result.
# 11. Do not modify the original temperatures array.

abs_temp = np.abs(temperatures)
print(abs_temp)

square_temp = np.square(temperatures)
print(square_temp)

sqrt_temp = np.sqrt(square_temp)
print(sqrt_temp)

sqrt_round = np.round(sqrt_temp, 2)
print(sqrt_round)

mean_abs = np.mean(abs_temp, axis=1)
print(mean_abs)

filter_mask = mean_abs > 15
print(filter_mask)

cities = temperatures[filter_mask]
cities_abs = abs_temp[filter_mask]
print(cities)
print(cities_abs)

difference = np.subtract(abs_temp, sqrt_round)
print(difference)

verification = np.all(difference == 0)
print(verification)

print(temperatures)

# ============================================================
# Exercise 10
# ============================================================

sales = np.array([
    [120, 150, 180, 210],
    [ 90, 110, 140, 170],
    [200, 220, 250, 280],
    [ 80, 100, 130, 160],
    [160, 190, 230, 270]
])

# Rows represent five stores.
# Columns represent four consecutive months.
#
# 1. Increase every sales value by 12%.
# 2. Round the projected sales to 2 decimal places.
# 3. Calculate the absolute difference between projected
#    and original sales.
# 4. Calculate the square root of every projected sales value.
# 5. Calculate the natural logarithm of every projected sales value.
# 6. Calculate the mean projected sales for each store.
# 7. Identify stores whose mean projected sales exceed 200.
# 8. Select those stores from the projected sales array.
# 9. Calculate the maximum projected sales for each month.
# 10. Verify that the original sales array remains unchanged.
# 11. Print the projected sales, differences, transformed arrays,
#     store means, mask, selected rows, monthly maxima,
#     and verification result.

sales_increased = np.add(sales, sales * 0.12)
print(sales_increased)

increased_round = np.round(sales_increased, 2)
print(increased_round)

difference = np.abs(np.subtract(increased_round, sales))
print(difference)

sqrt = np.sqrt(increased_round)
ln = np.log(increased_round)
mean = np.mean(increased_round, axis=1)
print(sqrt)
print(ln)
print(mean)

mask = mean > 200
print(mask)

sales_filtered = sales[mask]
print(sales_filtered)

sales_projected_filtered = increased_round[mask]
print(sales_projected_filtered)

max_projected_sales = np.max(increased_round, axis=0)
print(max_projected_sales)

print(sales)