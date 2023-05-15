# 데이터셋 예시
data = {
    'Height (Inches)': [72, 69, 74, None, 65, 120],
    'Weight (Pounds)': [180, 165, 190, 155, None, 140],
    'BMI': [24.4, 24.3, 24.4, None, None, None]
}

# 데이터셋을 Pandas DataFrame으로 변환합니다.
import pandas as pd
data = pd.DataFrame(data)

# 'Height (Inches)', 'Weight (Pounds)', 'BMI' 컬럼에서 조건에 맞는 dirty_mask를 생성합니다.
dirty_mask = (
    data['Height (Inches)'].isna() | data['Weight (Pounds)'].isna()

)

print(dirty_mask)