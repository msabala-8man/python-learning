
import numpy as np


# Exercise 1

temperatures = np.array([12, 19, 25, 8, 31, 16, 22, 5, 28, 14])

# 1. Replace temperatures below 15 with 15.
# 2. Create a boolean mask for temperatures above 25.
# 3. Count temperatures above 25.
# 4. Verify all resulting values are at least 15.

temperatures_below_15 = np.where(temperatures < 15, 15, temperatures)
print(temperatures_below_15)

mask = temperatures > 25
print(mask)

print(np.sum(mask))

verify = np.all(temperatures_below_15 >= 15)
print(verify)

# Exercise 2

scores = np.array([45, 72, 88, 59, 94, 67, 38, 81, 76, 52, 99, 61])

# 1. Identify scores >= 60 and < 90.
# 2. Create a new array containing only those scores.
# 3. Identify scores below 40 or above 95.
# 4. Check whether any score is below 40 and all scores are below 100.

scores_filtered = scores[((scores >= 60) & (scores < 90))]
print(scores_filtered)

scores_filtered_2 = scores[((scores < 40) | (scores > 95))]
print(scores_filtered_2)

print(np.any(scores < 40))

print(np.all(scores < 100))

# Exercise 3

sales = np.array([
    [120, 180, 240, 90],
    [210, 160, 190, 260],
    [80, 140, 175, 220],
    [300, 280, 150, 130]
])

# 1. Replace sales values below 150 with 0.
# 2. Create a mask for values between 150 and 250, inclusive.
# 3. Count values in the original array greater than 200.
# 4. Check whether every store has a monthly sales value above 250.

sales_replaced = np.where(sales < 150, 0, sales)
print(sales_replaced)

mask = ((sales >= 150) & (sales <= 250))
print(mask)

count = np.sum(sales > 200)
print(count)

check = np.all(np.any(sales > 250, axis=1))
print(check)

# Exercise 4

measurements = np.array([
    [10.5, 12.0, -1.0],
    [8.5, 15.2, 11.1],
    [np.nan, 9.8, 14.0],
    [7.2, 18.5, 0.0]
])

# 1. Identify negative values and values equal to zero.
# 2. Identify values that are negative or equal to zero.
# 3. Check whether any value is NaN.
# 4. Replace negative values and zeros with np.nan.
#    Leave existing NaN values unchanged.

negative_mask = measurements < 0
zero_mask = measurements == 0
print(negative_mask, zero_mask)
print(measurements[negative_mask])
print(measurements[zero_mask])

mask_2 = ((measurements < 0) | (measurements == 0))
print(mask_2)
print(measurements[mask_2])

check = np.any(np.isnan(measurements))
print(check)

measurements[((measurements < 0) | (measurements == 0))] = np.nan
print(measurements)

# Exercise 5

customers = np.array([
    [25, 120, 3],
    [42, 350, 8],
    [19, 80, 1],
    [35, 220, 6],
    [51, 500, 10],
    [28, 180, 4],
    [46, 90, 2],
    [31, 400, 7]
])

# Columns: age, total_spending, purchases

# 1. Identify customers aged >= 30 with spending > 200.
# 2. Identify customers aged < 25 or with >= 8 purchases.
# 3. Create an array containing customers meeting the first condition.
# 4. Check whether any customer has spending above 450.
# 5. Check whether all customers have at least one purchase.

mask = ((customers[:, 0] >= 30) & (customers[:, 1] > 200))
print(mask)
print(customers[mask])

mask_2 = ((customers[:, 0] < 25) | (customers[:, 2] >= 8))
print(mask_2)
print(customers[mask_2])

mask_array = customers[mask]
print(mask_array)

print(np.any(customers[:, 1] > 450))

np.all(customers[:, 2] >= 1)

# Exercise 6

# Columns: employee_id, sales, customer_satisfaction, absence_days
employees = np.array([
    [101, 12500, 4.8, 2],
    [102, 8700, 3.6, 8],
    [103, 15300, 4.9, 1],
    [104, 9900, 4.2, 5],
    [105, 7200, 3.1, 12],
    [106, 14200, 4.5, 3],
    [107, 11000, 3.8, 6],
    [108, 16800, 4.7, 0],
    [109, 9500, 4.6, 4],
    [110, 13100, 3.4, 9]
], dtype=float)

np.set_printoptions(suppress=True)

# 1. Identify employees with sales >= 12000,
#    satisfaction >= 4.5, and absence_days <= 3.
# 2. Identify employees who have sales < 9000
#    or satisfaction < 3.5 or absence_days > 10.
# 3. Create a copy of the employee data and replace
#    sales below 8000 with 8000 in the copy.
# 4. Check whether every employee has sales >= 7000
#    and whether any employee has absence_days > 10.
# 5. Count employees who satisfy the first condition.
# 6. Verify that the original sales column remains unchanged.

employees_original = employees.copy()

