import pandas as pd

df = pd.DataFrame({
    'A':[np.nan,2,np.nan,np.nan,np.nan,8,np.nan],
    'B':[1.2,1.4,np.nan,6.2,None,1.1,4.3],
    'C':['a','?','c','d','--',np.nan,'d'],
    'D':[True, True, np.nan,None, False, True, False]
})

new = pd.Series([1 ,2, np.nan, 4, np.nan, 5, np.nan] ,dtype=pd.Int64Dtype() )
df['E'] = new

print(df)

# print(df.isna())
#
# print(df.isna().any())
#
# print(df.isna().sum())

# df.replace({"?": np.nan, "--": "misdata"}, inplace= True)
# print(df)
#
# df.dropna(axis=0,how="all",inplace=True)
# print(df)

print("================")

# df.dropna(axis=0,how="any",inplace=True)
# print(df)
#
# print("================")
# NaN이 3개 이상인 경우에만 drop
# df.replace({"?": np.nan, "--": np.nan}, inplace= True)
# print(df.notna().sum(axis=1))
# df.dropna(axis=0,thresh=4,inplace=True)
# print(df)

# df.fillna(99, inplace=True)
# print(df)

# mean = df['A'].mean()
# print(mean)
# df['A'].fillna(mean, inplace=True)
# print(df)


# df.fillna(axis=0, method='ffill',inplace=True)
# print(df)

# df.fillna(axis=0, method='bfill',inplace=True)
# print(df)

df.fillna(axis=0, method='ffill', limit=1,inplace=True)
print(df)