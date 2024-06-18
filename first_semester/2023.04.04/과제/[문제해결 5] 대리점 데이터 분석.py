import pandas as pd
import numpy as np

df = pd.read_csv( './bicycle.csv', encoding='euc-kr' )

df['month'] = pd.to_datetime( df['대여일시'] ).dt.strftime('%Y%m')
print(df.month)

res = df.pivot_table( index='month', columns='대여소명', aggfunc="size", fill_value=0)
print(res)