mask_1 = ((employees[:, 1] >= 12000) & (employees[:, 2] >= 4.5) & 
(employees[:, 3] <= 3))
print(mask_1)

employees_mask_1 = employees[mask_1]
print(employees_mask_1)

mask_2 = ((employees[:, 1] < 9000) | (employees[:, 2] < 3.5)
| (employees[:, 3] > 10))
print(mask_2)

employees_mask_2 = employees[mask_2]
print(employees_mask_2)

employees_copy = employees.copy()
print(employees_copy)
employees_copy[:, 1] = np.where(employees_copy[:, 1] < 8000, 8000, employees_copy[:, 1])
print(employees_copy)

print(np.all(employees[:, 1] >= 7000))
print(np.any(employees[:, 3] > 10))

print(np.sum(employees[:, 1] >= 7000))

print(np.all(employees_original[:, 1] == employees[:, 1]))

# Exercise 7

# Columns: temperature, pressure, humidity, voltage
sensors = np.array([
    [22.5, 101.2, 45.0, 3.3],
    [35.8, 99.8, 82.0, 3.1],
    [18.2, 103.5, 38.0, 3.4],
    [np.nan, 100.4, 55.0, 3.2],
    [27.0, np.nan, 91.0, 2.8],
    [41.5, 98.9, 67.0, 3.0],
    [24.8, 101.0, np.nan, 3.3],
    [19.5, 104.2, 42.0, 2.5],
    [30.1, 100.0, 59.0, 3.5],
    [26.4, 102.1, 48.0, np.nan]
])

# 1. Identify rows containing at least one NaN.
# 2. Identify rows where all four measurements are present.
# 3. Among complete rows, identify sensors with temperature
#    > 30 and humidity > 60.
# 4. Create a copy and replace temperatures > 40 with NaN.
# 5. Check whether any complete row has voltage < 3.0.
# 6. Verify that the original sensor data has not changed.

sensors_original = sensors.copy()

nan_sensors = np.isnan(sensors)
print(nan_sensors)

nan_rows_mask = np.any(nan_sensors, axis=1)
print(nan_rows_mask, nan_rows_mask.shape)
print(sensors[nan_rows_mask])

all_present_data = sensors[~nan_rows_mask]
print(all_present_data)

mask = ((all_present_data[:, 0] > 30) & (all_present_data[:, 2] > 60))
print(all_present_data[mask])

sensors_copy = sensors.copy()
sensors_copy[:, 0] = np.where(sensors_copy[:, 0] > 40, np.nan, sensors_copy[:, 0])
print(sensors_copy)

print(np.any(all_present_data[:, 3] < 3))

# tutaj zalatwia sprawe:
# print(np.array_equal(sensors, sensors_original, equal_nan=True))
verif_mask_1 = ~np.isnan(sensors)
print(verif_mask_1)
verif_mask_2 = ~np.isnan(sensors_original)
print(verif_mask_2)
verif_1 = sensors[verif_mask_1]
verif_2 = sensors_original[verif_mask_2]
print(verif_1)
print(verif_2)
print(np.all(verif_1 == verif_2))

# Exercise 8

# Columns: age, monthly_income, campaign_clicks, purchases
customers = np.array([
    [24, 4200, 12, 3],
    [37, 7800, 5, 1],
    [19, 2500, 18, 4],
    [45, 9200, 2, 0],
    [31, 6100, 9, 2],
    [52, 11000, 7, 3],
    [27, 4800, 3, 0],
    [41, 6900, 14, 5],
    [22, 3300, 8, 1],
    [36, 8500, 16, 6],
    [29, 5400, 11, 0],
    [48, 7600, 6, 2]
])

# 1. Identify customers aged 25–40 inclusive,
#    with income >= 5000 and at least 8 clicks.
# 2. Identify customers with zero purchases and
#    either income > 7000 or at least 12 clicks.
# 3. Create a copy of the data and replace click counts
#    below 5 with 5.
# 4. Check whether all customers with at least 12 clicks
#    have made at least one purchase.
# 5. Check whether any customer aged below 25 has
#    income > 4000 and at least 3 purchases.
# 6. Count customers who satisfy either condition 1 or 2.

mask = ((customers[:, 0] >= 25) & (customers[:, 0] <= 40) & 
        (customers[:, 1] >= 5000) & (customers[:, 2] >= 8))
print(customers[mask])

mask_2 = ((customers[:, 3] == 0) & ((customers[:, 1] > 7000) | 
        (customers[:, 2] >= 12)))
print(customers[mask_2])

customers_copy = customers.copy()
print(customers_copy)

customers_copy[:, 2] = np.where(customers_copy[:, 2] < 5, 5, customers_copy[:, 2])
print(customers_copy)

mask_3 = (customers[:, 2] >= 12)
print(np.all(customers[mask_3][:, 3] >= 1))
print(np.sum(mask_3))

