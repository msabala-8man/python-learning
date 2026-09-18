import pandas as pd
import numpy as np

df = pd.read_excel(
    "datasets/Online Retail.xlsx",
    engine="openpyxl"
)

print(df.head())
print(df.shape)
print(df.columns)

numeric_data = df[["Quantity", "UnitPrice"]].to_numpy()

print(numeric_data)
print(numeric_data.shape)
print(numeric_data.ndim)

quantity = numeric_data[:, 0]
unit_price = numeric_data[:, 1]

# print(quantity)
# print(unit_price)

revenue = quantity * unit_price

print(revenue)
print(revenue.shape)
# print(np.mean(revenue))
# print(np.min(revenue))
# print(np.max(revenue))

# EXERCISE 1
# Using the revenue array:
#
# 1. Calculate the total revenue across all rows.
# 2. Calculate the average transaction value.
# 3. Find the smallest transaction value.
# 4. Find the largest transaction value.
# 5. Count how many transactions have a revenue greater than 100.
#
# Print all five results.

numeric_data_revenue = np.concatenate((numeric_data, revenue))

print(np.sum(numeric_data_revenue[::, -1::]))
print(np.mean(numeric_data_revenue[::, -1::]))
print(np.min(numeric_data_revenue[::, -1::]))
print(np.max(numeric_data_revenue[::, -1::]))
print(np.sum(numeric_data_revenue[::, -1::] > 100))