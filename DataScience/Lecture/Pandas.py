import numpy as np
import pandas as pd

# pandas으로 만들 수 있는 데이터셋
#
# Series : 1차원 배열
# DataFrame : 2차원 배열
#
#

# 1. Series 만들기
s = pd.Series([1, 2, 4, np.nan, 6, 3])
print(s)

arr = [1, 2, 3]
d = pd.Series(arr)
print(d)

# 2. DataFrame 만들기
df = pd.DataFrame(np.random.randn(6, 4))
print(df)

dates = pd.date_range('20221229 12:11:38', periods=6, freq='D')
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)

df.head()
df.tail()
df.index
df.columns

df.to_numpy()

df.sort_values(by='A', ascending=True)  # 오름차순

students = [('jack', 'Apples', 34),
            ('Riti', 'Mangos', 31),
            ('Aadi', 'Grapes', 30),
            ('Sonia', 'Apples', 32),
            ('Lucy', 'Mangos', 33),
            ('Mike', 'Apples', 35)
            ]

dfx = pd.DataFrame(students, columns=['Name', 'Product', 'Sale'])

dfx['Product'] == 'Apples'  # Product가 Apple이면 True, 이외는 False인 Series를 리턴한다.
subDfx = dfx[(dfx['Product'] == 'Apples') == False]

df['A']
df[2:4][['A', 'B']]  # 가능
# df[2:4]['A', 'B'] # 불가능

# loc와 iloc의 차이, 사용법

# loc : 인덱스의 label을 기준으로 선택
df.loc[dates[0]]  # 0번째 행 출력
df.loc[:]  # 전체 df 출력
df.loc[:, ['A']]  # A 열 출력
df.loc[:, ['A', 'B']]  # A, B 열 출력
df.loc[:, df.columns[0]]  # 0번째 column 출력

# iloc: 위치를 기반, index 기반으로 찾음 iloc의 i가 index임
df.iloc[0]  # Series 타입으로 반환
df.iloc[0:2]  # df 타입으로 반환

df.iloc[3:5, 0:3]
#                             A         B         C
# 2023-01-01 12:11:38  1.565205  1.172675  0.114149
# 2023-01-02 12:11:38  0.189984  0.727252 -0.106850

df3 = df.copy()
df3['E'] = pd.Series([2, 3, 4, 5, 6, 7], index=df3.index, )

# 값 바뀌기

# 마찬가지로 at와 iat 이 있다.
df3.at[dates[0], 'A'] = 0

df3.iat[0, 1] = 0

# 이건 범위로 바꿀수는 없다.
# 범위로 바꾸려면, loc, iloc 등을 사용해서 바꿔야 한다.

df3.loc[dates[0], :] = np.array([5.] * 5)
df3.iloc[:, [0]] = np.array([1.33] * len(df3))

grade = pd.Series(['A', 'B', 'C', 'C', 'C', 'A', 'B'])
score = pd.DataFrame({'id': [1, 2, 3, 4, 5, 6, 7], 'grade': grade.astype('category')})

score['grade'].cat.categories = ['수', '우', '미']

score['grade'] = score['grade'].cat.set_categories(['1', '2', '3', '4'])

# 새로 컬럼을 만들수도 있음. 채워지지 않은 나머지는 NaN으로 배정됨
df3.loc[0:3, 'BB'] = 1
df3.dropna(how='any', thresh=1)
