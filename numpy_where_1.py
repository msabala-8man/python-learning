import numpy as np

np.set_printoptions(suppress=True)

# TOPIC:
# NumPy: np.where()
#
# - conditional values
# - boolean conditions
# - masks
# - replacing values
# - multiple conditions


# EXERCISE 1:
#
# Create the following NumPy array:
#
# [45, 72, 88, 53, 91, 64, 39]
#
# Create a new array where:
# - scores greater than or equal to 60 → "pass"
# - scores below 60 → "fail"
#
# Print the result.

arr1 = np.array([45, 72, 88, 53, 91, 64, 39])

arr1_where = np.where(arr1 >= 60, 'pass', 'fail')
print(arr1_where)

# EXERCISE 2:
#
# Create the following NumPy array:
#
# [80, 120, 250, 60, 300, 150]
#
# Create a new array where:
# - prices greater than 150 → "expensive"
# - prices less than or equal to 150 → "normal"
#
# Print the result.

arr2 = np.array([80, 120, 250, 60, 300, 150])
arr2_where = np.where(arr2 > 150, "expensive", "normal")
print(arr2_where)

# EXERCISE 3:
#
# Create the following NumPy array:
#
# [0.8, -0.4, 1.2, -1.1, 0.3, 1.8, -0.7, 0.5]
#
# Create a new array where:
# - positive returns → "profit"
# - negative returns → "loss"
#
# Print the result.

arr3 = np.array([0.8, -0.4, 1.2, -1.1, 0.3, 1.8, -0.7, 0.5])
arr3_where = np.where(arr3 > 0, "profit", "loss")
print(arr3_where)

# EXERCISE 4:
#
# Create the following NumPy array:
#
# [45, 72, 58, 91, 63, 39, 84]
#
# Create a new array where every score below 60
# is replaced with 60.
#
# All other scores should remain unchanged.
#
# Print the result.

arr4 = np.array([45, 72, 58, 91, 63, 39, 84])
arr4_where = np.where(arr4 < 60, 60, arr4)
print(arr4_where)

# EXERCISE 5:
#
# Create the following NumPy array:
#
# [-1.2, 0.4, 1.8, -0.6, 2.1, 0.2, -1.5, 1.1]
#
# Create a new array according to these rules:
#
# - returns greater than 1.0 → 1
# - returns between 0 and 1.0 → 0
# - returns below 0 → -1
#
# Print the result.

arr5 = np.array([-1.2, 0.4, 1.8, -0.6, 2.1, 0.2, -1.5, 1.1])
arr5_where = np.where(arr5 > 1, 1, (np.where(arr5 < 0, -1, 0)))
print(arr5_where)

# TOPIC:
# NumPy: np.where() - Advanced Practice
#
# - np.where()
# - boolean masks
# - multiple conditions
# - slicing
# - 2D arrays
# - conditional transformations


# DATASET 1:
#
# Each row represents one trade:
#
# column 0 → Entry Price
# column 1 → Exit Price
# column 2 → Quantity
# column 3 → Return
#
# Calculate Return:
# (Exit Price - Entry Price) / Entry Price * 100

trades = np.array([
    [100, 108, 50,  8.0],
    [250, 240, 20, -4.0],
    [80,   92, 100, 15.0],
    [500, 525, 10,  5.0],
    [150, 135, 40, -10.0],
    [300, 330, 15, 10.0],
    [90,   87, 80, -3.33],
    [400, 460, 12, 15.0]
])

print((trades[:, 1] - trades[:, 0])/trades[:, 0] * 100)


# EXERCISE 6:
#
# Select only the last 5 trades.
#
# Create a new array using np.where() where:
# - Return greater than 5% → "strong"
# - Return between 0% and 5% → "positive"
# - Return below 0% → "negative"
#
# Print the result.
#
# Hint:
# You will need nested np.where().

arr6 = trades[-5::, ::]
arr6_where = np.where(
    arr6[:, 3] > 5,
    "strong",
    np.where(arr6[:, 3] < 0, "negative", "positive")
)

