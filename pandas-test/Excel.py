import pandas as pa
import numpy as np

df = pa.read_excel(open("C:\\Users\\Rod\\Documents\\20170816_10002_191.xlsx",'rb'),sheetname=0);
print(df['Model Name'].unique());
print(df['Ext Cost'].sum())