mask_4 = ((customers[:, 0] < 25))
print(np.any((customers[mask_4][:, 1] > 4000) & (customers[mask_4][:, 3] >= 3)))
print(np.sum(mask_4))
print(np.sum(mask_3 | mask_4))

# Exercise 9

# Rows represent regions; columns represent months.
sales = np.array([
    [120, 180, 260, 310, 290, 340],
    [90, 140, 175, 220, 240, 210],
    [300, 280, 320, 150, 130, 160],
    [200, 210, 205, 215, 220, 225],
    [80, 95, 110, 125, 140, 155],
    [400, 380, 360, 340, 320, 300]
])

# 1. Identify regions with at least 3 months of sales >= 250.
# 2. Identify regions where every month has sales >= 100.
# 3. Identify regions that have at least one month < 100
#    and at least one month > 300.
# 4. Create a copy and replace sales below 100 with NaN.
# 5. Verify that the original sales array contains no values
#    below 0 and that every region has at least one month
#    with sales > 300.
# 6. Count regions satisfying both conditions 1 and 3.

mask = sales >= 250
print(mask)
mask_2 = np.sum(mask, axis=1)
print(mask_2)
regions_condition_1 = mask_2 >= 3
print(sales[regions_condition_1])

mask_2 = sales >= 100
print(mask_2)
mask_2_2 = np.sum(mask_2, axis=1)
print(mask_2_2)
mask_2_3 = mask_2_2 == 6
print(sales[mask_2_3])

mask_3 = ((sales < 100))
print(mask_3)
mask_3_sum = np.sum(mask_3, axis=1)
print(mask_3_sum)

mask_3_2 = ((sales > 300))
print(mask_3_2)
mask_3_2_sum = np.sum(mask_3_2, axis=1)
print(mask_3_2_sum)

mask_3_3 = ((mask_3_sum > 0) & (mask_3_2_sum > 0))
print(mask_3_3)

print(sales[mask_3_3])

sales_copy = sales.copy()
print(sales_copy)

sales_copy = np.where(sales_copy < 100, np.nan, sales_copy)
print(sales_copy)

mask_4 = sales > 300
print(mask_4)
mask_4_2 = np.any(mask_4, axis=1)
print(mask_4_2)

print(np.all(sales >= 0))
print(np.all(mask_4_2 > 0))

print(np.sum((regions_condition_1) & (mask_3_3)))

# Exercise 10

# Columns: transaction_id, amount, account_age_days,
#          failed_logins, international_transaction
# The last column is binary: 0 = no, 1 = yes.
transactions = np.array([
    [1001, 120, 400, 0, 0],
    [1002, 2400, 15, 3, 1],
    [1003, 850, 120, 1, 0],
    [1004, 5200, 8, 4, 1],
    [1005, 75, 900, 0, 0],
    [1006, 1800, 35, 2, 1],
    [1007, 3100, 500, 0, 1],
    [1008, 450, 20, 5, 0],
    [1009, 2700, 12, 1, 1],
    [1010, 950, 250, 3, 0],
    [1011, 6100, 5, 0, 1],
    [1012, 1300, 60, 4, 1]
], dtype=float)

# 1. Flag transactions with amount > 2000,
#    account_age_days < 30, and international_transaction == 1.
# 2. Flag transactions with failed_logins >= 3
#    and either amount > 1000 or account_age_days < 20.
# 3. Create a risk mask identifying transactions that satisfy
#    either condition 1 or condition 2.
# 4. Create a copy of the transaction data and replace amounts
#    > 5000 with 5000 in the copy.
# 5. Check whether any flagged transaction has amount > 3000.
# 6. Check whether all transactions with amount > 4000
#    are international.
# 7. Count flagged transactions and verify that the original
#    transaction amounts remain unchanged.

transactions_original = transactions.copy()

mask = ((transactions[:, 1] > 2000) & (transactions[:, 2] < 30) 
& (transactions[:, 4] == 1))
transactions_mask = transactions[mask]
print(transactions_mask)

mask2 = ((transactions[:, 3] >= 3) & ((transactions[:, 1] > 1000) 
| (transactions[:, 2] < 20)))
transactions_mask2 = transactions[mask2]
print(transactions_mask2)

risk_mask = (mask | mask2)
print(risk_mask)
transactions_risk_mask = transactions[risk_mask]
print(transactions_risk_mask)

transactions_copy = transactions.copy()
print(transactions_copy)
transactions_copy[:, 1] = np.where(transactions_copy[:, 1] > 5000, 5000, transactions_copy[:, 1])
print(transactions_copy)

check_risk_mask = np.any(transactions_risk_mask[:, 1] > 3000)
print(check_risk_mask)

check_trans = np.all(transactions[transactions[:, 1] > 4000][:, 4] == 1)
print(check_trans)

count = np.sum(risk_mask)
print(count)
print((np.all(transactions[:, 1] == transactions_original[:, 1])))