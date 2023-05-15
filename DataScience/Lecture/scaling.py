import pandas as pd
import numpy as np
from sklearn import preprocessing

a = np.random.randn(1000)
b = np.random.randn(1000)

df = pd.DataFrame([a,b])

scaler = preprocessing.MinMaxScaler()
df_scaled = scaler.fit_transform(df)

