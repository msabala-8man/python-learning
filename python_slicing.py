import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# # EXERCISE 1:
# # Print the first 5 elements.
# print(arr[:5])
# # EXERCISE 2:
# # Print all elements starting from index 5.
# print(arr[5:])
# # EXERCISE 3:
# # Print the last 4 elements using negative indexing.
# print(arr[-4:])
# # EXERCISE 4:
# # Print every second element, starting from the first element.
# print(arr[::2])
# # EXERCISE 5:
# # Print the elements from index 2 up to, but not including, index 8,
# # taking every second element.
# print(arr[2:8:2])


arr = np.array([
    10, 20, 30, 40, 50,
    60, 70, 80, 90, 100,
    110, 120, 130, 140, 150
])

matrix = np.array([
    [10, 20, 30, 40, 50, 60],
    [70, 80, 90, 100, 110, 120],
    [130, 140, 150, 160, 170, 180],
    [190, 200, 210, 220, 230, 240],
    [250, 260, 270, 280, 290, 300]
])

# EXERCISE 6:
# Print every second element of arr,
# starting from the last element and moving backwards.

print(arr[::-2])

# EXERCISE 7:
# Print the elements of arr from index 3 up to,
# but not including, index 13,
# taking every third element.

print(arr[3:13:3])

# EXERCISE 8:
# Print the last 6 elements of arr in reverse order,
# taking every second element.

print(arr[-1:-7:-2])

# EXERCISE 9:
# From matrix, print:
# - rows from index 1 up to, but not including, index 4
# - columns from index 2 up to, but not including, index 5

print(matrix[1:4, :])
print(matrix[:, 2:5])

#EXERCISE 10:
#From matrix, print:
#- every second row, starting from the last row
#- every second column, starting from the last column

print(matrix[-1::-2, :])
print(matrix[:, -1::-2])

#########################################################

arr2 = np.array([
    10, 20, 30, 40, 50,
    60, 70, 80, 90, 100,
    110, 120, 130, 140, 150
])


# EXERCISE 11:
# Print the array in reverse order,
# taking every second element.

print(arr2[::-2])

# EXERCISE 12:
# Print the last 8 elements in reverse order,
# taking every second element.

print(arr2[-1:-9:-2])

# EXERCISE 13:
# Print the elements from index 12 down to,
# but not including, index 4,
# taking every third element.

###

print(arr2[-3:4:-2])

# EXERCISE 15:
# Print the elements from index 13 down to,
# but not including, index 2,
# taking every third element.

print(arr2[13:2:-3])
