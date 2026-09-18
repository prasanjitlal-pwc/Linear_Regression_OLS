## Simple Linear Regression from Scratch using OLS ##Multiple Linear Regression from Scratch

Implemented **Simple Linear Regression from scratch** using the **Ordinary Least Squares (OLS)** method with NumPy.

### Steps Implemented

* Calculated the mean of `X` and `y`
* Calculated the **slope** and **intercept** using OLS
* Generated predicted values (`y_pred`)
* Calculated **residuals**
* Calculated **SSE (Sum of Squared Errors)**
* Calculated **SST (Total Sum of Squares)**
* Calculated **R² (Coefficient of Determination)**
* Printed the model results
* Visualized the actual data and regression line using Matplotlib

### Workflow

`Data → Mean → Slope & Intercept → Predictions → Residuals → SSE & SST → R² → Visualization`

This project implements Multiple Linear Regression from scratch using NumPy and the Ordinary Least Squares (OLS) Normal Equation.

What I implemented
Created two independent variables: X1 and X2
Combined the features into a single input matrix
Added a column of 1s to calculate the intercept
Calculated regression coefficients using the Normal Equation
Extracted the intercept and slopes for each feature
Generated predicted values
Calculated residuals
Calculated the R² score to evaluate model performance
Regression Equation

The model follows:

[
\hat{y} = b_0 + b_1X_1 + b_2X_2
]

Where:

b0 = intercept
b1 = coefficient for X1
b2 = coefficient for X2
ŷ = predicted value
OLS Normal Equation

The coefficients are calculated using:

[
\beta = (X^TX)^{-1}X^Ty
]

Model Evaluation

Residuals are calculated as:

[
Residual = y - \hat{y}
]

R² is used to measure how much variation in the target variable is explained by the regression model.

Tools Used
Python
NumPy
