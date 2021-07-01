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

# Getting a conditional cells
print(csv.loc[csv['HP'] > 100]) #prints all cells whose hp is greater than 100

# Getting mathematical info from data
print(csv.describe())

# Sorting Data 
print(csv.sort_values('Type 1')) # sortes data according to Type 1
print(csv.sort_values(['Type 1', 'HP']))

# Creating a column
csv['Total'] = csv['Attack'] + csv['Defense']
print(csv.head(5))

# Deleting a column from Data
csv = csv.drop(columns=['Type 2'])
print(csv.head(3))