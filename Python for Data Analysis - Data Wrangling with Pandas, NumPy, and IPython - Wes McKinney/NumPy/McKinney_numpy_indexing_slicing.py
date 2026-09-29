import numpy as np

# EXERCISE 1
# Create a NumPy array representing 100 observations with 5 variables.
#
# 1. Create an array containing integers from 1 to 500.
# 2. Reshape it into 100 rows and 5 columns.
# 3. Print the array and its shape.
# 4. Using slicing, select rows 21 through 80 and all columns.
# 5. From the selected rows, keep every second row.
# 6. From the resulting array, keep columns 2 through 5.
# 7. Print the final array and its shape.
# 8. Create another array with the same shape as the final array,
#    filled with the value 100.
# 9. Print the new array and its shape.

observations = np.arange(1, 501)
print(observations, observations.shape, observations.dtype)

observations_reshaped = np.reshape(observations, (100, 5))
print(observations_reshaped, observations_reshaped.shape)

observations_reshaped_rows = observations_reshaped[20:80, :]
observations_reshaped_every_second_row = observations_reshaped_rows[::2, :]
observations_reshaped_final = observations_reshaped_every_second_row[:, 1:5]
print(observations_reshaped_final, observations_reshaped_final.shape)

rate_hundred = np.full_like(observations_reshaped_final, 100)
print(rate_hundred, rate_hundred.shape)

# EXERCISE 2
# Create a NumPy array representing 20 days of sales data.
# Each row contains 6 daily measurements.
#
# 1. Create an array containing integers from 1 to 120.
# 2. Reshape it into 20 rows and 6 columns.
# 3. Print the array and its shape.
# 4. Select days 5 through 18.
# 5. From those days, keep every second day starting with the first
#    selected day.
# 6. From the resulting data, select the last four columns.
# 7. Reverse the order of the selected columns.
# 8. Print the final array and its shape.
# 9. Print the dtype of the final array.

sales = np.arange(1, 121)
print(sales, sales.shape, sales.dtype)

sales_reshaped = np.reshape(sales, (20, 6))
print(sales_reshaped, sales_reshaped.shape)

sales_reshaped_rows = sales_reshaped[4:18:, :]
sales_reshaped_every_second_row = sales_reshaped_rows[::2, :]
sales_reshaped_last_4_columns = sales_reshaped_every_second_row[:, -4::]
sales_reshaped_final = np.flip(sales_reshaped_last_4_columns, axis=1)
print(sales_reshaped_final, sales_reshaped_final.shape, sales_reshaped_final.dtype)

# EXERCISE 3
# Create a NumPy array representing 12 months of data for 8 regions.
# Each row represents a month and each column represents a region.
#
# 1. Create an array containing integers from 1 to 96.
# 2. Reshape it into 12 rows and 8 columns.
# 3. Print the array and its shape.
# 4. Select months 3 through 10.
# 5. From those months, keep every second month starting with month 3.
# 6. From the resulting data, select columns 2 through 7.
# 7. From those columns, keep every second column starting with column 2.
# 8. Reverse the order of the rows.
# 9. Print the final array and its shape.
#
# Important:
# Step 8 operates on the result of step 7.
# Do not go back to the original array.

data = np.arange(1, 97)
print(data, data.shape, data.dtype)

data_reshaped = np.reshape(data, (12, 8))
print(data_reshaped, data_reshaped.shape)

data_rows = data_reshaped[2:10, :]
data_rows_every_second_row = data_rows[::2, :]
data_rows_columns = data_rows_every_second_row[:, 1:7]
data_colums_every_second_column = data_rows_columns[:, ::2]
data_final = np.flip(data_colums_every_second_column, axis=0)
print(data_final, data_final.shape)

# EXERCISE 4
# Create a 3D NumPy array representing sales data.
# The dimensions represent:
#   - 4 regions
#   - 6 months
#   - 5 products
#
# 1. Create an array containing integers from 1 to 120.
# 2. Reshape it into a 3D array with shape (4, 6, 5).
# 3. Print the array and its shape.
# 4. Select regions 2 through 4.
# 5. From those regions, select months 2 through 5.
# 6. From those months, keep every second month.
# 7. From the products, select the last three products.
# 8. Reverse the order of the selected products.
# 9. Print the final array and its shape.
# 10. Print the dtype of the final array.

sales = np.arange(1, 121)
print(sales, sales.shape, sales.dtype)

sales_reshaped = np.reshape(sales, (4, 6, 5))
print(sales_reshaped, sales_reshaped.shape)

