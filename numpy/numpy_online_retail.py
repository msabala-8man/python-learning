import pandas as pd
import numpy as np

df = pd.read_excel(
    "../datasets/Online Retail.xlsx",
    engine="openpyxl"
)

numeric_data = df[["Quantity", "UnitPrice"]].to_numpy()

quantity = numeric_data[:, 0]
unit_price = numeric_data[:, 1]

revenue = quantity * unit_price

numeric_data = np.column_stack((numeric_data, revenue))

print(numeric_data.shape)

np.save("../datasets/online_retail_numeric.npy", numeric_data)