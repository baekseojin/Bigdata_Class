# 안정은쌤 : ENTP

# 데이터 복사
import pandas as pd
df = pd.DataFrame({'a':[1, 2, 3], 'b':[4,5,6], 'c':[7,8,9]})

df2 = df
df.columns = ['d', 'e', 'f']
print(df)
print(df2)

import copy
df. pd.DataFrame( {'a': [1, 2, 3], 'b': [4, 5, 6], 'c':[7, 8, 9] } )
df2 = copy.deepcopy(df)

