import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'spends': [2400, 2650, 2350, 4950, 3100, 2500, 5106, 3100, 2900, 1750],
    'income': [41200, 50100, 52000, 66000, 44500, 37700, 73500, 37500, 56700, 35600]
})

m = (10 * 1631016000 - 30806 * 494800) / (10 * 105821236 - 30806 * 30806)

b = (494800 - m * 30806) / 10

for_m = format(m, '.4f')
for_b = format(b, '.4f')

print(f'y = {for_m}x + {for_b} =')

exp_val_01 = m * 3500 + b
exp_val_02 = m * 5300 + b
