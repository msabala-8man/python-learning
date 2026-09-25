import numpy as np

np.set_printoptions(suppress=True)

# EXERCISE 1
# Create the following 2D NumPy array:
#
# data = [
#     [120,  5, 600, 0.12],
#     [250,  3, 750, 0.08],
#     [80,  10, 800, 0.15],
#     [300,  2, 600, 0.05],
#     [150,  7, 1050, 0.10],
#     [90,  8, 720, 0.20],
#     [200,  4, 800, 0.07],
#     [350,  1, 350, 0.03],
#     [175,  6, 1050, 0.11],
#     [110,  9, 990, 0.18]
# ]

data_arr_1 = np.array([
    [120,  5, 600, 0.12],
    [250,  3, 750, 0.08],
    [80,  10, 800, 0.15],
    [300,  2, 600, 0.05],
    [150,  7, 1050, 0.10],
    [90,  8, 720, 0.20],
    [200,  4, 800, 0.07],
    [350,  1, 350, 0.03],
    [175,  6, 1050, 0.11],
    [110,  9, 990, 0.18]])


# Columns represent:
# Quantity, UnitPrice, Revenue, Discount
#
# 1. Select only rows where Quantity is greater than 100
#    and Revenue is greater than 700.
# 2. From the filtered result, select only the first three columns.
# 3. Calculate the mean of each column.
# 4. Calculate the standard deviation of each column.
# 5. Find the index of the row with the highest Revenue
#    in the filtered result from step 1.
# 6. Print the selected data, means, standard deviations,
#    and the index from step 5.

arr_1_filter = data_arr_1[(data_arr_1[:, 0] > 100) & (data_arr_1[:, 2] > 700)]
print(arr_1_filter, arr_1_filter.shape)
arr_1_filter_columns = arr_1_filter[:, 0:3]
print(arr_1_filter_columns, arr_1_filter_columns.shape)
print(np.mean(arr_1_filter_columns, axis=0))
print(np.std(arr_1_filter_columns, axis=0))
arr_1_filter_max_rev = np.max(arr_1_filter[:, 2])
print(arr_1_filter_max_rev)
arr_1_filter_argmax = arr_1_filter[arr_1_filter[:, 2]==arr_1_filter_max_rev]
print(arr_1_filter_argmax)
arr_1_filter_argmax = np.argmax(arr_1_filter[:, 2])
print(arr_1_filter_argmax, arr_1_filter[arr_1_filter_argmax])
#mam dwie wartosci max rev, ale indeks tylko 1

# EXERCISE 2
# Create the following 2D NumPy array:
#
# scores = [
#     [72, 88, 91, 64, 55],
#     [83, 76, 95, 68, 71],
#     [59, 87, 79, 92, 66],
#     [81, 73, 54, 89, 97],
#     [68, 91, 85, 77, 90],
#     [94, 62, 88, 71, 84]
# ]
#
# 1. Select rows where the average score across all five columns
#    is greater than 80.
# 2. From those rows, select only columns 2 through 5.
# 3. Calculate the average of each selected column.
# 4. Find the largest value in each selected column.
# 5. Find the index of the row with the highest average score
#    among the rows selected in step 1.
# 6. Create a new array where values below 70 are replaced with 70.
# 7. Print all important intermediate and final results.

scores = np.array([
    [72, 88, 91, 64, 55],
    [83, 76, 95, 68, 71],
    [59, 87, 79, 92, 66],
    [81, 73, 54, 89, 97],
    [68, 91, 85, 77, 90],
    [94, 62, 88, 71, 84]
])

scores_mean = np.mean(scores, axis=1)
print('Scores row mean:', scores_mean)
scores_filter = scores[scores_mean > 80]
print(scores_filter, scores_filter.shape)
scores_filter_columns = scores_filter[:, 1:5]
print(scores_filter_columns)
scores_filter_columns_mean = np.mean(scores_filter_columns, axis=0)
print(scores_filter_columns_mean)
scores_filter_columns_max = np.max(scores_filter_columns, axis=0)
print(scores_filter_columns_max)
scores_filter_mean = np.mean(scores_filter, axis=1)
print(scores_filter_mean)
scores_filter_mean_argmax = np.argmax(scores_filter_mean)
print(scores_filter_mean_argmax)
scores_rep_70 = np.where(scores_filter < 70, 70, scores_filter)
print(scores_rep_70)

# EXERCISE 3
# Create the following 2D NumPy array:
#
# sales = [
#     [120, 150, 180, 200, 220, 250],
#     [90,  130, 170, 160, 180, 210],
#     [200, 220, 190, 250, 270, 300],
#     [80,  110, 140, 130, 150, 170],
#     [150, 180, 210, 230, 240, 260]
# ]
#
# 1. Select rows 2 through 5.
# 2. From this new array, select every second column,
#    starting with the first selected column.
# 3. Calculate the total for each row.
# 4. Find the row with the highest total.
# 5. Find the row with the lowest total.
# 6. Sort the selected rows according to their totals in ascending order.
# 7. From the sorted result, select the last two rows.
# 8. Calculate the average of all values in these final two rows.
# 9. Print the intermediate arrays and final results.


# EXERCISE 4
# Create the following 2D NumPy array:
#
# data = [
#     [45, 12, 78, 34, 91, 56],
#     [23, 67, 89, 15, 42, 73],
#     [81, 29, 54, 96, 38, 62],
#     [17, 85, 31, 70, 49, 88],
#     [64, 21, 93, 46, 75, 19]
# ]
#
# 1. Select rows 1 through 5 in reverse order.
# 2. From this reversed array, select columns 2 through 6,
#    also in reverse order.
# 3. Replace every value greater than 80 with 100.
# 4. Replace every value below 30 with 0.
# 5. Calculate the mean of each row.
# 6. Find the index of the row with the highest mean.
# 7. Calculate the cumulative sum of each row.
# 8. Print the modified array, row means, highest-mean row index,
#    and cumulative sums.


# EXERCISE 5
# Create a NumPy array containing:
# 15, 42, 8, 73, 31, 56, 91, 24, 67, 38, 85, 19
#
# 1. Select every second element starting from the first element.
# 2. From this new array, select only values greater than 30.
# 3. Calculate the mean and standard deviation of the filtered values.
# 4. Find the index of the smallest value in the filtered array.
# 5. Find the index of the largest value in the filtered array.
# 6. Create a new array where:
#    - values greater than 70 become 70
#    - values below 40 become 40
#    - all other values remain unchanged
# 7. Sort the modified array in descending order.
# 8. Calculate the cumulative sum of the sorted array.
# 9. Print all important intermediate and final results.