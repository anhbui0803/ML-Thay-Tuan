
import numpy as np
import matplotlib.pyplot as plt

# Height (cm)
# .T means tranpose of the matrix
x = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T

# Weight (kg)
y = np.array([[49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

# Visualize data
# plt.plot(x, y, "ro") # "ro" for red circles to appear on every point (x, y)
# plt.axis([140, 190, 45, 75])
# plt.xlabel("Height (cm)")
# plt.ylabel("Weight (kg)")
# plt.show()

# Building Xbar
one = np.ones((x.shape[0], 1)) # create a vector of 1, x.shape returns (n, m) so x.shape[0] returns n
Xbar = np.concatenate((one, x), axis = 1) # connect each element in vector 'one' with its corresponding in vector 'x'

# Calculating weights of the fitting line
A = np.dot(Xbar.T, Xbar) # multiply 2 matrices
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b) # w = ((A.T * A) ^ (-1)) * (A.T * y)

# Preparing the fitting line
w_0 = w[0][0] # w is a (2, 1) np.array
w_1 = w[1][0]
x0 = np.linspace(145, 185, 2, endpoint = True)
y0 = w_0 + w_1 * x0

# Drawing the fitting line
plt.plot(x.T, y.T, "ro") # data
plt.plot(x0, y0) # the fitting line
plt.axis([140, 190, 45, 75])
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.show()

# Estimate weight of 155cm and 160cm
y1 = w_1 * 155 + w_0
y2 = w_1 * 160 + w_0
print("Dự đoán cân nặng của người có chiều cao 155cm: %.2f (kg), số liệu thật 52 (kg)" %y1)
print("Dự đoán cân nặng của người có chiều cao 160cm: %.2f (kg), số liệu thật 56 (kg)" %y2)