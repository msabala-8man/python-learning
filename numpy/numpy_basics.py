import numpy as np

scores = np.array([72, 88, 91, 64, 55, 83, 77, 96, 69, 81])

total = np.sum(scores)
average = np.mean(scores)
minimum = np.min(scores)
maximum = np.max(scores)
standard_deviation = np.std(scores)

scores_80_or_more = scores[scores >= 80]
below_70 = scores[scores < 70]
between_70_and_90 = scores[(scores > 70) & (scores < 90)]

scores_plus_5 = scores + 5

print("Total:", total)
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Standard deviation:", standard_deviation)
print("Scores 80 or more:", scores_80_or_more)
print("Below 70:", below_70)
print("Between 70 and 90:", between_70_and_90)
print("Scores plus 5:", scores_plus_5)

# TOPIC:
# NumPy Basics - Exercise 1
#
# - creating arrays
# - basic calculations
# - basic statistics



# EXERCISE 1

# 1. Print the array.
#
# 2. Print the number of elements.
#
# 3. Add 10 to every number.
#
# 4. Multiply every number by 2.
#
# 5. Divide every number by 5.
#
# 6. Calculate the total.
#
# 7. Calculate the average.
#
# 8. Find the minimum value.
#
# 9. Find the maximum value.
#
# 10. Calculate the standard deviation.

numbers = np.array([12, 25, 7, 40, 18, 33, 5, 50])

print(numbers)              # 1
print(numbers.size)         # 2
print(numbers + 10)         # 3
print(numbers * 2)          # 4
print(numbers / 5)          # 5
print(np.sum(numbers))      # 6
print(np.mean(numbers))     # 7
print(np.min(numbers))      # 8
print(np.max(numbers))      # 9
print(np.std(numbers))      # 10



# EXERCISE 2:
#
# We have prices of 6 products.
#
# 1. Create a NumPy array called prices with:
#    120, 250, 80, 300, 150, 90
#
# 2. Add 20 to every price.
#
# 3. Multiply every price by 1.1.
#
# 4. Calculate the total value of all prices.
#
# 5. Calculate the average price.
#
# 6. Find the cheapest product.
#
# 7. Find the most expensive product.
#
# 8. Calculate the difference between the most expensive
#    and cheapest product.

prices = np.array([120, 250, 80, 300, 150, 90])     # 1
print(prices + 20)                                  # 2                              
print(prices * 1.1)                                 # 3
print(np.sum(prices))                               # 4
print(np.mean(prices))                              # 5
print(np.min(prices))                               # 6 
print(np.max(prices))                               # 7
print(np.max(prices) - np.min(prices))              # 8



# EXERCISE 3:
#
# We have daily returns in percent:
#
# 0.5, -0.3, 1.2, -0.8, 0.4, 0.9, -0.2, 1.5
#
# 1. Create a NumPy array called returns.
#
# 2. Calculate the total return.
#
# 3. Calculate the average daily return.
#
# 4. Find the best daily return.
#
# 5. Find the worst daily return.
#
# 6. Calculate the standard deviation.
#
# 7. Add 0.1 percentage point to every return.
#
# 8. Multiply every return by 2.

returns = np.array([0.5, -0.3, 1.2, -0.8, 0.4, 0.9, -0.2, 1.5]) # 1
print(np.sum(returns))                                          # 2
print(np.mean(returns))                                         # 3
print(np.max(returns))                                          # 4
print(np.min(returns))                                          # 5
print(np.std(returns))                                          # 6
print(returns + 0.1)                                            # 7
print(returns * 2)                                              # 8


# EXERCISE 4:
#
# We have profit/loss from 10 trades, in percentage points:
#
#  1.2, -0.7, 2.1, -1.5, 0.4, 1.8, -0.3, 2.5, -1.1, 0.9
#
# 1. Create a NumPy array called trades.
#
# 2. Calculate the total result of all trades.
#
# 3. Calculate the average result per trade.
#
# 4. Find the best trade.
#
# 5. Find the worst trade.
#
# 6. Calculate the standard deviation of the results.
#
# 7. Add 0.2 percentage points to every trade.
#
# 8. Multiply every trade result by 1.5.
#
# 9. Calculate the range of the results:
#    maximum - minimum
#
# 10. Print the original array at the end.

trades = np.array([1.2, -0.7, 2.1, -1.5, 0.4, 1.8, -0.3, 2.5, -1.1, 0.9]) # 1
print(np.sum(trades))                                                     # 2
print(np.mean(trades))                                                    # 3
print(np.max(trades))                                                     # 4
print(np.min(trades))                                                     # 5
print(np.std(trades))                                                     # 6
print(trades + 0.2)                                                       # 7
print(trades * 1.5)                                                       # 8
print(np.max(trades) - np.min(trades))                                    # 9
print(trades)                                                             # 10


# EXERCISE 5:
#
# You are analyzing the daily P&L of a strategy.
# Values are in percentage points.
#
#  0.8, -1.2, 1.5, 0.3, -0.6, 2.0, -0.4, 1.1, 0.7, -0.9
#
# 1. Create a NumPy array called pnl.
#
# 2. Calculate the total P&L.
#
# 3. Calculate the average daily P&L.
#
# 4. Find the best day.
#
# 5. Find the worst day.
#
# 6. Calculate the standard deviation.
#
# 7. Calculate the range (best - worst).
#
# 8. Add 0.2 percentage points to every day.
#
# 9. Multiply every day's result by 2.
#
# 10. Print the original pnl array at the end.

pnl = np.array([0.8, -1.2, 1.5, 0.3, -0.6, 2.0, -0.4, 1.1, 0.7, -0.9])  # 1
print(np.sum(pnl))                                                      # 2
print(np.mean(pnl))                                                     # 3
print(np.max(pnl))                                                      # 4
print(np.min(pnl))                                                      # 5
print(np.std(pnl))                                                      # 6
print(np.max(pnl) - np.min(pnl))                                        # 7
print(pnl + 0.2)                                                        # 8
print(pnl * 2)                                                          # 9
print(pnl)                                                              # 10
