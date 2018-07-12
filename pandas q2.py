import pandas as pd
import numpy as np

df=pd.read_csv("File.csv")
print("A.First Five rows of Dataframe")
print(df.head())
print("#"*100)
print("B.First 10 rows of Dataframe")
print(df.head(10))
print("#"*100)
print("C.Some statistics Function On This DataFrame")
print("1.Sum:\n",df.sum())
print("*"*100)
print("2.Row Wise Sum:\n",df.sum(1))
print("*"*100)
print("3.Mean:\n",df.mean())
print("*"*100)
print("4.Standred Daviation:\n",df.std())
print("*"*100)
print("5.variance:\n",df.var())
print("*"*100)

print("6.Summarizing the data:\n",df.describe())
print("#"*100)
print("D.Last 5 rows of Dataframe")
print(df.tail())
print("#"*100)

df1 = df[df.columns[1]]
print("Some Statistics function on these 2nd column:\n")
a=df1.describe(include=['object'])
print(a)
