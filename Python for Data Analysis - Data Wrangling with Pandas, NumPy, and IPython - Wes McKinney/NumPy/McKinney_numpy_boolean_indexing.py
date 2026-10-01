import numpy as np

# TOPIC:
# NumPy boolean indexing — boolean masks, logical conditions and filtering
#
# EXERCISE 1
# You are given daily sales for 10 stores.
#
# 1. Create the following NumPy array:
#    sales = [120, 85, 240, 60, 175, 310, 95, 200, 45, 150]
#
# 2. Create a boolean mask for sales greater than 150.
# 3. Print the mask.
# 4. Use the mask to extract the corresponding sales values.
# 5. Count how many stores had sales greater than 150.

sales = np.array([120, 85, 240, 60, 175, 310, 95, 200, 45, 150])
print(sales, sales.shape, sales.dtype)

mask_above_150 = sales > 150
print(mask_above_150)

sales_above_150 = sales[mask_above_150]
print(sales_above_150)
print(np.sum(mask_above_150)) 

# EXERCISE 2
# Using the same sales array:
#
# 1. Create a mask for sales between 100 and 200.
# 2. Use the mask to extract those sales values.
# 3. Calculate their mean.
# 4. Create a second mask for sales below 80 OR above 250.
# 5. Use the second mask to extract those sales values.

mask_between_100_200 = ((sales > 100) & (sales < 200))
print(mask_between_100_200)

sales_between_100_200 = sales[mask_between_100_200]
print(sales_between_100_200)
print(np.mean(sales_between_100_200))

mask_below_80_or_above_250 = ((sales < 80) | (sales > 250))
print(mask_below_80_or_above_250)

sales_below_80_or_above_250 = sales[mask_below_80_or_above_250]
print(sales_below_80_or_above_250)

# EXERCISE 3
# You are given the following customer transaction values:
#
# transactions = np.array([45, 120, 75, 310, 95, 180, 60, 420, 135, 250])
#
# 1. Create a mask for transactions greater than or equal to 100.
# 2. Create a mask for transactions below 300.
# 3. Combine the two masks to select transactions from 100 through 299.
# 4. Calculate the mean of the selected transactions.
# 5. Count how many transactions satisfy the condition.

transactions = np.array([45, 120, 75, 310, 95, 180, 60, 420, 135, 250])

mask_above_or_equal_100 = transactions >= 100
print(mask_above_or_equal_100)

mask_below_300 = transactions < 300
print(mask_below_300)

transactions_between_100_299 = transactions[mask_above_or_equal_100 & mask_below_300]
print(transactions_between_100_299)
print(np.mean(transactions_between_100_299))
print(np.sum(mask_above_or_equal_100 & mask_below_300))

# EXERCISE 4
# You are given:
#
# scores = np.array([45, 72, 88, 91, 63, 55, 97, 81, 69, 100])
#
# 1. Create a mask for scores greater than or equal to 60.
# 2. Use the mask to replace all failing scores with 60.
# 3. Create a mask for scores greater than 90.
# 4. Use the mask to increase those scores by 5.
# 5. Print the final array.

scores = np.array([45, 72, 88, 91, 63, 55, 97, 81, 69, 100])

mask_above_or_equal_60 = scores >= 60
print(mask_above_or_equal_60)

scores = np.where(mask_above_or_equal_60 == False, 60, scores)
print(scores)

mask_above_90 = scores > 90
print(mask_above_90)

scores = np.where(mask_above_90 == True, scores + 5, scores)
print(scores)
# w poleceniu nic nie ma, że wynik nie może być większy niż 100, więc zostawiam tak, jak jest

# EXERCISE 5
# You are given monthly returns:
#
# returns = np.array([
#     0.05, -0.02, 0.08, -0.10, 0.03,
#     0.12, -0.04, 0.07, -0.15, 0.02
# ])
#
# 1. Create a mask for positive returns.
# 2. Create a mask for negative returns.
# 3. Calculate the mean of the positive returns.
# 4. Calculate the mean of the negative returns.
# 5. Create a mask for returns below -0.05 OR above 0.05.
# 6. Use the mask to extract those returns.
# 7. Count how many returns satisfy this condition.

returns = np.array([
    0.05, -0.02, 0.08, -0.10, 0.03,
    0.12, -0.04, 0.07, -0.15, 0.02
])
print(returns, returns.shape)

mask_positive = returns > 0
print(mask_positive)

mask_negative = returns < 0
print(mask_negative)

print(np.mean(returns[mask_positive]))
print(np.mean(returns[mask_negative]))

mask = ((returns < -0.05) | (returns > 0.05))
print(mask)

print(returns[mask])
print(np.sum(mask))

