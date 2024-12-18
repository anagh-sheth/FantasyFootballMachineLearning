import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

data = pd.read_csv('all2022data.csv')
print(data.head())
features = [
    'Age', 'Rec', 'Tgt', 'TD', 'Y/G', 'Touch', 'Y/G', 'Y/G.1']
X = data[features]
y = data['FantPt']

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='b')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='r', linestyle='--', linewidth=2)
plt.title('Actual vs Predicted Fantasy Football Points')
plt.xlabel('Actual Points')
plt.ylabel('Predicted Points')
plt.grid(True)
plt.show()

# Display feature importance (coefficients)
coefficients = pd.DataFrame({'Feature': features, 'Coefficient': model.coef_})
print(coefficients.sort_values(by='Coefficient', ascending=False))