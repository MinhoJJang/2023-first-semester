import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
x = np.array([6, 16, 26, 36, 46, 56]).reshape((-1, 1))
y = np.array([4, 23, 10, 12, 22, 35])

model = LinearRegression()
model.fit(x,y)

model.coef_
model.intercept_

y_pred = model.predict(x)
r_sq = model.score(x,y)

plt.scatter(x,y)
plt.plot(x,y_pred)
plt.plot(x,y)
plt.show()

