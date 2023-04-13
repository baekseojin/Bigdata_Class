import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("titanic")
df.head()
df.tail()
df.info() # 컬럼별 정보
df.describe() # 컬럼에 대한 요약 통계
df.describe(include='object')
df['who'].value_counts()
sns.countplot( x='pclass', hue='sex', data=df )
