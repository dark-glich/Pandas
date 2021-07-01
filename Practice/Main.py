import pandas as pd
# Pandas is a python framework that is used to read & edit data from 
# different datatypes

# From .csv
csv = pd.read_csv('Data/pokemon_data.csv')  
print(csv.head(5))

# From .txt
txt = pd.read_csv('Data/pokemon_data.txt', delimiter='\t')
print(txt.tail(5))

# From .xlsx
# to read excel file openpyxl module has to be installed
xlsx = pd.read_excel('Data/pokemon_data.xlsx')
print(xlsx)

# Reading Header of the data
print(csv.columns)

# Reading a specific column / columns
print(csv['Name'])
print(csv[['Name', 'Attack', 'Defense']])

# Reading a specific row / rows
print(csv.iloc[200])
print(csv.iloc[30:35])

# Reading a specific cell
print(csv.iloc[2,3]) # csv.iloc[column, row]

