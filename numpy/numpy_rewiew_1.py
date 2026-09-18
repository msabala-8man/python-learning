import numpy as np

# TOPIC:
# NumPy: Review of Checkpoint 4
#
# - slicing
# - 2D indexing
# - boolean masks
# - multiple conditions
# - aggregations
# - axis
# - argmax
# - copy
# - transpose
# - flatten
# - split

np.set_printoptions(suppress=True)

# DATASET

data = np.array([
    [120,  5,  600, 0.12],
    [250,  3,  750, 0.08],
    [80,  10, 800, 0.15],
    [300,  2,  600, 0.05],
    [150,  7, 1050, 0.10],
    [90,  8, 720, 0.20],
    [200,  4, 800, 0.07],
    [350,  1, 350, 0.03],
    [175,  6, 1050, 0.11],
    [110,  9, 990, 0.18]
])

# column 0 → Price
# column 1 → Quantity
# column 2 → Revenue
# column 3 → Discount


# EXERCISE 1:
# Select the last 4 rows and only the first 3 columns.

print([data[-4::,:3:]])

# EXERCISE 2:
# Calculate the average of each selected column.

filtered_1 = data[-4::,:3:]
print(np.mean(filtered_1, axis=0))

# EXERCISE 3:
# Select all rows where:
# - Revenue is greater than 800
# - AND Discount is greater than 0.10

filtered_2 = data[((data[:, 2] > 800) & (data[:, 3] > 0.1))]
print(filtered_2)

# EXERCISE 4:
# From the rows selected in Exercise 3, calculate:
# - average Price
# - maximum Revenue
# - standard deviation of Quantity

print(np.mean(filtered_2[:, 0]))
print(np.max(filtered_2[:, 2]))
print(np.std(filtered_2[:, 1]))

# EXERCISE 5:
# Count how many rows have Quantity greater than 5.

print(np.sum(data[:, 1] > 5))

# EXERCISE 6:
# Find the index of the row with the highest Revenue.

print(np.argmax(data[:, 2]))

# EXERCISE 7:
# Create a copy of the "data" array.
# In the copy, increase every Price by 10.
# The original "data" array must remain unchanged.

data_copy = data.copy()
data_copy[:, 0] += 10
print(data)
print(data_copy)

# EXERCISE 8:
# From the copied dataset, select every second row,
# starting from the last row and moving upwards.

print(data_copy[-1::-2, ::])

# EXERCISE 9:
# Transpose the original "data" array.
# Print the transposed array and its shape.

data_transpose = data.T
print(data_transpose, data_transpose.shape)

# EXERCISE 10:
# Flatten the transposed array.
# Split it into 5 equal parts.
# Print all five parts separately.

data_transpose_flatten = data_transpose.flatten()
data_transpose_flatten_split = np.split(data_transpose_flatten, 5)
print(data_transpose_flatten_split[0])
print(data_transpose_flatten_split[1])
print(data_transpose_flatten_split[2])
print(data_transpose_flatten_split[3])
print(data_transpose_flatten_split[4])