# EXERCISE 7:
#
# From the last 5 trades, create a new array
# containing only:
# - Entry Price
# - Exit Price
# - Return
#
# Then use np.where() to classify each trade:
#
# - Return greater than or equal to 10% → 1
# - Return between 0% and 10% → 0
# - Return below 0% → -1
#
# Print the result.

arr7 = trades[-5::, [0, 1, 3]]
arr7_where = np.where(
    arr7[:, 2] >= 10,
    1,
    np.where(arr7[:, 2] >= 0, 0, -1)
)

# EXERCISE 8:
#
# Create a copy of the full "trades" array.
#
# Using np.where(), create a new Price column:
#
# - If Return is negative → decrease Exit Price by 5
# - Otherwise → keep Exit Price unchanged
#
# Add this new column back into the copied dataset
# by replacing the original Exit Price column.
#
# Print the modified dataset.
#
# The original "trades" array must remain unchanged.

arr8_trades_copy = trades.copy()
arr8 = np.where(arr8_trades_copy[:, 3] < 0, arr8_trades_copy[:, 1] - 5, arr8_trades_copy[:, 1])
arr8_trades_copy[:, 1] = arr8
print(arr8_trades_copy)

# DATASET 2:
#
# Each row represents one instrument.
# Each column represents one period.
#
# Values are percentage returns.

returns = np.array([
    [ 0.8, -0.4,  1.2,  0.3, -0.7,  1.5],
    [ 1.5,  0.2, -0.8,  0.9,  1.1, -0.3],
    [-0.3,  0.7,  1.8, -1.2,  0.4,  0.9],
    [ 2.1, -0.9,  0.5,  1.3, -0.2,  1.7],
    [-1.1,  0.6,  0.9, -0.5,  1.7,  0.2]
])


# EXERCISE 9:
#
# Select:
# - every second row, starting from the last row
# - columns from the second column to the last column,
#   taking every second column
#
# On this sliced array, use np.where() to create
# a new array where:
#
# - returns greater than 1.0 → 1
# - returns between 0 and 1.0 → 0
# - returns below 0 → -1
#
# Print the result.

arr9 = returns[-1::-2, 1::2]
arr9_where = np.where(arr9 > 1, 1, np.where(arr9<0, -1, 0))
print(arr9_where)

# EXERCISE 10:
#
# Work with the original "returns" array.
#
# Create a copy of the array.
#
# Using np.where(), replace every negative return
# with 0.
#
# Keep all positive returns unchanged.
#
# Then:
# 1. Print the modified array.
# 2. Calculate the average return of each instrument.
# 3. Calculate the average return of each period.
#
# Do not modify the original "returns" array.

returns_copy = returns.copy()
returns_copy_where = np.where(returns_copy < 0, 0, returns_copy)

print(returns_copy_where)
print(np.mean(returns_copy_where, axis=1))
print(np.mean(returns_copy_where, axis=0))

# TOPIC:
# NumPy: np.where() - Review Practice
#
# - np.where()
# - boolean masks
# - slicing
# - 2D arrays
# - axis
# - copy()
# - conditional transformations


# DATASET 1:
#
# Each row represents one transaction:
#
# column 0 → Price
# column 1 → Quantity
# column 2 → Revenue
# column 3 → Discount

sales = np.array([
    [120,  5,  600, 0.05],
    [250,  3,  750, 0.10],
    [80,  10, 800, 0.15],
    [300,  2,  600, 0.05],
    [150,  7, 1050, 0.20],
    [90,   8, 720, 0.10],
    [200,  4, 800, 0.05],
    [350,  1, 350, 0.00],
    [175,  6, 1050, 0.15],
    [110,  9, 990, 0.20]
])


# EXERCISE 11:
#
# Select the last 6 transactions.
#
# From this slice, select only:
# - Price
# - Revenue
# - Discount
#
# Create a new array using np.where():
#
# - Discount >= 0.15 → "high"
# - Discount between 0.05 and 0.15 → "medium"
# - Discount below 0.05 → "low"
#
# Print the result.

arr11 = sales[-6:: , [0, 2, 3]]
arr11_where = np.where(arr11[:, 2] >= 0.15, 'high', np.where(arr11[:, 2] < 0.5, 'low', 'medium'))
print(arr11_where)

