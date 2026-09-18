import numpy as np

returns = np.array([
    [ 0.8, -0.4,  1.2,  0.3, -0.7],
    [ 1.5,  0.2, -0.8,  0.9,  1.1],
    [-0.3,  0.7,  1.8, -1.2,  0.4],
    [ 2.1, -0.9,  0.5,  1.3, -0.2],
    [-1.1,  0.6,  0.9, -0.5,  1.7],
    [ 0.4,  1.2, -0.6,  2.0, -0.8]
])

# 1. Print the shape, number of dimensions,
#    and total number of elements.
print(returns.shape, returns.ndim, returns.size)
# 2. Calculate the average return for each instrument.
print(np.mean(returns, axis=1))
# 3. Calculate the average return for each period.
print(np.mean(returns, axis=0))
# 4. Calculate the total return for each instrument.
print(np.sum(returns, axis=1))
# 5. Find the maximum return for each instrument.
print(np.max(returns, axis=1))
# 6. Find the minimum return for each instrument.
print(np.min(returns, axis=1))
# 7. Calculate the standard deviation for each instrument.
print(np.std(returns, axis=1))
# 8. Calculate the range (max - min)
#    for each instrument.
print(np.max(returns, axis=1) - (np.min(returns, axis=1)))
# 9. Find all return values greater than 1.0.
print(returns[returns > 1])
# 10. Find all return values below -0.5.
print(returns[returns < -0.5])
# 11. Count how many return values are greater than 1.0.
print(np.sum(returns > 1))
# 12. Count how many return values are negative.
print(np.sum(returns < 0))
# 13. Find all rows where:
#     average return is greater than 0.5
#     AND standard deviation is below 1.0.
print(returns[(np.mean(returns, axis=1) > 0.5) & (np.std(returns, axis=1) < 1)])
# 14. Calculate the average of all returns
#     greater than 1.0.
filtered_14 = returns[returns > 1]
print(np.mean(filtered_14))
# 15. Calculate the average of all returns
#     between -0.5 and 1.0.
filtered_15 = returns[(returns < 1) & (returns > -0.5)]
print(np.mean(filtered_15))
# 16. Find the maximum return among values
#     greater than 1.0.
filtered_16 = returns[returns > 1]
print(np.max(filtered_16))
# 17. Find the minimum return among negative values.
filtered_17 = returns[returns < 0]
print(np.min(filtered_17))
# 18. Add 0.2 to every return.
print(returns + 0.2)
# 19. Multiply every return by 1.5.
print(returns * 1.5)
# 20. Find the instrument with the largest total return.
filtered_20 = np.sum(returns, axis=1)
print(np.max(filtered_20))