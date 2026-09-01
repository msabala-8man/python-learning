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


# EXERCISE:
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
