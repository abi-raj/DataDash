from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5,6,7,8]).reshape((-1,1))
y=np.array([2,3,4,5,6,7,8,9]).reshape((-1,1))

reg=LinearRegression()
reg.fit(x,y)
plt.plot(x,y)


ypred=reg.predict([[4,5]])
print(ypred)
plt.show()