# bicycle_out.csv / bycicle.csv / bicycle_dup   업로드

from google.colab import files
uploaded = files.upload()

# 날짜 데이터
import pandas as pd
import numpy as np
df = pd.read_csv( './bicycle.csv', encoding='euc-kr')

df.head()


# 결측값 확인
df.isnull() #df.notnull()
df.isnull().sum()

#결측 데이터 제거
df_droprow = df.dropna(axis=0)
df_dropcolumn = df.dropna(axis=1)
print( df_droprow.isnull().sum() )
print(df_droprow.columns)
print(df_dropcolumn.columns)