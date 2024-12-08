import numpy as np

def linear_regression(X, y, learning_rate=0.01, epochs=1000):
    m, n = X.shape
    X = np.hstack((np.ones((m, 1)), X))  # Add bias term
    weights = np.zeros(n + 1)

    for _ in range(epochs):
        predictions = np.dot(X, weights)
        errors = predictions - y
        gradient = np.dot(X.T, errors) / m
        weights -= learning_rate * gradient

    return weights

# Example usage
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1.2, 1.9, 3.0, 3.9, 5.1])
weights = linear_regression(X, y)
print("Learned weights:", weights)
