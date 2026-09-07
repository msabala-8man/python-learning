import numpy as np

np.set_printoptions(suppress=True)

# DATASET 1

data = np.array([
    [120,  5,  600, 0.12],
    [250,  3,  750, 0.08],
    [80,  10, 800, 0.15],
    [300,  2,  600, 0.05],
    [150,  7, 1050, 0.10],
    [90,  8,  720, 0.20],
    [200,  4,  800, 0.07],
    [350,  1,  350, 0.03],
    [175,  6, 1050, 0.11],
    [110,  9, 990, 0.18]
])

# index 0 → Price
# index 1 → Quantity
# index 2 → Revenue
# index 3 → Discount

# TASK 1/3:
#
# Work with the "data" array.
#
# 1. Print the last 5 rows using slicing.

print(data[-5::])

# 2. From these last 5 rows, select only:
#    - Price
#    - Quantity
#    - Revenue

print(data[-5::, 0:3:])

# 3. Calculate the average of each selected column.

print(np.mean(data[-5::, 0:3:], axis=0))

# 4. Find all rows where Revenue is greater than 800.

filtered_1_1 = data[data[:, 2] > 800]
print(filtered_1_1)

# 5. From those rows, calculate:
#    - average Price
#    - maximum Quantity
#    - standard deviation of Revenue

print(np.mean(filtered_1_1[:, 0]))
print(np.max(filtered_1_1[:, 1]))
print(np.std(filtered_1_1[:, 2]))

# 6. Find the index of the row with the highest Revenue.

print(np.argmax(data[:, 2]))

# 7. Create a copy of the dataset.
#    Add 10 to every Price in the copied dataset.
#    Do not modify the original "data" array.

copy_data = data.copy()
copy_data[:, 0] += 10 

# 8. Print the original Price column
#    and the modified Price column.

print(data, copy_data)

# DATASET 2

returns = np.array([
    [ 0.8, -0.4,  1.2,  0.3, -0.7],
    [ 1.5,  0.2, -0.8,  0.9,  1.1],
    [-0.3,  0.7,  1.8, -1.2,  0.4],
    [ 2.1, -0.9,  0.5,  1.3, -0.2],
    [-1.1,  0.6,  0.9, -0.5,  1.7],
    [ 0.4,  1.2, -0.6,  2.0, -0.8]
])


# TASK 2/3:
#
# 1. Select every second row,
#    starting from the last row and moving upwards.

print(returns[-1::-2, ::])

# 2. From the resulting array, select columns
#    from the second column to the last column,
#    taking every second column.

filtered_2_1 = returns[-1::-2, ::]
print(filtered_2_1[::, 1::2])

# 3. Calculate the mean of each row
#    of the resulting array.

filtered_2_2 = filtered_2_1[::, 1::2]
print(np.mean(filtered_2_2, axis=1))

# 4. Find all returns greater than 1.0.

filtered_2_3 = returns[returns > 1]
print(filtered_2_3)

# 5. Count how many returns are negative.

print(np.sum(returns < 0))

# 6. Calculate the average of all returns
#    between -0.5 and 1.0.

filtered_2_4 = returns[(returns > -0.5) & (returns < 1)]
print(np.mean(filtered_2_4))

# 7. Calculate the total return of each original instrument.

total_instruments = np.sum(returns, axis=1)
print(total_instruments)

# 8. Find the index of the instrument
#    with the highest total return.

print(np.argmax(total_instruments))

# 9. Transpose the original "returns" array.
#    Print its shape.

returns_transpose = returns.T

print(returns_transpose, returns_transpose.shape)

# 10. Flatten the transposed array
#     and split it into 3 equal parts.
#     Print all three parts.

returns_transpose_flatten = returns_transpose.flatten()
returns_transpose_flatten_split = np.split(returns_transpose_flatten, 3)
print(returns_transpose_flatten_split[0])
print(returns_transpose_flatten_split[1])
print(returns_transpose_flatten_split[2])

# DATASET 3

# TASK 3/3:

iris = np.loadtxt(
    "Iris.csv",
    delimiter=",",
    skiprows=1,
    usecols=(1, 2, 3, 4)
)

#column 0 → SepalLength
#column 1 → SepalWidth
#column 2 → PetalLength
#column 3 → PetalWidth

# 1. Select rows from index 20 up to,
#    but not including, index 80.

print(iris[20:80:, :])

# 2. From these rows, select only:
#    - SepalLength
#    - PetalLength

filtered_3_1 = iris[20:80:, :]
print(filtered_3_1[:, 0:3:2])

# 3. Calculate the average of each selected measurement.

filtered_3_2 = filtered_3_1[:, 0:3:2]
print(np.mean(filtered_3_2, axis=0))

# 4. From the original "iris" array,
#    select flowers where:
#    SepalLength > 6.0
#    AND
#    PetalWidth > 1.5

filtered_3_3 = iris[(iris[:, 0] > 6) & (iris[:, 3] > 1.5)]
print(filtered_3_3)

# 5. Calculate the number of selected flowers.

print(np.sum((iris[:, 0] > 6) & (iris[:, 3] > 1.5)))

# 6. Calculate the average of all four measurements
#    for the selected flowers.

print(np.mean(filtered_3_3))

# 7. Calculate the average of each measurement separately.

print(np.mean(filtered_3_3, axis=0))

# 8. Find the maximum value of each measurement.

print(np.max(filtered_3_3, axis=0))

# 9. Find the minimum value of each measurement.

print(np.min(filtered_3_3, axis=0))

# 10. Take the selected flowers and:
#     - transpose the array
#     - flatten the transposed array
#     - split the result into 4 equal parts
#
#     Print each part separately.

filtered_3_3_transpose = filtered_3_3.T
filtered_3_3_transpose_flatten = filtered_3_3_transpose.flatten()
filtered_3_3_transpose_flatten_split = np.split(filtered_3_3_transpose_flatten, 4)
print(filtered_3_3_transpose_flatten_split[0])
print(filtered_3_3_transpose_flatten_split[1])
print(filtered_3_3_transpose_flatten_split[2])
print(filtered_3_3_transpose_flatten_split[3])

# 11. Create a copy of the selected flowers.
#     Add 0.1 to every PetalWidth.
#     Print the original PetalWidth column
#     and the modified PetalWidth column.
filtered_3_3_copy = filtered_3_3.copy()
filtered_3_3_copy[:, 3] += 0.1
print(filtered_3_3)
print(filtered_3_3_copy)



