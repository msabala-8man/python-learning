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