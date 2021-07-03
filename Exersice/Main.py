import pandas as pd 
import os

# Merging 12 months sales data into single csv file
files = [file for file in os.listdir('Exersice/Data/Input')]
data = pd.DataFrame()
for file in files:
    df = pd.read_csv(f'Exersice/Data/Input/{file}')
    data = pd.concat([data, df])
    
data.to_csv('Exersice/Data/Output/all_data.csv')

# Remove row with Nan value
data.dropna(subset=['Order Date'], inplace=True)

# Removing other non integer rows
data = data[data['Order Date'].str[0:2] != 'Or']

# Creating a month column
data['Month'] = data['Order Date'].str[0:2]
data['Month'] = data['Month'].astype('int16')

# Creating a total column
data['Price Each'] =  data['Price Each'].astype('float32')
data['Quantity Ordered'] = data['Quantity Ordered'].astype('int32')
data['Total'] = data['Price Each'] * data['Quantity Ordered']

# Which month has best sales
print(data.groupby('Month').sum())
