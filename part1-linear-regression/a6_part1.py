import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# gets the data and sets x and y values
data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
print(x)
y = data["Blood Pressure"].values
print(y)

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)
print(x)

# sets the size of the graph
plt.figure(figsize=(6,4))

# creates a scatter plot and labels the axes
plt.scatter(x,y)
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure by Age")


# show the plot
plt.show()


# Create the model
model = LinearRegression().fit(x, y)
# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x, y)
print(coef, intercept, r_squared)

# Predict the the blood pressure of someone who is 43 years old.
x_predict = 43

prediction = model.predict([[x_predict]])

# Print out the linear equation and r squared value
print(f"Model's Linear Equation: y = {coef}x + {intercept}")
print(f"R Squared value: {r_squared}")


# Print out the prediction
print(f"Prediction when x is {x_predict}: {prediction}")
# Create the model in matplotlib and include the line of best fit


# prints the correlation coefficient
print("Pearson's Correlation: r = :", x.corr(y))

