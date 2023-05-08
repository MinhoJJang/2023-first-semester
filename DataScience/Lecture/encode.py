import numpy as np
from sklearn.preprocessing import OrdinalEncoder

# 범주형 데이터
categorical_data = np.array([['red', 'small'],
                             ['blue', 'medium'],
                             ['green', 'large'],
                             ['red', 'large'],
                             ['blue', 'small']])

# OrdinalEncoder 객체 생성
encoder = OrdinalEncoder()

# 데이터에 맞게 인코더를 학습하고 변환
encoded_data = encoder.fit_transform(categorical_data)

# 변환된 데이터 출력
print(encoded_data)

import numpy as np
from sklearn.preprocessing import OneHotEncoder

# 범주형 데이터
categorical_data = np.array([['red', 'small'],
                             ['blue', 'medium'],
                             ['green', 'large'],
                             ['red', 'large'],
                             ['blue', 'small']])

# OneHotEncoder 객체 생성
encoder = OneHotEncoder()

# 데이터에 맞게 인코더를 학습하고 변환
encoded_data = encoder.fit_transform(categorical_data).toarray()

# 변환된 데이터 출력 (희소 행렬 형태)
print(encoded_data)
