import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    'spends': [2400, 2650, 2350, 4950, 3100, 2500, 5106, 3100, 2900, 1750],
    'income': [41200, 50100, 52000, 66000, 44500, 37700, 73500, 37500, 56700, 35600]
})

# Fit a linear regression model
X = data['spends'].values.reshape(-1, 1)
y = data['income'].values.reshape(-1, 1)
reg = LinearRegression().fit(X, y)

# Get the coefficients and the intercept
slope = reg.coef_[0][0]
intercept = reg.intercept_[0]

# Create a regression line
reg_line = slope * X + intercept

# Visualize the scatter plot and the regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='spends', y='income')
plt.plot(X, reg_line, color='red', label=f'y = {slope:.4f}x + {intercept:.4f}')
plt.xlabel('Spends')
plt.ylabel('Income')
plt.legend()
plt.title('Spends vs Income with Regression Line')
plt.show()
