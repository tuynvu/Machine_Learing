import pandas as pd

df = pd.read_csv('vgsales.csv')
print("---------------------")
print(df.shape)
print("---------------------")
print(df.describe())
print("---------------------")
print(df.values)