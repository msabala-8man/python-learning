import numpy as np


# EXERCISE 1:
#
# Generate 10 random integers between 1 and 100.
# Print the array.
# Print its mean, minimum, and maximum.
# Count how many generated values are greater than 50.

arr_1 = np.random.randint(1, 101 , 10)
print(arr_1)
print(np.mean(arr_1), np.min(arr_1), np.max(arr_1))
print(np.sum(arr_1 > 50))


# EXERCISE 2:
#
# Generate a 4 x 5 array of random floating-point numbers
# between 0 and 1.
# Print the array.
# Print its shape.
# Calculate the mean of each row.
# Calculate the mean of each column.

arr_2 = np.random.rand(4, 5)
print(arr_2)
print(arr_2.shape)
print(np.mean(arr_2, axis=1))
print(np.mean(arr_2, axis=0))

# EXERCISE 3:
#
# Generate 20 random values from a standard normal distribution.
# Print the array.
# Calculate the mean and standard deviation.
# Count how many values are negative.
# Count how many values are greater than 1.

arr_3 = np.random.randn(20)
print(arr_3)
print(np.mean(arr_3), np.std(arr_3))
print(np.sum(arr_3 < 0))
print(np.sum(arr_3 > 1))

# EXERCISE 4:
#
# Generate a 5 x 5 array of random integers from 10 to 50.
#
# 1. Select all values greater than 40 from this generated array.
# 2. Count how many selected values there are.
# 3. In the original generated array, replace every value below 20 with 20.
# 4. Print the modified array.
# 5. Print the minimum value of the modified array.
# 6. Print the maximum value of the modified array.

arr_4 = np.random.randint(10, 51, (5, 5))
print(arr_4)
arr_4_filtered = arr_4[arr_4 > 40]
print(arr_4_filtered)
print(np.sum(arr_4 > 40))
arr_4_modified = np.where(arr_4 < 20, 20, arr_4)
print(arr_4_modified)
print(np.min(arr_4_modified))
print(np.max(arr_4_modified))

# EXERCISE 5:
#
# Simulate 1000 observations from a standard normal distribution.
#
# Calculate the mean and standard deviation.
# Count how many observations are between -1 and 1.
# Calculate what percentage of observations fall between -1 and 1.
# Count how many observations are greater than 2.
# Print the results.

arr_5 = np.random.randn(1000)
print(np.mean(arr_5))
print(np.std(arr_5))
print(np.sum((arr_5 < 1) & (arr_5 > -1)))
print(np.sum((arr_5 > -1) & (arr_5 < 1))/1000 * 100)
print(np.sum(arr_5 > 2))