# (1) 상하 결합

import pandas as pd

df1 = pd.DataFrame({'A' : [1, 2, 3], 'B' : [11, 12, 13], 'C' : [21, 22, 23]})
df2 = pd.DataFrame({'A' : [4, 5, 6], 'B' : [14, 15, 16], 'C' : [24, 25, 26]})

pd.concat([df1, df2], ignore_index = True)

# NaN : Not of Number => 결측값(값을 측정할 수 없음)

pd.concat([df1, df2], join='inner')


# (2) 좌우 결합