sales_reshaped_regions = sales_reshaped[1:, :, :]
sales_regions_months = sales_reshaped_regions[1:5, :]
sales_regions_every_second_month = sales_regions_months[::2, :]
sales_products = sales_regions_every_second_month[:, -3::]
sales_final = np.flip(sales_products, axis=1)
print(sales_final, sales_final.shape, sales_final.dtype)

# EXERCISE 5
# Create a NumPy array representing 100 observations with 10 variables.
#
# 1. Create an array containing integers from 1 to 1000.
# 2. Reshape it into 100 rows and 10 columns.
# 3. Print the array and its shape.
# 4. Select rows 15 through 90.
# 5. From those rows, keep every third row.
# 6. From the resulting data, select columns 2 through 9.
# 7. From those columns, keep every second column starting with column 2.
# 8. Reverse the order of the columns.
# 9. Reverse the order of the rows.
# 10. Print the final array and its shape.
# 11. Create another array with the same shape as the final array,
#     filled with the value 50.
# 12. Print the new array and its shape.
#
# Important:
# Each slicing step after step 4 should operate on the result
# of the previous step.

observations = np.arange(1, 1001)
print(observations, observations.shape, observations.dtype)

observations_reshaped = np.reshape(observations, (100, 10))
print(observations_reshaped, observations_reshaped.shape)

observation_rows = observations_reshaped[14:90, :]
observation_rows_every_third = observation_rows[::3, :]
observation_columns = observation_rows_every_third[:, 1:9]
observation_columns_every_second = observation_columns[:, ::2]
observation_columns_reversed = np.flip(observation_columns_every_second, axis=1)
observation_rows_reversed = np.flip(observation_columns_reversed, axis=0)
print(observation_rows_reversed, observation_rows_reversed.shape)

rate_50 = np.full_like(observation_rows_reversed, 50)
print(rate_50, rate_50.shape)

# EXERCISE 6
# Create a 3D NumPy array representing sales data.
# The dimensions represent:
#   - 5 regions
#   - 8 months
#   - 6 products
#
# 1. Create an array containing integers from 1 to 240.
# 2. Reshape it into a 3D array with shape (5, 8, 6).
# 3. Print the array and its shape.
# 4. Select regions 2 through 5.
# 5. From the selected regions, select months 3 through 8.
# 6. From the selected months, keep every second month starting with
#    the first selected month.
# 7. From the resulting data, select products 2 through 6.
# 8. Reverse the order of the products.
# 9. Reverse the order of the regions.
# 10. Print the final array and its shape.
# 11. Print the dtype of the final array.
#
# Important:
# Every step after step 4 must operate on the result of the previous step.

sales = np.arange(1, 241)
print(sales, sales.shape, sales.dtype)

sales_reshaped = np.reshape(sales, (5, 8, 6))
print(sales_reshaped, sales_reshaped.shape)

regions = sales_reshaped[1:, :, :]
print(regions, regions.shape)

months = regions[:, 2:, :]
months = months[:, ::2, :]
print(months, months.shape)

products = months[:, :, 1:]
print(products, products.shape)

products_reversed = np.flip(products, axis=2)
print(products_reversed, products_reversed.shape)

regions_reversed = np.flip(products_reversed, axis=0)
print(regions_reversed, regions_reversed.shape, regions_reversed.dtype)

# EXERCISE 7
# Create a 3D NumPy array representing customer activity.
# The dimensions represent:
#   - 6 customer groups
#   - 10 weeks
#   - 4 activity metrics
#
# 1. Create an array containing integers from 1 to 240.
# 2. Reshape it into a 3D array with shape (6, 10, 4).
# 3. Print the array and its shape.
# 4. Select customer groups 2 through 6.
# 5. From the selected groups, select weeks 2 through 9.
# 6. From the selected weeks, keep every second week.
# 7. From the resulting data, select the last three activity metrics.
# 8. Reverse the order of the weeks.
# 9. Reverse the order of the activity metrics.
# 10. Print the final array and its shape.
#
# Important:
# Steps 8 and 9 must operate on the result of step 7.
# Do not return to the original array.

activity = np.arange(1, 241)
print(activity, activity.shape, activity.dtype)

activity_reshaped = np.reshape(activity, (6, 10, 4))
print(activity_reshaped, activity_reshaped.shape)

customers = activity_reshaped[1:6, :, :]
print(customers, customers.shape)

weeks = customers[:, 1:9, :]
weeks = weeks[:, ::2, :]
print(weeks, weeks.shape)

activity_metrics = weeks[:, :, -3:]
print(activity_metrics, activity_metrics.shape)

weeks_reversed = np.flip(activity_metrics, axis=1)
print(weeks_reversed, weeks_reversed.shape)

