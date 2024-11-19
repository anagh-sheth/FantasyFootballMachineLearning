import csv
import pandas as pd
df2022 = pd.read_csv("2022data.csv")
df2023 = pd.read_csv("2023data.csv")
df2024 = pd.read_csv("2024data.csv")
dfFantasy2022 = pd.read_csv("2022fantasydata.csv")
dfFantasy2023 = pd.read_csv("2023fantasydata.csv")
dfFantasy2024 = pd.read_csv("2024fantasydata.csv")

print(df2022.shape, df2023.shape, df2024.shape)
print(dfFantasy2022.shape, dfFantasy2023.shape, dfFantasy2024.shape)

#df2022 = df2022.iloc[1:]
#df2022.to_csv('2022data.csv', index=False)

#df2023 = df2023.iloc[1:]
#df2023.to_csv('2023data.csv', index=False)

#df2024 = df2024.iloc[:, :-1]
#df2024.to_csv('2024data.csv', index=False) 
#print(df2024.head())
#df2023 = df2023.iloc[:, :-1]
#df2023.to_csv('2023data.csv', index=False) 
#print(df2023.head())
#df2022 = df2022.iloc[:, :-1]
#df2022.to_csv('2022data.csv', index=False) 
#print(df2022.head())

#dfFantasy2022 = dfFantasy2022.drop(dfFantasy2022.columns[4:25], axis=1)
#dfFantasy2022.to_csv('2022fantasydata.csv', index=False)
#print(dfFantasy2022.head())

#dfFantasy2023 = dfFantasy2023.drop(dfFantasy2023.columns[4:25], axis=1)
#dfFantasy2023.to_csv('2023fantasydata.csv', index=False)
#print(dfFantasy2023.head())

#dfFantasy2024 = dfFantasy2024.drop(dfFantasy2024.columns[4:25], axis=1)
#dfFantasy2024.to_csv('2024fantasydata.csv', index=False)
#print(dfFantasy2024.head())