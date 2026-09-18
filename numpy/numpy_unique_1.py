import numpy as np

# EXERCISE 1:
#
# Print all unique values.

arr1 = np.array([10, 20, 10, 30, 20, 40, 10, 50, 30])

print(np.unique(arr1))


# EXERCISE 2:
#
# Print the unique values.
# Print how many times each unique value occurs.

arr2 = np.array([5, 7, 5, 8, 7, 5, 9, 8, 8, 10, 5])
print(np.unique(arr2, return_counts=True))

# EXERCISE 3:
#
# Store unique values in one variable.
# Store their counts in another variable.
# Print both variables.
# Print the count of the value 3.

arr3 = np.array([1, 3, 2, 1, 4, 3, 2, 5, 1, 4, 3, 3])

arr3_unique, arr3_counts = np.unique(arr3, return_counts=True)
print(arr3_unique)
print(arr3_counts)


# EXERCISE 4:
#
# Print all unique values from the entire array.
# Print how many times each value occurs.

arr4 = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [1, 2, 4],
    [3, 4, 5]
])

print(np.unique(arr4, return_counts=True))

# EXERCISE 5:
#
# Select the first three columns.
# Find all unique values in this slice.
# Find how many times each unique value occurs.

arr5 = np.array([
    [10, 20, 10, 30],
    [20, 40, 30, 20],
    [10, 50, 40, 30],
    [60, 20, 10, 40]
])

arr5_modified = arr5[::, 0:3:]
print(np.unique(arr5_modified, return_counts=True))
