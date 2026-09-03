import numpy as np

iris = np.loadtxt(
    "Iris.csv",
    delimiter=",",
    skiprows=1,
    usecols=(1, 2, 3, 4)
)

# print(iris)
# print(iris.shape)
# print(iris.ndim)
# print(iris.size)

# TOPIC:
# NumPy: Working with a real CSV dataset
#
# EXERCISE 1:
# Use the Iris dataset loaded into the `iris` NumPy array.
#
# 1. Print the shape of the array.
# 2. Print the number of dimensions.
# 3. Print the total number of elements.
# 4. Calculate the average of each column.
# 5. Calculate the minimum value of each column.
# 6. Calculate the maximum value of each column.
# 7. Calculate the standard deviation of each column.
# 8. Calculate the average of each row.

# print(iris.shape)               # 1
# print(iris.ndim)                # 2
# print(iris.size)                # 3
# print(np.mean(iris, axis=0))    # 4
# print(np.min(iris, axis=0))     # 5
# print(np.max(iris, axis=0))     # 6
# print(np.std(iris, axis=0))     # 7
# print(np.mean(iris, axis=1))    # 8

# EXERCISE 2:
#
# 1. Print all rows where SepalLength is greater than 6.0.
# 2. Print all rows where PetalLength is greater than 5.0.
# 3. Print all rows where PetalWidth is less than 0.5.
# 4. Print all rows where SepalLength is greater than 6.0
#    AND PetalLength is greater than 5.0.
# 5. Count how many flowers have PetalLength greater than 5.0.
# 6. Count how many flowers have SepalWidth less than 3.0.
# 7. Calculate the average PetalLength for flowers
#    where PetalLength is greater than 5.0.
# 8. Calculate the average SepalLength for flowers
#    where PetalWidth is greater than 2.0.

#column 0 → SepalLength
#column 1 → SepalWidth
#column 2 → PetalLength
#column 3 → PetalWidth

print(iris[iris[:, 0] > 6])                                             # 1
print(iris[iris[:, 2] > 5])                                             # 2
print(iris[iris[:, 3] < 0.5])                                           # 3
print(iris[(iris[:, 0] > 6) & (iris[:, 2] > 5)])                        # 4
petallength_greater_than_5 = iris[iris[:, 2] > 5]                       # 5
print(petallength_greater_than_5[petallength_greater_than_5 > 5].size)  # 5
sepalwidth_less_than_3 = iris[iris[:, 1] < 3]                           # 6
print(sepalwidth_less_than_3[sepalwidth_less_than_3 < 3].size)          # 6
print(np.mean(petallength_greater_than_5[:, 2], axis=0))                # 7
petalwidth_greater_than_2 = iris[iris[:, 3] > 2]                        # 8
print(np.mean(petalwidth_greater_than_2[:, 0], axis=0))                 # 8