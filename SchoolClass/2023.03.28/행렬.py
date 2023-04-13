# (1) 7월과 8월의 A사 매출을 행렬로 나타내시오.
import pandas as pd

jul = pd.DataFrame({
    '지역':['부산', '서울', '대구'],
    '음료수':[1, 3.3, 1.2],
    '아이스크림':[3.5, 1.5, 1],
    '과자류':[2, 1, 2]
})

aug = pd.DataFrame({
    '지역':['부산', '서울', '대구'],
    '음료수':[1.5, 3, 2],
    '아이스크림':[3, 2, 1.2],
    '과자류':[2, 1.4, 2]
})

print(jul)
print(aug)

# (2) 7월과 8월의 총 매출 현황을 행렬로 나타내시오.

jul['지역총합'] = jul.iloc[:, :].sum(axis=1)
print(jul)
print('7월 총합 : ' , jul['지역총합'].sum())
aug['지역총합'] = aug.iloc[:, :].sum(axis=1)
print(aug)
print('8월 총합 : ', aug['지역총합'].sum())


# (3) 7월 대비 8월의 매출 증감량을 행렬로 나타내시오.
diff = aug.iloc[:, 1:4] - jul.iloc[:, 1:4]
print(diff)

jul['month'] = [ 7 for i in range(len(jul)) ]
print(jul)
aug['month'] = [ 8 for i in range(len(aug)) ]
print(aug)

sales = pd.concat([jul, aug])
print(sales)