# EXERCISE 6
# You are given monthly sales for 6 stores across 5 months.
#
# sales = np.array([
#     [120, 150, 180, 210, 190],
#     [80,  95,  110, 130, 125],
#     [250, 230, 270, 290, 310],
#     [60,  75,  90,  85,  70],
#     [175, 160, 185, 200, 220],
#     [95,  120, 140, 155, 180]
# ])
#
# 1. Create a mask for values greater than 200.
# 2. Use the mask to extract all sales values greater than 200.
# 3. Create a mask for values between 100 and 200, inclusive.
# 4. Use the mask to calculate the mean of all sales values in this range.
# 5. Create a mask for values below 80 OR above 250.
# 6. Use the mask to replace all such values with 100.
# 7. Print the final array.

sales = np.array([
    [120, 150, 180, 210, 190],
    [80,  95,  110, 130, 125],
    [250, 230, 270, 290, 310],
    [60,  75,  90,  85,  70],
    [175, 160, 185, 200, 220],
    [95,  120, 140, 155, 180]
])
print(sales, sales.shape, sales.dtype)

mask = sales > 200
print(mask)

sales_above_200 = sales[mask]
print(sales_above_200)

mask_between_100_200 = (sales >= 100) & (sales <= 200)
print(mask_between_100_200)
print(np.mean(sales[mask_between_100_200]))

mask_below_80_or_above_250 = (sales < 80) | (sales > 250)
print(mask_below_80_or_above_250)
print(sales[mask_below_80_or_above_250].shape)
sales = np.where(mask_below_80_or_above_250 == True, 100, sales)
print(sales)

# EXERCISE 7
# You are given the following employee performance data.
# Each row represents one employee and the columns represent:
# [projects_completed, average_score, overtime_hours, customer_rating]
#
# performance = np.array([
#     [12, 88, 14, 4.7],
#     [ 8, 72,  6, 4.1],
#     [15, 94, 22, 4.9],
#     [ 6, 65,  4, 3.8],
#     [11, 81, 18, 4.5],
#     [ 9, 76,  9, 4.0],
#     [14, 91, 20, 4.8],
#     [ 7, 69,  5, 3.9]
# ])
#
# 1. Create a mask for employees with an average score of at least 80.
# 2. Create a second mask for employees with a customer rating of at least 4.5.
# 3. Combine the masks to select employees who satisfy both conditions.
# 4. Extract the complete rows of those employees.
# 5. Create a mask for employees who have an average score below 75 OR more than 15 overtime hours.
# 6. Extract the complete rows satisfying this condition.
# 7. Create a mask for employees who do NOT have an average score below 75.
# 8. Use the mask to extract the complete rows.

performance = np.array([
    [12, 88, 14, 4.7],
    [ 8, 72,  6, 4.1],
    [15, 94, 22, 4.9],
    [ 6, 65,  4, 3.8],
    [11, 81, 18, 4.5],
    [ 9, 76,  9, 4.0],
    [14, 91, 20, 4.8],
    [ 7, 69,  5, 3.9]
])
print(performance, performance.shape, performance.dtype)

mask_score_80_or_above = performance[:, 1] >= 80
mask_customer_rating_4p5_or_above = performance[:, 3] >= 4.5
mask = (mask_score_80_or_above & mask_customer_rating_4p5_or_above)
print(performance[mask])

mask_score_below_75 = performance[:, 1] < 75
mask_above_15_overtime = performance[:, 2] > 15
mask = (mask_score_below_75 | mask_above_15_overtime)
print(performance[mask])

mask_score_not_below_75 = (~mask_score_below_75)
print(performance[mask_score_not_below_75])

# EXERCISE 8
# You are given daily returns for 5 assets across 8 trading days.
#
# returns = np.array([
#     [ 0.02, -0.01,  0.04, -0.03,  0.01,  0.06, -0.02,  0.03],
#     [-0.04,  0.02,  0.01,  0.05, -0.02,  0.03,  0.07, -0.01],
#     [ 0.01,  0.03, -0.05,  0.02,  0.04, -0.02,  0.01,  0.05],
#     [-0.06,  0.01,  0.02, -0.04,  0.03,  0.08, -0.01,  0.02],
#     [ 0.03, -0.02,  0.06,  0.01, -0.03,  0.04,  0.02, -0.07]
# ])
#
# 1. Create a mask for returns greater than 0.05 OR below -0.05.
# 2. Extract all returns satisfying this condition.
# 3. Replace all returns below -0.05 with -0.05.
# 4. After completing point 3, create a mask for positive returns.
# 5. Use the mask to calculate the mean of all positive returns.
# 6. Create a mask for returns between -0.02 and 0.04, inclusive.
# 7. Use the mask to calculate how many returns satisfy this condition.

