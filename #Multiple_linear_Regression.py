#Multiple_linear_Regression
import numpy as np  
import matplotlib.pyplot as plt

# -------------------------
# Data
# -------------------------

X1 = np.array([1, 2, 3, 4, 5])
X2 = np.array([2, 1, 4, 3, 5])

y = np.array([10, 12, 20, 22, 30])

#Combine X1 and X2

X = np.column_stack((X1, X2))

#Add columns of 1s

X_b = np.c_[np.ones(len(X)) ,X]

# calculate  coefficient
coefficients = (np.linalg.inv(X_b.T @X_b)@X_b.T @ y)

#Separate Coefficients
intercept = coefficients[0]
slope_X1 = coefficients[1]
slope_X2 = coefficients[2]

# -------------------------
# Make predictions
# -------------------------

y_pred = (
    intercept
    + slope_X1 * X1
    + slope_X2 * X2
)

# -------------------------
# Calculate residuals
# -------------------------

residuals = y - y_pred


# -------------------------
# Calculate R²
# -------------------------

ss_res = np.sum((y - y_pred) ** 2)

ss_total = np.sum((y - np.mean(y)) ** 2)

r2 = 1 - (ss_res / ss_total)

# -------------------------
# Print results
# -------------------------

print("Intercept:", intercept)

print("Slope X1:", slope_X1)

print("Slope X2:", slope_X2)

print("Predicted values:", y_pred)

print("Residuals:", residuals)

print("R² Score:", r2)
