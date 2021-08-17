import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

x = np.linspace(-3, 3, 30)
y = [2 * i + np.random.normal() for i in x]

x1 = [[i] for i in x]
y1 = [[i] for i in y]

model = linear_model.LinearRegression()
model.fit(x1, y1)

# print(model.predict([[3], [9]]))
print(model.coef_, model.intercept_)

plt.scatter(x, y)
y_p = [model.coef_[0][0] * i + model.intercept_[0] for i in x]
plt.plot(x, y_p, c='r')
plt.show()