returns = np.array([
    [ 0.02, -0.01,  0.04, -0.03,  0.01,  0.06, -0.02,  0.03],
    [-0.04,  0.02,  0.01,  0.05, -0.02,  0.03,  0.07, -0.01],
    [ 0.01,  0.03, -0.05,  0.02,  0.04, -0.02,  0.01,  0.05],
    [-0.06,  0.01,  0.02, -0.04,  0.03,  0.08, -0.01,  0.02],
    [ 0.03, -0.02,  0.06,  0.01, -0.03,  0.04,  0.02, -0.07]
])
print(returns, returns.shape)
mask = ((returns < -0.05) | (returns > 0.05))
print(returns[mask])

returns = np.where(returns < -0.05, -0.05, returns)
print(returns)

mask_positive = returns > 0
print(np.mean(returns[mask_positive]))

mask = ((returns >= -0.02) & (returns <= 0.04))
print(np.sum(mask)) 

# EXERCISE 9
# You are given sales data for 7 stores across 4 quarters.
#
# sales = np.array([
#     [120, 135, 150, 160],
#     [ 80,  95, 110, 105],
#     [210, 225, 240, 260],
#     [ 65,  70,  75,  80],
#     [175, 190, 205, 220],
#     [ 90, 100, 115, 130],
#     [250, 270, 290, 310]
# ])
#
# 1. Create a mask identifying stores where every quarterly sales value is at least 100.
# 2. Use the mask to extract the complete rows of those stores.
# 3. Create a second mask identifying stores where at least one quarterly sales value is above 250.
# 4. Extract the complete rows satisfying this condition.
# 5. Create a mask identifying stores that do NOT have any quarterly sales value below 80.
# 6. Use the mask to extract the complete rows.
# 7. Using the original sales array, replace all individual sales values below 100 with 100.
# 8. Print the modified array.

sales = np.array([
    [120, 135, 150, 160],
    [ 80,  95, 110, 105],
    [210, 225, 240, 260],
    [ 65,  70,  75,  80],
    [175, 190, 205, 220],
    [ 90, 100, 115, 130],
    [250, 270, 290, 310]
])
print(sales, sales.shape)

mask = np.all(sales >= 100, axis=1)
print(mask)
print(sales[mask])

mask = np.any(sales > 250, axis=1)
print(sales[mask])

mask = ~(np.any(sales < 80, axis=1))
print(sales[mask])

sales = np.where(sales < 100, 100, sales)
print(sales)

# EXERCISE 10
# You are given a simplified portfolio dataset.
# Each row represents one asset and the columns represent:
# [price, daily_return, volatility, volume]
#
# portfolio = np.array([
#     [120.0,  0.03, 0.12, 150000],
#     [ 85.0, -0.02, 0.18,  90000],
#     [210.0,  0.07, 0.25, 250000],
#     [ 60.0, -0.06, 0.30,  70000],
#     [175.0,  0.04, 0.15, 180000],
#     [ 95.0,  0.01, 0.10, 120000],
#     [250.0,  0.09, 0.28, 300000],
#     [ 70.0, -0.03, 0.22,  80000]
# ])
#
# 1. Select assets with a daily return above 0.02 AND volatility below 0.20.
# 2. Extract the complete rows of those assets.
# 3. Select assets with a daily return below 0 OR volume above 200000.
# 4. Extract the complete rows satisfying this condition.
# 5. Create a mask for assets that do NOT have volatility above 0.25.
# 6. Use the mask to extract the complete rows.
# 7. Replace all negative daily returns with 0.
# 8. After completing point 7, calculate the mean daily return of the modified portfolio.

portfolio = np.array([
    [120.0,  0.03, 0.12, 150000],
    [ 85.0, -0.02, 0.18,  90000],
    [210.0,  0.07, 0.25, 250000],
    [ 60.0, -0.06, 0.30,  70000],
    [175.0,  0.04, 0.15, 180000],
    [ 95.0,  0.01, 0.10, 120000],
    [250.0,  0.09, 0.28, 300000],
    [ 70.0, -0.03, 0.22,  80000]
])

mask = ((portfolio[:, 1] > 0.02) & (portfolio[:, 2] < 0.2))
print(portfolio[mask])

mask = ((portfolio[:, 1] < 0) | (portfolio[:, 3] > 200000))
print(portfolio[mask])

mask = ~(portfolio[:, 2] > 0.25)
print(portfolio[mask])

portfolio[:, 1] = np.where(portfolio[:, 1] < 0, 0, portfolio[:, 1])
print(portfolio)
print(np.mean(portfolio[:, 1]))

# Exercise 11 — Sales corrections
# ============================================================

sales = np.array([
    [120,  90, 150],
    [ 80, 110, 170],
    [200,  75, 130],
    [ 95, 160, 220],
    [140,  85, 105]
])