activity_reversed = np.flip(weeks_reversed, axis=2)
print(activity_reversed, activity_reversed.shape)

# EXERCISE 8
# Create a 3D NumPy array representing monthly financial data.
# The dimensions represent:
#   - 4 departments
#   - 12 months
#   - 5 financial metrics
#
# 1. Create an array containing integers from 1 to 240.
# 2. Reshape it into a 3D array with shape (4, 12, 5).
# 3. Print the array and its shape.
# 4. Select departments 1 through 4.
# 5. From the selected departments, select months 4 through 11.
# 6. From the selected months, keep every second month starting with
#    the first selected month.
# 7. From the resulting data, select metrics 2 through 5.
# 8. Keep every second metric starting with the first selected metric.
# 9. Reverse the order of the departments.
# 10. Reverse the order of the remaining metrics.
# 11. Print the final array and its shape.
#
# Important:
# Each step must operate on the result of the previous step.

data = np.arange(1, 241)
print(data, data.shape, data.dtype)

data_reshaped = np.reshape(data, (4, 12, 5))
print(data_reshaped, data_reshaped.shape)

departments = data_reshaped[0:4, :, :]
print(departments, departments.shape)

months = departments[:, 3:11, :]
months = months[:, ::2, :]
print(months, months.shape)

metrics = months[:, :, 1:5]
metrics = metrics[:, :, ::2]
print(metrics, metrics.shape)

metrics = np.flip(metrics, axis=0)
metrics = np.flip(metrics, axis=2)
print(metrics, metrics.shape)

# EXERCISE 9
# Create a 3D NumPy array representing product performance.
# The dimensions represent:
#   - 7 product categories
#   - 9 months
#   - 8 performance indicators
#
# 1. Create an array containing integers from 1 to 504.
# 2. Reshape it into a 3D array with shape (7, 9, 8).
# 3. Print the array and its shape.
# 4. Select categories 2 through 7.
# 5. From the selected categories, select months 2 through 8.
# 6. Keep every second month starting with the first selected month.
# 7. From the resulting data, select indicators 2 through 7.
# 8. Keep every second indicator starting with the second selected indicator.
# 9. Reverse the order of the categories.
# 10. Reverse the order of the months.
# 11. Reverse the order of the indicators.
# 12. Print the final array and its shape.
#
# Important:
# Steps 9–11 must operate on the result of step 8.
# The three reversals should affect three different axes.


performance = np.arange(1, 505)
print(performance, performance.shape, performance.dtype)

performance = np.reshape(performance, (7, 9, 8))
print(performance, performance.shape)

performance = performance[1:7, :, :]
print(performance, performance.shape)

performance = performance[:, 1:8, :]
performance = performance[:, ::2, :]
print(performance, performance.shape)

performance = performance[:, :, 1:7]
performance = performance[:, :, 1::2]
print(performance, performance.shape)

performance = np.flip(performance, axis=0)
performance = np.flip(performance, axis=1)
performance = np.flip(performance, axis=2)
print(performance, performance.shape)

# EXERCISE 10
# Create a 3D NumPy array representing a portfolio dataset.
# The dimensions represent:
#   - 8 assets
#   - 15 trading periods
#   - 6 numerical variables
#
# 1. Create an array containing integers from 1 to 720.
# 2. Reshape it into a 3D array with shape (8, 15, 6).
# 3. Print the array and its shape.
# 4. Select assets 2 through 7.
# 5. From the selected assets, select trading periods 3 through 14.
# 6. Keep every second trading period starting with the first selected period.
# 7. From the resulting data, select variables 2 through 6.
# 8. Keep every second variable starting with the first selected variable.
# 9. Reverse the order of the assets.
# 10. Reverse the order of the trading periods.
# 11. Reverse the order of the remaining variables.
# 12. Print the final array and its shape.
# 13. Create another array with the same shape as the final array,
#     filled with the value 100.
# 14. Print the new array and its shape.
#
# Important:
# Each slicing step after step 4 must operate on the result
# of the previous step.
#
# Pay close attention to which axis represents:
#   - assets
#   - trading periods
#   - variables

data = np.arange(1, 721)
print(data, data.shape, data.dtype)

data = np.reshape(data, (8, 15, 6))
print(data, data.shape)

data = data[1:7, :, :]
data = data[:, 2:14, :]
data = data[:, ::2, :]
data = data[:, :, 1:6]
data = data[:, :, ::2]
print(data, data.shape)

data = np.flip(data, axis=0)
data = np.flip(data, axis=1)
data = np.flip(data, axis=2)
print(data, data.shape)

rate_100 = np.full_like(data, 100)
print(rate_100, rate_100.shape)
