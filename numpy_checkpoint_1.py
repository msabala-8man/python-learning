import numpy as np

data = np.array([
    [120, 5,  600,  0.12],
    [250, 3,  750,  0.08],
    [80,  10, 800,  0.15],
    [300, 2,  600,  0.05],
    [150, 7,  1050, 0.10],
    [90,  8,  720,  0.20],
    [200, 4,  800,  0.07],
    [350, 1,  350,  0.03],
    [175, 6,  1050, 0.11],
    [110, 9,  990,  0.18]
])

# 0 → price
# 1 → quantity
# 2 → revenue
# 3 → discount

np.set_printoptions(suppress=True)

# 1. Print the shape of the dataset.
print(data.shape)
# 2. Print the number of dimensions.
print(data.ndim)
# 3. Print the total number of elements.
print(data.size)
# 4. Print the average of each column.
print(np.mean(data, axis=0))
# 5. Print the minimum value of each column.
print(np.min(data, axis=0))
# 6. Print the maximum value of each column.
print(np.max(data, axis=0))
# 7. Calculate the total revenue.
print(np.sum(data[:, 2]))
# 8. Calculate the average revenue.
print(np.mean(data[:, 2]))
# 9. Calculate the average revenue for each row.
print(np.mean(data, axis=1))
# 10. Find all rows where revenue is greater than 800.
print(data[data[:, 2] > 800])
# 11. Find all rows where quantity is greater than 5
#     AND discount is greater than 0.10.
print(data[(data[:, 1] > 5) & (data[:, 3] > 0.1)])
# 12. Count how many rows have revenue greater than or equal to 800.
print(sum(data[:, 2] >= 800))
# 13. Calculate the average price for rows
#     where quantity is greater than 5.
filtered_13 = data[data[:, 1] > 5]
print(np.mean(filtered_13[:, 0]))