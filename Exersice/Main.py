import pandas as pd 
import os

# Merging 12 months sales data into single csv file
files = [file for file in os.listdir('Exersice/Data/Input')]
data = pd.DataFrame()
for file in files:
    df = pd.read_csv(f'Exersice/Data/Input/{file}')
    data = pd.concat([data, df])
    
data.to_csv('Exersice/Data/Output/all_data.csv')