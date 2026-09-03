import numpy as np

# TOPIC:
# NumPy: 2D Arrays and Axis
#
# - 2D arrays
# - rows and columns
# - shape, ndim, size
# - 2D indexing
# - selecting rows and columns
# - axis=0 and axis=1


# EXERCISE 0:
#
# 1. Print the shape of the array.
# 2. Print the number of dimensions.
# 3. Print the total number of elements.
# 4. Print the second row.
# 5. Print the third column.
# 6. Calculate the average score for each row.
# 7. Calculate the average score for each column.
# 8. Calculate the total score for each row.
# 9. Find the maximum score for each column.
# 10. Find the minimum score for each row.

scores = np.array([
    [72, 88, 91],
    [64, 55, 83],
    [77, 96, 69]
])

print(scores.shape) # 1
print(scores.ndim)  # 2
print(scores.size)  # 3
print(scores[1])    # 4
print(scores[:, 2]) # 5
print(np.mean(scores, axis=1))  # 6
print(np.mean(scores, axis=0))  # 7
print(np.sum(scores, axis=1))   # 8
print(np.max(scores, axis=0))   # 9
print(np.min(scores, axis=1))   # 10

# EXERCISE 1:
#
# Create a 2D NumPy array called scores:
#
# [
#     [72, 88, 91],
#     [64, 55, 83],
#     [77, 96, 69]
# ]
#
# 1. Print the entire array.
# 2. Print the shape.
# 3. Print the number of dimensions.
# 4. Print the total number of elements.
# 5. Print the second row.
# 6. Print the third column.

scores = np.array([[72, 88, 91],
                   [64, 55, 83],
                   [77, 96, 69]])

print(scores)           # 1
print(scores.shape)     # 2
print(scores.ndim)      # 3
print(scores.size)      # 4
print(scores[1])        # 5
print(scores[:, 2])     # 6

# EXERCISE 2:
#
# Use the following array:
#
# [
#     [10, 20, 30, 40],
#     [15, 25, 35, 45],
#     [20, 30, 40, 50]
# ]
#
# 1. Calculate the average of each row.
# 2. Calculate the average of each column.
# 3. Calculate the sum of each row.
# 4. Calculate the sum of each column.

data = np.array([[10, 20, 30, 40],
                    [15, 25, 35, 45],
                    [20, 30, 40, 50]])

print(np.mean(data, axis=1))    # 1
print(np.mean(data, axis=0))    # 2
print(np.sum(data, axis=1))     # 3
print(np.sum(data, axis=0))     # 4


# EXERCISE 3:

data = np.array([
    [12, 25, 38, 41, 56],
    [18, 31, 27, 49, 52],
    [22, 14, 35, 58, 61],
    [9,  28, 44, 36, 68]
])

# # 1. Find the maximum value in each row.
# # 2. Find the minimum value in each row.
# # 3. Find the maximum value in each column.
# # 4. Find the minimum value in each column.
# # 5. Calculate the range of each row.

print(np.max(data, axis=1))     # 1
print(np.min(data, axis=1))     # 2
print(np.max(data, axis=0))     # 3
print(np.min(data, axis=0))     # 4
print(np.max(data, axis=1) - np.min(data, axis=1))  # 5


# Exercise 4 

# 1. Calculate the total return of each strategy.
#
# 2. Calculate the average daily return of each strategy.
#
# 3. Find the best day for each strategy.
#
# 4. Find the worst day for each strategy.
#
# 5. Calculate the range between the best and worst day
#    for each strategy.
#
# 6. Calculate the average return for each day
#    across all strategies.
#
# 7. Find the best-performing strategy based on total return.
#
# 8. Find the worst-performing strategy based on total return.

returns = np.array([
    [ 0.8, -0.4,  1.2,  0.5, -0.7,  1.1],
    [-0.3,  1.1,  0.6, -0.8,  1.4,  0.2],
    [ 0.5,  0.2, -0.9,  1.3,  0.7, -0.4],
    [ 1.0, -0.6,  0.4,  0.8, -0.2,  1.5]
])

print(np.sum(returns, axis=1))      # 1
print(np.mean(returns, axis=1))     # 2
print(np.max(returns, axis=1))      # 3
print(np.min(returns, axis=1))      # 4
print(np.max(returns, axis=1) - np.min(returns, axis=1))     # 5
print(np.mean(returns, axis=0))                              # 6 
print(np.max(np.sum(returns, axis=1)))                       # 7
print(np.min(np.sum(returns, axis=1)))                       # 8

# EXERCISE 5:
#
# 1. Calculate the total return of each strategy.
#
# 2. Calculate the average daily return of each strategy.
#
# 3. Calculate the standard deviation of each strategy.
#
# 4. Calculate the range between the best and worst return
#    for each strategy.
#
# 5. Find the best total return among all strategies.
#
# 6. Find the worst total return among all strategies.
#
# 7. Calculate the average return for each trading day
#    across all strategies.
#
# 8. Find the best average-return day.
#
# 9. Find the worst average-return day.
#
# 10. Calculate the total return of all strategies combined.

returns = np.array([
    [ 0.8, -0.4,  1.2,  0.5, -0.7,  1.1,  0.3, -0.2],
    [-0.3,  1.1,  0.6, -0.8,  1.4,  0.2, -0.5,  0.9],
    [ 0.5,  0.2, -0.9,  1.3,  0.7, -0.4,  1.0,  0.6],
    [ 1.0, -0.6,  0.4,  0.8, -0.2,  1.5, -0.3,  0.7],
    [-0.7,  0.9,  1.1, -0.5,  0.3,  0.8, -0.6,  1.2]
])

print(np.sum(returns, 1))   # 1
print(np.mean(returns, 1))  # 2
print(np.std(returns, 1))   # 3
print(np.max(returns, 1) - np.min(returns, 1))  # 4
print(np.max(np.sum(returns, 1)))   # 5
print(np.min(np.sum(returns, 1)))   # 6
print(np.mean(returns, 0))          # 7
print(np.max(np.mean(returns, 0)))  # 8
print(np.min(np.mean(returns, 0)))  # 9
print(np.sum(np.sum(returns, 1)))   # 10