# EXERCISE 12:
#
# From the original sales array:
#
# Find all transactions where:
# - Quantity is greater than 5
# AND
# - Revenue is greater than 800
#
# Then create a classification using np.where():
#
# - Revenue >= 1000 → "top"
# - Otherwise → "regular"
#
# Print the classified result.

arr12 = sales[(sales[:, 1] > 5) & (sales[:, 2] > 800)]
arr12_where = np.where(arr12 >= 1000, 'top', 'regular')
print(arr12_where)

# EXERCISE 13:
#
# Create a copy of sales.
#
# Using np.where(), modify the Price column:
#
# - If Discount >= 0.15 → decrease Price by 10
# - Otherwise → keep Price unchanged
#
# Replace the original Price column in the copy.
#
# Then:
# 1. Print the modified dataset.
# 2. Print the original Price column.
# 3. Print the modified Price column.
#
# The original sales array must remain unchanged.

sales_copy = sales.copy()
sales_copy[:, 0] = np.where(sales_copy[:, 3] >= 0.15, sales_copy[:, 0] - 10, sales_copy[:, 0])
print(sales_copy)

# DATASET 2:
#
# Each row represents one instrument.
# Each column represents one period.
#
# Values are percentage returns.

returns = np.array([
    [ 0.8, -0.4,  1.2,  0.3, -0.7,  1.5],
    [ 1.5,  0.2, -0.8,  0.9,  1.1, -0.3],
    [-0.3,  0.7,  1.8, -1.2,  0.4,  0.9],
    [ 2.1, -0.9,  0.5,  1.3, -0.2,  1.7],
    [-1.1,  0.6,  0.9, -0.5,  1.7,  0.2],
    [ 0.4,  1.2, -0.6,  2.0, -0.8,  1.4]
])


# EXERCISE 14:
#
# Select every second row starting from the last row.
#
# From those rows, select:
# - columns 1 through 5
# - every second column
#
# On the resulting array use np.where():
#
# - return > 1.0 → 1
# - return between 0 and 1.0 → 0
# - return < 0 → -1
#
# Print the result.
#
# Then calculate the average of each row
# of the resulting sliced array.

arr14 = returns[-1::-2, 0:5:2]
arr14_where = np.where(arr14 > 1, 1, np.where(arr14 < 0, -1, 0))
print(np.mean(arr14_where, axis=1))

# EXERCISE 15:
#
# Create a copy of returns.
#
# Using np.where(), replace:
#
# - returns below -0.5 → -0.5
# - all other values → unchanged
#
# Print the modified array.
#
# Then:
# 1. Calculate the average return of each instrument.
# 2. Calculate the average return of each period.
# 3. Find the instrument with the highest total return.
# 4. Print the original returns array to confirm
#    that it was not modified.

returns_copy = returns.copy()
returns_copy_ = np.where(returns_copy < -0.5, -0.5, returns_copy)
print(returns_copy)
print(np.mean(returns_copy, axis=1))
print(np.mean(returns_copy, axis=0))
total = np.sum(returns_copy, axis=1)
print(np.argmax(total))
print(returns)

###########################################################################3

# DATASET 1:
#
# Each row represents one product sale.
#
# Column 1 → Price
# Column 2 → Quantity
# Column 3 → Revenue
# Column 4 → Discount
#
# Remember:
# "Column 1" means the first column from the left.
# Python index for Column 1 is 0.

sales = np.array([
    [120,  5,  600, 0.05],
    [250,  3,  750, 0.10],
    [80,  10, 800, 0.15],
    [300,  2, 600, 0.05],
    [150,  7, 1050, 0.20],
    [90,   8, 720, 0.10],
    [200,  4, 800, 0.05],
    [350,  1, 350, 0.00],
    [175,  6, 1050, 0.15],
    [110,  9, 990, 0.20]
])


# EXERCISE 16:
#
# Select rows 3 through 8.
# Remember: row numbers are counted from the top,
# starting with 1.
#
# From those rows, select:
# - Column 1
# - Column 3
# - Column 4
#
# Create a classification based on Discount:
#
# - Discount >= 0.15 → "high"
# - Discount >= 0.10 → "medium"
# - Otherwise → "low"
#
# Print the classification.

