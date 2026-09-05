import numpy as np

# TOPIC:
# NumPy: Axis Practice with 2D Arrays
#
# - axis=0
# - axis=1
# - calculations across rows and columns


data = np.array([
    [12, 25, 38, 41, 56, 63],
    [18, 31, 27, 49, 52, 70],
    [22, 14, 35, 58, 61, 77],
    [9,  28, 44, 36, 68, 55],
    [16, 33, 29, 47, 73, 81]
])



# EXERCISE:
#
# 1. Print the shape of the array.
# 2. Calculate the average for each row.
# 3. Calculate the average for each column.
# 4. Calculate the sum for each row.
# 5. Calculate the sum for each column.
# 6. Find the maximum value in each row.
# 7. Find the minimum value in each column.
# 8. Calculate the difference between the maximum
#    and minimum value for each row.
# 9. Calculate the difference between the maximum
#    and minimum value for each column.

print(data.shape)               # 1.
print(np.mean(data, axis=1))    # 2.
print(np.mean(data, 0))         # 3.
print(np.sum(data, axis=1))     # 4.
print(np.sum(data, axis=0))     # 5.
print(np.max(data, axis=1))     # 6.
print(np.min(data, axis=0))     # 7.
print(np.max(data, axis=1)-np.min(data, axis=1))    # 8.
print(np.max(data, axis=0)-np.min(data, axis=0))    # 9.
