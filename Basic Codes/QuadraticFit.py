import numpy as np
import matplotlib.pyplot as plt

# Data points
x = np.array([2,4,7,9,11])
y = np.array([14,27,48,55,68])

# Prepare the design matrix
A = np.vstack([x**2, x, np.ones(len(x))]).T

# Solve for coefficients using least squares
coeffs = np.linalg.lstsq(A, y, rcond=None)[0]
a, b, c = coeffs

# Generate x values for the fitted curve
x_fit =np.linspace(0, 12,100)
y_fit = a * x_fit**2 + b * x_fit + c

# Create the plot
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_fit, y_fit, color='red', label=f"Fitted Quadratic: y = {a:.2f}x**2 + {b:.2f}x + {c:.2f}")
plt.title("Quadratic Fit using least Squares Method")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()



