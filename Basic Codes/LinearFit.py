
# Linear Fit using least square method

import numpy as np
import matplotlib.pyplot as plt

# Function for performing linear squares fitting
def least_squares_fit(x,y):

    # Prepare the matrix A for the equation A * [n,b] = y
    A = np.vstack((x, np.ones(len(x)))).T

    n, b = np.linalg.lstsq(A, y, rcond=None)[0]
    return n, b

# Example data
x = np.array([1,6,11,16,20,26])
y = np.array([13,16,17,23,24,31])

# Perform least squares fitting
n, b = least_squares_fit(x,y)

# Generate the fitted line
y_fit = n * x + b

# Plot the data and the fitted line
plt.figure(figsize = (6,4))
plt.scatter(x,y, color="blue", label="Data Points")
plt.plot(x, y_fit, color="red", label= f"Best fit line: y = {n:.2f}x + {b:.2f}")
plt.title("Linear fit using least squares method")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Print the coefficients
print(f"Slop (m): {n}")
print(f"Intercept (b): {b}")