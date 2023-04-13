import pandas as pd

df = pd.DataFrame({'a' : [i for i in range(1, 11)], 'b' : [i for i in range(11, 21)], 'c' : [i for i in range(21, 31)]})





# a, c 열 출력
print( df[['a', 'c']])

# a 가 3 이상인 데이터 출력
print( df[df.a >= 3])

# c 가 최댓값인 데이터 출력
print( df[df.c == df.c.max()])

# a 가 3 이상인 데이터 중 a, c 열만 출력
print(df[df.a >= 3][['a', 'c']])

# a 가 3 이상이고, b 가 16 미만인 데이터 출력
df[(df['a']>=3) & (df['b'] < 16)]

# a, b, c를 합한 total 컬럼을 추가하라.
# total 이 50 이상이면 'A',  50미만 40이상이면 'B', 40미만이면 'C' 등급을 지정하는 'grade' 컬럼을 추가하라. ( 중첩 조건문 np.where 이용 )
# grade를 오름차순으로 정렬하라. ( sort_values )

import numpy as np
df['total']= df.a+df.b+df.c
#df[ 'grade' ] = np.where( df.total >=50, 'A', np.where( df.total >=40 , 'B', 'C') )
#print(df)
def grade_total( total ) :
  if total >= 50 : 
    return 'A'
  elif total >=40 :
    return 'B'
  else :
    return 'C'
df['grade'] = df.total.apply(grade_total)
print(df)