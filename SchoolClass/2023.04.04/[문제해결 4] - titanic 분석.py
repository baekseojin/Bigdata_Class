import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

print(df.head())
print(df.tail())

df.info() # 컬럼별 정보
df.describe() # 컬럼에 대한 요약 통계
df.describe(include='object')


# 전체 데이터 중 나이가 15세 미만인 승객
print( df[ df.age < 15 ] )

#s 남자이면서 1등석 승객
print( df[ ( df['sex'].isin(['male'] ) ) & ( df['class'].isin( ['First'] )  )] ) 
print( df[ ( df['sex'].isin(['male'] ) ) & ( df['class'].isin( ['First'] )  )]['who']  ) # 조건에 맞는'who'만 출

#fare를 30이상 40미만 지불한 승객
print( df[  (df.fare >=30) & (df.fare <40) ]['fare'] )

#나이의 평균과 중앙값
print( df.age.mean(), df.age.median() )

# mean() : 평균
# median() : 중앙값
# -> 성인이 좀 더 많다.

# 결측값 확인
print(df.isnull().sum())

# 피벗 테이블
res = pd.pivot_table( df, 
                     index =['class', 'sex'], 
                     columns='survived', values=['age', 'fare'], 
                     aggfunc = ['mean', 'max'] )
print( res )

#성별 생존자 수 확인
print( df.groupby('sex').sum()['survived'] )
print('='*100)
res2 = pd.pivot_table( df, 
                     index =['sex'], columns='survived',  aggfunc = 'size' )
print( res2 )

#탑승지별 생존자수/사망자수 확인(그래프)
sns.countplot( data=df, x='embarked', hue='survived')

#크로스탭
print( df['survived'].value_counts())
pd.crosstab(df['who'], df['pclass'])