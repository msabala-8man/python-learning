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

print(iris.shape)               # 1
print(iris.ndim)                # 2
print(iris.size)                # 3
print(np.mean(iris, axis=0))    # 4
print(np.min(iris, axis=0))     # 5
print(np.max(iris, axis=0))     # 6
print(np.std(iris, axis=0))     # 7
print(np.mean(iris, axis=1))    # 8

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


# EXERCISE 3:
#
# 1. Calculate the average SepalLength for flowers
#    where SepalLength is greater than 6.0.
#
# 2. Calculate the average PetalWidth for flowers
#    where PetalLength is greater than 5.0.
#
# 3. Find the maximum PetalLength among flowers
#    where SepalWidth is less than 3.0.
#
# 4. Find the minimum SepalLength among flowers
#    where PetalWidth is greater than 1.5.
#
# 5. Count how many flowers have both:
#    SepalLength greater than 6.0
#    AND PetalWidth greater than 1.5.
#
# 6. Count how many flowers have either:
#    PetalLength greater than 5.5
#    OR SepalLength less than 5.0.
#
# 7. Calculate the average of all four measurements
#    for flowers where PetalWidth is greater than 2.0.
#
# 8. Calculate the standard deviation of PetalLength
#    for flowers where SepalLength is greater than 6.5.

#column 0 → SepalLength
#column 1 → SepalWidth
#column 2 → PetalLength
#column 3 → PetalWidth

sepallenght_greater_than_6 = iris[iris[:, 0] > 6]   # 1
print(np.mean(sepallenght_greater_than_6[:, 0]))    # 1
petallength_greater_than_5 = iris[iris[:, 2] > 5]   # 2
print(np.mean(petallength_greater_than_5[:, 3]))    # 2
sepalwidth_less_than_3 = iris[iris[:, 1] < 3]       # 3
print(np.max(sepalwidth_less_than_3[:, 2]))         # 3
petalwidth_greater_than_1_point_5 = iris[iris[:, 3] > 1.5]  # 4
print(np.min(petalwidth_greater_than_1_point_5[:, 0]))      # 4
print(np.sum((iris[:, 0] > 6) & (iris[:, 3] > 1.5)))        # 5
print(np.sum((iris[:, 2] > 5.5) | (iris[:, 0] < 5)))        # 6
print(np.mean(iris[:, 3] > 2))                              # 7
sepallenght_greater_than_6_point_5 = iris[iris[:, 0] > 6.5] # 8
print(np.std(sepallenght_greater_than_6_point_5[:, 2]))     # 8


# EXERCISE 4:
#
# 1. Calculate the average SepalWidth for flowers
#    where SepalLength is greater than 6.5.
#
# 2. Calculate the average PetalLength for flowers
#    where PetalWidth is greater than 1.5.
#
# 3. Find the maximum SepalLength for flowers
#    where PetalLength is greater than 5.0.
#
# 4. Find the minimum PetalWidth for flowers
#    where SepalWidth is less than 3.0.
#
# 5. Count how many flowers have both:
#    SepalWidth less than 3.0
#    AND PetalLength greater than 5.0.
#
# 6. Count how many flowers have either:
#    SepalLength greater than 7.0
#    OR PetalWidth less than 0.3.
#
# 7. Calculate one average from all measurements
#    for flowers where SepalLength is greater than 6.0.
#
# 8. Calculate the standard deviation of SepalWidth
#    for flowers where PetalLength is greater than 4.5.

#column 0 → SepalLength
#column 1 → SepalWidth
#column 2 → PetalLength
#column 3 → PetalWidth

sepallength_greater_than_6_point_5 = iris[iris[:, 0] > 6.5] # 1
print(np.mean(sepallength_greater_than_6_point_5[:, 1]))    # 1
petalwidth_greater_than_1_point_5 = iris[iris[:, 3] > 1.5]  # 2
print(np.mean(petalwidth_greater_than_1_point_5[:, 2]))     # 2
petallength_greater_than_5 = iris[iris[:, 2] > 5]           # 3
print(np.max(petallength_greater_than_5[:, 0]))             # 3
sepalwidth_less_than_3 = iris[iris[:, 1] < 3]               # 4
print(np.min(sepalwidth_less_than_3[:, 3]))                 # 4
print(np.sum((iris[:, 1] < 3) & (iris[:, 2] > 5)))          # 5
print(np.sum((iris[:, 0] > 7) | (iris[:, 3] < 0.3)))        # 6
print(np.mean(iris[iris[:, 0] > 6]))                        # 7
petallength_greater_than_4_point_5 = iris[iris[:, 2] > 4.5] # 8
print(np.std(petallength_greater_than_4_point_5[:, 1]))     # 8

# EXERCISE 5:
#
# 1. Calculate the average PetalLength for flowers
#    where SepalLength is greater than 6.5.
#
# 2. Find the maximum PetalWidth for flowers
#    where SepalWidth is less than 3.0.
#
# 3. Find the minimum SepalLength for flowers
#    where PetalLength is greater than 5.0
#    AND PetalWidth is greater than 1.5.
#
# 4. Count how many flowers have:
#    SepalLength greater than 6.0
#    AND SepalWidth less than 3.0.
#
# 5. Count how many flowers have either:
#    PetalLength greater than 5.0
#    OR PetalWidth greater than 2.0.
#
# 6. Calculate the standard deviation of SepalLength
#    for flowers where PetalLength is greater than 4.5.
#
# 7. Calculate the average of all four measurements
#    for flowers where:
#    SepalLength is greater than 6.0
#    AND PetalWidth is greater than 1.5.
#
# 8. For flowers where SepalLength is greater than 6.0,
#    calculate the average of each measurement separately.

#column 0 → SepalLength
#column 1 → SepalWidth
#column 2 → PetalLength
#column 3 → PetalWidth

sepallength_greater_than_6p5 = iris[iris[:, 0] > 6.5]   # 1
print(np.mean(sepallength_greater_than_6p5[:, 2]))      # 1 
sepalwidth_less_than_3 = iris[iris[:, 1] < 3]           # 2
print(np.max(sepalwidth_less_than_3[:, 3]))             # 2
filtered3 = iris[(iris[:, 2] > 5) & (iris[:, 3] > 1.5)] # 3
print(np.min(filtered3[:, 0]))                          # 3
print(np.sum((iris[:, 0] > 6) & (iris[:, 1] < 3)))      # 4
print(np.sum((iris[:, 2] > 5) | (iris[:, 3] > 2)))      # 5
petallength_greater_than_4p5 = iris[iris[:, 2] > 4.5]   # 6
print(np.std(petallength_greater_than_4p5[:, 0]))       # 6
filtered7 = iris[(iris[:, 0] > 6) & (iris[:, 3] > 1.5)] # 7
print(np.mean(filtered7))                               # 7
sepallength_greater_than_6 = iris[iris[:, 0] > 6]       # 8
print(np.mean(sepallength_greater_than_6, axis=0))      # 8