arr16 = sales[2:8:, [0, 2, 3]]
arr16_where = np.where(arr16[:, 2] >= 0.15, 'high', np.where(arr16[:, 2] < 0.10, 'low', 'medium'))
print(arr16_where)

# EXERCISE 17:
#
# From the original sales array, select transactions where:
#
# - Quantity is greater than 5
# AND
# - Discount is at least 0.10
#
# Then use np.where() based on Revenue:
#
# - Revenue >= 1000 → "top"
# - Revenue >= 800 → "good"
# - Otherwise → "normal"
#
# Print the classification.
#
# Do not classify Price, Quantity or Discount.
# Classification must be based only on Revenue.
# Column 1 → Price
# Column 2 → Quantity
# Column 3 → Revenue
# Column 4 → Discount

arr17 = sales[((sales[:, 1] > 5) & (sales [:, 3] >= 0.10))]
arr17_where = np.where(arr17[:, 2] >= 1000, 'top', np.where(arr17[:, 2] < 800, 'normal', 'good'))
print(arr17_where)

# EXERCISE 18:
#
# Create a copy of sales.
#
# Using np.where(), modify the Quantity column:
#
# - If Discount >= 0.15 → increase Quantity by 2
# - Otherwise → keep Quantity unchanged
#
# Replace the Quantity column in the copied dataset.
#
# Then calculate:
# 1. Total Quantity for each transaction is not required.
# 2. Calculate the average Quantity across all transactions.
# 3. Calculate the average Quantity only for transactions
#    where Revenue is greater than 800.
#
# Print both averages.
#
# The original sales array must remain unchanged.

sales_modified = sales.copy()
sales_modified[:, 1] = np.where(sales_modified[:, 3] >= 0.15, sales_modified[:, 1] + 2, sales_modified[:, 1])
total_quantity = sales_modified[:, 1]
print(total_quantity)
print(np.mean(sales_modified[:, 1]))
arr18_where = sales[sales_modified[:, 2] > 800]
print(np.mean(arr18_where[:, 1]))

# DATASET 2:
#
# Each row represents one trading strategy.
# Each column represents one trading period.
#
# Values are percentage returns.

returns = np.array([
    [ 0.8, -0.4,  1.2,  0.3, -0.7,  1.5],
    [ 1.5,  0.2, -0.8,  0.9,  1.1, -0.3],
    [-0.3,  0.7,  1.8, -1.2,  0.4,  0.9],
    [ 2.1, -0.9,  0.5,  1.3, -0.2,  1.7],
    [-1.1,  0.6,  0.9, -0.5,  1.7,  0.2],
    [ 0.4,  1.2, -0.6,  2.0, -0.8,  1.4]
])


# EXERCISE 19:
#
# Select:
# - rows 2 through 6
# - columns 2 through 6
#
# Then take every second column from that selection.
#
# On the resulting array use np.where():
#
# - return >= 1.0 → 1
# - return >= 0 → 0
# - return < 0 → -1
#
# Print the resulting array.
#
# Then calculate the average of each row
# of the resulting array.

arr19 = returns[1:6, 1:6:2]
arr19_where = np.where(
    arr19 >= 1.0,
    1,
    np.where(arr19 >= 0, 0, -1)
)
print(arr19_where)
print(np.mean(arr19_where, axis=1))

# EXERCISE 20:
#
# Create a copy of returns.
#
# Using np.where(), transform every return:
#
# - return > 1.0 → 1.0
# - return < -1.0 → -1.0
# - all other returns → unchanged
#
# Print the modified array.
#
# Then:
# 1. Calculate the total return of each strategy.
# 2. Find the index of the strategy with the highest
#    total return.
# 3. Calculate the average return of each period.
#
# The original returns array must remain unchanged.

returns_modified = returns.copy()
returns_modified = np.where(returns_modified > 1.0, 1, np.where(returns_modified < -1.0, -1.0, returns_modified))
print(returns_modified)
print(np.sum(returns_modified, axis=1))
print(np.argmax(np.sum(returns_modified, axis=1)))
print(np.mean(returns_modified, axis=0))
print(returns)