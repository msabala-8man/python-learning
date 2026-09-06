import numpy as np

iris = np.loadtxt(
    "Iris.csv",
    delimiter=",",
    skiprows=1,
    usecols=(1, 2, 3, 4)
)

# Columns:
# 0 = SepalLength
# 1 = SepalWidth
# 2 = PetalLength
# 3 = PetalWidth


# ============================================================
# PART 1: OVERVIEW
# ============================================================

# 1. Print the shape of the dataset.
print(iris.shape)
# 2. Print the number of dimensions.
print(iris.ndim)
# 3. Print the total number of elements.
print(iris.size)
# 4. Calculate the average of each measurement.
print(np.mean(iris, axis=0))
# 5. Find the minimum value of each measurement.
print(np.min(iris, axis=0))
# 6. Find the maximum value of each measurement.
print(np.max(iris, axis=0))
# 7. Calculate the standard deviation of each measurement.
print(np.std(iris, axis=0))

# ============================================================
# PART 2: FILTERING
# ============================================================

# 8. Find all rows where SepalLength is greater than 6.5.
print(iris[iris[:, 0] > 6.5])
# 9. Find all rows where SepalWidth is less than 3.0.
print(iris[iris[:, 1] < 3])
# 10. Find all rows where PetalLength is greater than 5.0.
print(iris[iris[:, 2] > 5])
# 11. Find all rows where PetalWidth is greater than 1.5.
print(iris[iris[:, 3] > 1.5])
# 12. Find all rows where:
#     SepalLength is greater than 6.0
#     AND
#     PetalLength is greater than 5.0.
print(iris[(iris[:, 0] > 6) & (iris[:, 2] > 5)])
# 13. Find all rows where:
#     SepalWidth is less than 3.0
#     OR
#     PetalWidth is greater than 2.0.
print(iris[(iris[:, 1] < 3) | (iris[:, 3] > 2)])

# ============================================================
# PART 3: COUNTING
# ============================================================

# 14. Count how many flowers have SepalLength greater than 6.0.
print(np.sum(iris[:, 0] > 6))
# 15. Count how many flowers have PetalLength greater than 5.0.
print(np.sum(iris[:, 2] > 5))
# 16. Count how many flowers have PetalWidth less than 0.5.
print(np.sum(iris[:, 3] < 0.5))
# 17. Count how many flowers have both:
#     SepalLength greater than 6.0
#     AND
#     PetalWidth greater than 1.5.
print(np.sum((iris[:, 0] > 6) & (iris[:, 3] > 1.5)))
# 18. Count how many flowers have either:
#     PetalLength greater than 5.0
#     OR
#     SepalLength less than 5.0.
print(np.sum((iris[:, 2] > 5) | (iris[:, 0] < 5)))

# ============================================================
# PART 4: CONDITIONAL STATISTICS
# ============================================================

# 19. Calculate the average SepalLength for flowers
#     where PetalLength is greater than 5.0.
filtered_19 = iris[iris[:, 2] > 5]
print(np.mean(filtered_19[:, 0]))
# 20. Calculate the average PetalWidth for flowers
#     where SepalLength is greater than 6.0.
filtered_20 = iris[iris[:, 0] > 6]
print(np.mean(filtered_20[:, 3]))
# 21. Find the maximum PetalLength for flowers
#     where SepalWidth is less than 3.0.
filtered_21 = iris[iris[:, 1] < 3]
print(np.max(filtered_21[:, 2]))
# 22. Find the minimum SepalLength for flowers
#     where PetalWidth is greater than 1.5.
filtered_22 = iris[iris[:, 3] > 1.5]
print(np.min(filtered_22[:, 0]))
# 23. Calculate the standard deviation of PetalLength
#     for flowers where SepalLength is greater than 6.5.
filtered_23 = iris[iris[:, 0] > 6.5]
print(np.std(filtered_23[:, 2]))
# 24. Calculate the average of ALL measurements
#     for flowers where PetalWidth is greater than 2.0.
filtered_24 = iris[iris[:, 3] > 2]
print(np.mean(filtered_24))

# ============================================================
# PART 5: AXIS PRACTICE
# ============================================================

# 25. For flowers where SepalLength is greater than 6.0,
#     calculate the average of each measurement separately.
filtered_25 = iris[iris[:, 0] > 6]
print(np.mean(filtered_25, axis=0))
# 26. For flowers where PetalWidth is greater than 1.5,
#     find the maximum value of each measurement.
filtered_26 = iris[iris[:, 3] > 1.5]
print(np.max(filtered_26, axis=0))
# 27. For flowers where PetalLength is greater than 4.5,
#     find the minimum value of each measurement.
filtered_27 = iris[iris[:, 2] > 4.5]
print(np.min(filtered_27, axis=0))


# ============================================================
# FINAL EXCIRCISE
# ============================================================

# Analyze all flowers where:
#     SepalLength is greater than 6.0
#     AND
#     PetalWidth is greater than 1.5.
#
# Report:
#
# 28. The number of flowers.
final_filtered = iris[(iris[:, 0] > 6) & (iris[:, 3] > 1.5)]
print(np.sum((iris[:, 0] > 6) & (iris[:, 3] > 1.5)))
# 29. The average of ALL four measurements.
print(np.mean(final_filtered))
# 30. The average of each measurement separately.
print(np.mean(final_filtered, axis=0))
# 31. The maximum of each measurement.
print(np.max(final_filtered, axis=0))
# 32. The minimum of each measurement.
print(np.min(final_filtered, axis=0))
# 33. The standard deviation of each measurement.
print(np.std(final_filtered, axis=0))