# Columns:
# 0 → January sales
# 1 → February sales
# 2 → March sales

# 1. Find all rows where February sales are below 100.
# 2. Set February sales to 100 for those rows.
# 3. Find all rows where March sales are above 200.
# 4. Set March sales to 200 for those rows.
# 5. Print the final array.

print(sales[sales[:, 1] < 100])

sales[sales[:, 1] < 100, 1] = 100
print(sales)

print(sales[sales[:, 2] > 200])

sales[sales[:, 2] > 200, 2] = 200
print(sales)

# ============================================================
# Exercise 12
# ============================================================

employees = np.array([
    [101, 72,  8, 4.2],
    [102, 91, 14, 4.8],
    [103, 65,  6, 3.9],
    [104, 83, 18, 4.5],
    [105, 77, 11, 4.1],
    [106, 94, 21, 4.9]
])

# Columns:
# 0 → employee ID
# 1 → performance score
# 2 → overtime hours
# 3 → customer rating

# 1. Find rows where performance score is below 70.
# 2. Set the performance score to 70 for those rows.
# 3. Find rows where overtime hours are above 20.
# 4. Set overtime hours to 20 for those rows.
# 5. Print the final array.

print(employees[employees[:, 1] < 70])

employees[employees[:, 1] < 70, 1] = 70
print(employees)

print(employees[employees[:, 2] > 20])

employees[employees[:, 2] > 20, 2] = 20
print(employees)

# ============================================================
# Exercise 13
# ============================================================

portfolio = np.array([
    [100,  0.03, 0.12, 150000],
    [120, -0.02, 0.18, 210000],
    [ 80,  0.01, 0.25, 180000],
    [150, -0.05, 0.15, 320000],
    [200,  0.04, 0.30, 250000],
    [ 90, -0.01, 0.10, 190000]
])

# Columns:
# 0 → price
# 1 → daily return
# 2 → volatility
# 3 → volume

# 1. Find rows where daily return is negative.
# 2. Set negative daily returns to 0.
# 3. Find rows where volatility is above 0.20.
# 4. Set volatility to 0.20 for those rows.
# 5. Print the final array.

print(portfolio[portfolio[:, 1] < 0])

portfolio[portfolio[:, 1] < 0, 1] = 0
print(portfolio)

print(portfolio[portfolio[:, 2] > 0.2])

portfolio[portfolio[:, 2] > 0.2, 2] = 0.2
print(portfolio)

# ============================================================
# Exercise 14 
# ============================================================

transactions = np.array([
    [1001, 250, 2],
    [1002,  80, 5],
    [1003, 420, 1],
    [1004, 150, 8],
    [1005, 600, 3],
    [1006,  90, 7]
])

# Columns:
# 0 → transaction ID
# 1 → transaction value
# 2 → number of items

# 1. Find rows where transaction value is below 100 OR number of items is above 6.
# 2. Set the transaction value to 100 for those rows.
# 3. Find rows where transaction value is above 500 AND number of items is below 5.
# 4. Set the number of items to 5 for those rows.
# 5. Print the final array.

print(transactions[(transactions[:, 1] < 100) | (transactions[:, 2] > 6)])

transactions[(transactions[:, 1] < 100) | (transactions[:, 2] > 6), 1] = 100
print(transactions)

print(transactions[(transactions[:, 1] > 500) & (transactions[:, 2] < 5)])

transactions[(transactions[:, 1] > 500) & (transactions[:, 2] < 5), 2] = 5
print(transactions)

# ============================================================
# Exercise 15
# ============================================================

quality = np.array([
    [1, 82,  5, 0],
    [2, 64,  8, 1],
    [3, 91,  4, 0],
    [4, 58, 12, 1],
    [5, 76,  7, 0],
    [6, 88, 15, 1]
])

# Columns:
# 0 → product ID
# 1 → quality score
# 2 → processing time
# 3 → defect flag

# 1. Find rows where quality score is below 70.
# 2. Set quality score to 70 for those rows.
# 3. Find rows where processing time is above 10 AND defect flag equals 1.
# 4. Set processing time to 10 for those rows.
# 5. Find rows where quality score is below 80 OR defect flag equals 1.
# 6. Set quality score to 80 for those rows.
# 7. Print the final array.

print(quality[quality[:, 1] < 70])

quality[quality[:, 1] < 70, 1] = 70
print(quality)

print(quality[((quality[:, 2] > 10) & (quality[:, 3] == 1))])

quality[((quality[:, 2] > 10) & (quality[:, 3] == 1)), 2] = 10
print(quality)

print(quality[(quality[:, 1] < 80) | (quality[:, 3] == 1)])

quality[(quality[:, 1] < 80) | (quality[:, 3] == 1), 1] = 80
print(quality)
