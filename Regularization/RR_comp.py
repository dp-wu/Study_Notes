# Comparison of cost function of Ridge Regression and Linear Regression (without the regularization term)

# MSE(theta) = 1/m * sum(theta * x - y)^2
# J(theta) = MSE(theta) + [regularization term]
# [regularization term] = 0.5 * alpha * sum(theta^2)

# Suppose we have two points A(1, 1.5), B(2, 2)
# MSE(theta) = Z1, with a=2.5, b=5.5, c=2.125
# J(theta) = Z


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# X is theta
X = np.arange(-3.0, 3.0, 0.5)
# Y is alpha
Y = np.arange(0.0, 0.6, 0.05)
# Z is J(theta, alpha)
Z = (0.5*Y + 2.5) * X**2 + 5.5*X + 2.125
Z1 = 2.5 * X**2 + 5.5*X + 2.125


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.plot_wireframe(X, Y, Z)
ax.plot(X, Y, Z, c='r')
ax.plot(X, np.zeros(12), Z1, c='g')
ax.set_xlabel('Theta')
ax.set_ylabel('Alpha')
ax.set_zlabel('J')
plt.show()
